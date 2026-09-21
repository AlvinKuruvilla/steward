"""The normalizer, against a recorded page rather than invented events.

`tests/data/precogly_pull_request_page.json` is one real response to the
generated `PullRequestPage` operation, kept verbatim. Hand-written timeline JSON
would only ever contain what someone already believed GitHub sends; this
contains what it sent. It will be replaced by the recorded cassettes ROADMAP.md
describes once `steward sync` exists to record them.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import pytest

from steward.github_api.pull_request_page import (
    PullRequestPage,
    PullRequestPageRepositoryPullRequestsNodes,
)
from steward.model import KIND_FOR_TYPENAME, EventKind, validate_payload
from steward.normalize import events_for_pull_request

PAGE = Path(__file__).parent / "data" / "precogly_pull_request_page.json"


@pytest.fixture(scope="module")
def pull_requests() -> list[PullRequestPageRepositoryPullRequestsNodes]:
    page = PullRequestPage.model_validate(json.loads(PAGE.read_text())["data"])
    assert page.repository is not None
    return [pr for pr in page.repository.pull_requests.nodes or [] if pr is not None]


def test_every_pull_request_normalizes(
    pull_requests: list[PullRequestPageRepositoryPullRequestsNodes],
) -> None:
    assert len(pull_requests) == 25
    for pr in pull_requests:
        events = events_for_pull_request(pr)
        # One per timeline item, plus the synthesized OPENED.
        assert len(events) == len(pr.timeline_items.nodes or []) + 1


def test_payloads_match_their_kinds(
    pull_requests: list[PullRequestPageRepositoryPullRequestsNodes],
) -> None:
    # The normalizer validates as it builds; this checks what came out, so a
    # branch that skipped the call cannot pass unnoticed.
    for pr in pull_requests:
        for event in events_for_pull_request(pr):
            validate_payload(event.kind, event.payload)


def test_events_are_ordered_by_time(
    pull_requests: list[PullRequestPageRepositoryPullRequestsNodes],
) -> None:
    for pr in pull_requests:
        events = events_for_pull_request(pr)
        assert [e.occurred_at for e in events] == sorted(e.occurred_at for e in events)


def test_opened_leads_everything_except_earlier_commits(
    pull_requests: list[PullRequestPageRepositoryPullRequestsNodes],
) -> None:
    # A rebased commit keeps its original committedDate, so it can sit days
    # before the pull request. The log keeps that time; anything else ahead of
    # OPENED would be the normalizer inventing history.
    for pr in pull_requests:
        events = events_for_pull_request(pr)
        opened = next(i for i, e in enumerate(events) if e.kind is EventKind.OPENED)
        assert all(e.kind is EventKind.COMMIT for e in events[:opened])


def test_source_ids_are_unique_within_a_pull_request(
    pull_requests: list[PullRequestPageRepositoryPullRequestsNodes],
) -> None:
    # source_id is what makes a re-sync idempotent. A collision would make the
    # second sync a no-op for one of the two events rather than for neither.
    for pr in pull_requests:
        ids = [event.source_id for event in events_for_pull_request(pr)]
        assert len(set(ids)) == len(ids)


def test_recorded_page_exercises_most_of_the_model(
    pull_requests: list[PullRequestPageRepositoryPullRequestsNodes],
) -> None:
    seen = Counter(
        event.kind for pr in pull_requests for event in events_for_pull_request(pr)
    )
    # Not every kind: this page has no dismissal, assignment or draft
    # conversion. Naming what it misses is the point -- the count is coverage
    # of the normalizer, and the gap is what the cassettes will have to add.
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
    missing = set(KIND_FOR_TYPENAME.values()) - set(seen)
    assert missing == {
        EventKind.ASSIGNED,
        EventKind.UNASSIGNED,
        EventKind.REVIEW_DISMISSED,
        EventKind.REVIEW_REQUEST_REMOVED,
        EventKind.UNLABELED,
    }
