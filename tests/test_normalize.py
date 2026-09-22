"""The normalizer, against a recorded response rather than invented events.

`tests/data/precogly_rest_timeline.json` holds one real `pulls.list` response
and the timeline of each pull request in it, kept verbatim. Hand-written
timeline JSON would only ever contain what someone already believed GitHub
sends; this contains what it sent.

It is replayed through `httpx.MockTransport`, so githubkit parses it exactly as
it would parse the live API and the test covers the real path from bytes to
`Event`. That is the recorded-cassette shape `ROADMAP.md` describes, one
endpoint short of `steward sync` being able to record its own.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import httpx
import pytest
from githubkit import GitHub

from steward.model import KIND_FOR_TYPENAME, EventKind, validate_payload
from steward.normalize import IGNORED, events_for_pull_request

FIXTURE = Path(__file__).parent / "data" / "precogly_rest_timeline.json"
TIMELINE = re.compile(r"^/repos/precogly/precogly/issues/(\d+)/timeline$")


@pytest.fixture(scope="module")
def github() -> GitHub[Any]:
    recorded = json.loads(FIXTURE.read_text())

    def replay(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/repos/precogly/precogly/pulls":
            return httpx.Response(200, json=recorded["pulls"])
        match = TIMELINE.match(request.url.path)
        if match:
            return httpx.Response(200, json=recorded["timelines"][match.group(1)])
        raise AssertionError(f"no recording for {request.url.path}")

    return GitHub("recorded", transport=httpx.MockTransport(replay))


def _pulls_and_timelines(gh: GitHub[Any]) -> list[tuple[Any, list[Any]]]:
    pulls = gh.rest.pulls.list(
        owner="precogly", repo="precogly", state="all", per_page=25
    ).parsed_data
    return [
        (
            pr,
            gh.rest.issues.list_events_for_timeline(
                owner="precogly", repo="precogly", issue_number=pr.number, per_page=100
            ).parsed_data,
        )
        for pr in pulls
    ]


def test_every_item_becomes_an_event_or_is_named_as_ignored(
    github: GitHub[Any],
) -> None:
    for pr, timeline in _pulls_and_timelines(github):
        kept = [
            item
            for item in timeline
            if getattr(item, "event", type(item).__name__) not in IGNORED
        ]
        # Plus OPENED, which GitHub emits no timeline item for.
        assert len(events_for_pull_request(pr, timeline)) == len(kept) + 1


def test_payloads_match_their_kinds(github: GitHub[Any]) -> None:
    # The normalizer validates as it builds; this checks what came out, so a
    # branch that skipped the call cannot pass unnoticed.
    for pr, timeline in _pulls_and_timelines(github):
        for event in events_for_pull_request(pr, timeline):
            validate_payload(event.kind, event.payload)


def test_events_are_ordered_by_time(github: GitHub[Any]) -> None:
    for pr, timeline in _pulls_and_timelines(github):
        times = [e.occurred_at for e in events_for_pull_request(pr, timeline)]
        assert times == sorted(times)


def test_opened_leads_everything_except_earlier_commits(github: GitHub[Any]) -> None:
    # A rebased commit keeps its original date, so it can sit before the pull
    # request. Anything else ahead of OPENED would be invented history.
    for pr, timeline in _pulls_and_timelines(github):
        events = events_for_pull_request(pr, timeline)
        opened = next(i for i, e in enumerate(events) if e.kind is EventKind.OPENED)
        assert all(e.kind is EventKind.COMMIT for e in events[:opened])


def test_source_ids_are_unique_within_a_pull_request(github: GitHub[Any]) -> None:
    # source_id is what makes a re-sync idempotent. A collision would make the
    # second sync a no-op for one of two events rather than for neither. Cross
    # references matter most here: REST gives them no id, so theirs is built
    # from the event's own fields.
    for pr, timeline in _pulls_and_timelines(github):
        ids = [e.source_id for e in events_for_pull_request(pr, timeline)]
        assert len(set(ids)) == len(ids)


def test_recording_exercises_most_of_the_model(github: GitHub[Any]) -> None:
    seen = Counter(
        event.kind
        for pr, timeline in _pulls_and_timelines(github)
        for event in events_for_pull_request(pr, timeline)
    )
    assert set(seen) >= {
        EventKind.OPENED,
        EventKind.COMMIT,
        EventKind.REVIEW,
        EventKind.LABELED,
        EventKind.MERGED,
        EventKind.CLOSED,
        EventKind.CROSS_REFERENCED,
        EventKind.COMMENT,
    }
    # Naming the gap is the point: these kinds have no coverage here, and the
    # corpus cassettes are what will have to supply them.
    missing = set(KIND_FOR_TYPENAME.values()) - set(seen)
    assert missing == {
        EventKind.ASSIGNED,
        EventKind.UNASSIGNED,
        EventKind.REVIEW_DISMISSED,
        EventKind.REVIEW_REQUEST_REMOVED,
        EventKind.UNLABELED,
    }
