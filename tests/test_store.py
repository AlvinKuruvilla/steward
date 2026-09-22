"""Writing the log, against a real database.

Skips unless `STEWARD_DATABASE_URL` is set. The events come from the recorded
response, replayed through githubkit, so what is written here is what a sync
would write.
"""

from __future__ import annotations

import json
import os
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import httpx
import psycopg
import pytest
from githubkit import GitHub

from steward.migrate import apply
from steward.model import Event
from steward.normalize import events_for_pull_request
from steward.store import record_sync, repository_id, write

ADMIN_URL = os.environ.get("STEWARD_ADMIN_DATABASE_URL")
FIXTURE = Path(__file__).parent / "data" / "precogly_rest_timeline.json"
TIMELINE = re.compile(r"^/repos/precogly/precogly/issues/(\d+)/timeline$")

pytestmark = pytest.mark.skipif(
    ADMIN_URL is None, reason="needs a database: set STEWARD_ADMIN_DATABASE_URL"
)


@pytest.fixture
def db() -> Iterator[psycopg.Connection[Any]]:
    assert ADMIN_URL is not None
    with psycopg.connect(ADMIN_URL) as conn:
        with conn.transaction():
            conn.execute("""
                DO $$
                DECLARE t record;
                BEGIN
                    FOR t IN SELECT tablename FROM pg_tables WHERE schemaname = 'public'
                    LOOP
                        EXECUTE format('DROP TABLE public.%I CASCADE', t.tablename);
                    END LOOP;
                END $$
            """)
        apply(conn)
        yield conn


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
    db: psycopg.Connection[Any], recorded_events: list[Event]
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


def test_payloads_survive_the_round_trip(
    db: psycopg.Connection[Any], recorded_events: list[Event]
) -> None:
    from steward.model import PAYLOAD_FOR, EventKind, payload_from_dict

    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    write(db, repo, recorded_events)

    stored = {
        source_id: (EventKind(kind), payload)
        for source_id, kind, payload in db.execute(
            "SELECT source_id, kind, payload FROM events"
        ).fetchall()
    }
    for event in recorded_events:
        kind, payload = stored[event.source_id]
        assert kind is event.kind
        assert payload_from_dict(kind, payload) == event.payload
        assert PAYLOAD_FOR[kind] is not None or event.payload is None


def test_the_repository_row_is_reused(db: psycopg.Connection[Any]) -> None:
    first = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    assert repository_id(db, "precogly", "precogly", "R_kgDOabc") == first
    assert db.execute("SELECT count(*) FROM repositories").fetchone() == (1,)


def test_record_sync_stamps_the_repository(db: psycopg.Connection[Any]) -> None:
    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    assert db.execute(
        "SELECT last_sync FROM repositories WHERE id = %s", (repo,)
    ).fetchone() == (None,)

    record_sync(db, repo)

    row = db.execute(
        "SELECT last_sync FROM repositories WHERE id = %s", (repo,)
    ).fetchone()
    assert row is not None and row[0] is not None
