"""The state engine, over the recorded response.

No database and no network: events come from the recording, through the
normalizer, into the fold.

The recording is one page of pull requests plus #322, which is older than that
page and is the case the audit turns on -- opened as a draft, merged, so
`isDraft` reads false and the draft interval exists only in the events.
"""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from itertools import pairwise
from pathlib import Path
from typing import Any

import httpx
import pytest
from githubkit import GitHub

from steward.model import (
    ActorRef,
    ActorType,
    Event,
    EventKind,
    PullRequestReviewState,
    ReviewPayload,
    SubjectType,
)
from steward.normalize import events_for_pull_request
from steward.state import BlockedOn, Derivation, Interval, WorkflowState, current, fold

FIXTURE = Path(__file__).parent / "data" / "precogly_rest_timeline.json"
TIMELINE = re.compile(r"^/repos/precogly/precogly/issues/(\d+)/timeline$")


@pytest.fixture(scope="module")
def by_number() -> dict[int, list[Event]]:
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
    return {
        pr.number: events_for_pull_request(
            pr,
            gh.rest.issues.list_events_for_timeline(
                owner="precogly", repo="precogly", issue_number=pr.number, per_page=100
            ).parsed_data,
        )
        for pr in pulls
    }


def _event(kind: EventKind, minute: int, payload: Any = None) -> Event:
    return Event(
        subject_type=SubjectType.PULL_REQUEST,
        subject_number=1,
        kind=kind,
        occurred_at=datetime(2026, 9, 1, 12, minute, tzinfo=UTC),
        source_id=f"{kind.value}:{minute}",
        actor="someone",
        actor_type=ActorType.USER,
        payload=payload,
    )


def test_no_events_is_no_answer() -> None:
    assert fold([]) == []
    assert current([]) is None


def test_intervals_are_contiguous(by_number: dict[int, list[Event]]) -> None:
    for events in by_number.values():
        intervals = fold(events)
        for earlier, later in pairwise(intervals):
            assert earlier.end == later.start
        assert intervals[-1].end is None


def test_a_commented_review_creates_no_obligation() -> None:
    # GitHub records neither a request nor an approval for a comment, so
    # neither does the engine. Precogly #382 merged this way.
    events = [
        _event(EventKind.OPENED, 0),
        _event(EventKind.REVIEW_REQUESTED, 1, ActorRef("reviewer", ActorType.USER)),
        _event(EventKind.REVIEW, 2, ReviewPayload(PullRequestReviewState.COMMENTED)),
    ]
    answer = current(events)
    assert answer is not None
    assert answer.state is WorkflowState.REVIEW_WAIT
    assert answer.blocked_on is BlockedOn.REVIEWER


def test_merging_beats_closing_on_a_tied_timestamp() -> None:
    # Merging also closes, and both events can share a timestamp.
    merged = _event(EventKind.MERGED, 5)
    closed = _event(EventKind.CLOSED, 5)
    for order in ([merged, closed], [closed, merged]):
        answer = current([_event(EventKind.OPENED, 0), *order])
        assert answer is not None
        assert answer.state is WorkflowState.MERGED


def test_a_push_after_approval_returns_it_to_a_reviewer() -> None:
    events = [
        _event(EventKind.OPENED, 0),
        _event(EventKind.REVIEW, 1, ReviewPayload(PullRequestReviewState.APPROVED)),
        _event(EventKind.COMMIT, 2),
    ]
    answer = current(events)
    assert answer is not None
    assert answer.state is WorkflowState.RE_REVIEW_WAIT
    assert answer.blocked_on is BlockedOn.REVIEWER


def test_a_draft_interval_is_recovered_from_events(
    by_number: dict[int, list[Event]],
) -> None:
    intervals = fold(by_number[322])
    drafts = [i for i in intervals if i.state is WorkflowState.DRAFT]
    assert len(drafts) == 1
    assert drafts[0].start.date() == datetime(2026, 8, 15, tzinfo=UTC).date()
    assert drafts[0].end is not None
    assert drafts[0].end.date() == datetime(2026, 8, 29, tzinfo=UTC).date()
    assert drafts[0].blocked_on is BlockedOn.AUTHOR


def test_an_untriaged_pull_request_says_unknown_rather_than_guessing(
    by_number: dict[int, list[Event]],
) -> None:
    # Without a policy rule there is no answer, and the engine says so rather
    # than naming an author or a reviewer.
    untriaged = [
        interval
        for events in by_number.values()
        for interval in fold(events)
        if interval.state is WorkflowState.UNTRIAGED
    ]
    assert untriaged, "the recording has no untriaged interval to check"
    assert all(i.blocked_on is BlockedOn.UNKNOWN for i in untriaged)
    assert all(i.derivation is Derivation.UNKNOWN for i in untriaged)


def test_every_interval_carries_its_derivation(
    by_number: dict[int, list[Event]],
) -> None:
    # A state with no derivation class is a claim with no provenance.
    for events in by_number.values():
        for interval in fold(events):
            assert isinstance(interval, Interval)
            assert interval.derivation in set(Derivation)
