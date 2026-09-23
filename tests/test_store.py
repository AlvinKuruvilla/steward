"""Writing the log, and reading it back.

The events come from the recorded response, replayed through githubkit, so what
is written here is what a sync would write.
"""

from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import replace
from pathlib import Path
from typing import Any

import httpx
import pytest
from githubkit import GitHub

from steward.model import Event
from steward.normalize import events_for_pull_request
from steward.store import read_events, record_sync, repository_id, write

FIXTURE = Path(__file__).parent / "data" / "precogly_rest_timeline.json"
TIMELINE = re.compile(r"^/repos/precogly/precogly/issues/(\d+)/timeline$")


@pytest.fixture(scope="module")
def recorded_events() -> list[Event]:
    recorded = json.loads(FIXTURE.read_text())

    def replay(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/repos/precogly/precogly/pulls":
            return httpx.Response(200, json=recorded["pulls"])
        match = TIMELINE.match(request.url.path)
        assert match, f"no recording for {request.url.path}"
        return httpx.Response(200, json=recorded["timelines"][match.group(1)])

    gh: GitHub[Any] = GitHub("recorded", transport=httpx.MockTransport(replay))
    pulls = gh.rest.pulls.list(
        owner="precogly", repo="precogly", state="all", per_page=25
    ).parsed_data
    return [
        event
        for pr in pulls
        for event in events_for_pull_request(
            pr,
            gh.rest.issues.list_events_for_timeline(
                owner="precogly", repo="precogly", issue_number=pr.number, per_page=100
            ).parsed_data,
        )
    ]


def test_a_second_sync_adds_nothing(
    db: sqlite3.Connection, recorded_events: list[Event]
) -> None:
    # V0's acceptance bar, in miniature.
    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    first = write(db, repo, recorded_events)
    second = write(db, repo, recorded_events)

    assert first == (len(recorded_events), 0)
    assert second == (0, len(recorded_events))
    assert db.execute("SELECT count(*) FROM events").fetchone() == (
        len(recorded_events),
    )


def test_events_survive_the_round_trip(
    db: sqlite3.Connection, recorded_events: list[Event]
) -> None:
    # Timestamps and payloads both cross as text; what comes back must be the
    # event that went in, timezone and all.
    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    write(db, repo, recorded_events)

    # One commit can sit on two pull requests, so the id alone is not a key.
    read = read_events(db, "precogly", "precogly")
    stored = {
        (event.subject_number, event.source_id): event
        for events in read.values()
        for event in events
    }
    assert len(stored) == len(recorded_events)
    for event in recorded_events:
        assert stored[event.subject_number, event.source_id] == event


def test_a_naive_timestamp_is_refused(
    db: sqlite3.Connection, recorded_events: list[Event]
) -> None:
    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    naive = replace(
        recorded_events[0],
        occurred_at=recorded_events[0].occurred_at.replace(tzinfo=None),
    )
    with pytest.raises(ValueError, match="no timezone"):
        write(db, repo, [naive])


def test_the_repository_row_is_reused(db: sqlite3.Connection) -> None:
    first = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    assert repository_id(db, "precogly", "precogly", "R_kgDOabc") == first
    assert db.execute("SELECT count(*) FROM repositories").fetchone() == (1,)


def test_record_sync_stamps_the_repository(db: sqlite3.Connection) -> None:
    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    assert db.execute(
        "SELECT last_sync FROM repositories WHERE id = ?", (repo,)
    ).fetchone() == (None,)

    record_sync(db, repo)

    row = db.execute(
        "SELECT last_sync FROM repositories WHERE id = ?", (repo,)
    ).fetchone()
    assert row is not None and row[0] is not None
