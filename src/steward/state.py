"""Events in, `(state, blocked_on)` out.

A pure function: the same events give the same answer, with no network call and
no model in the path.

CHECKS_FAILED and CONFLICTED are in ROADMAP's diagram and not here. Both need
check runs and mergeability, and ingestion pulls neither.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

from steward.model import Event, EventKind, PullRequestReviewState, ReviewPayload


class WorkflowState(StrEnum):
    DRAFT = "DRAFT"
    # Open, and nothing has said who should look at it.
    UNTRIAGED = "UNTRIAGED"
    REVIEW_WAIT = "REVIEW_WAIT"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    RE_REVIEW_WAIT = "RE_REVIEW_WAIT"
    APPROVED = "APPROVED"
    MERGED = "MERGED"
    CLOSED = "CLOSED"


class BlockedOn(StrEnum):
    AUTHOR = "AUTHOR"
    REVIEWER = "REVIEWER"
    # Approved and not merged: whoever holds the merge button.
    MERGER = "MERGER"
    NOBODY = "NOBODY"
    UNKNOWN = "UNKNOWN"


class Derivation(StrEnum):
    """Where an answer came from."""

    EVENT = "EVENT"
    POLICY = "POLICY"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True, slots=True)
class Interval:
    start: datetime
    end: datetime | None
    state: WorkflowState
    blocked_on: BlockedOn
    derivation: Derivation


# Merging also closes, and both can carry the same timestamp. The tie breaks
# toward MERGED.
_TERMINAL = {EventKind.MERGED: 0, EventKind.CLOSED: 1}


def fold(events: Iterable[Event]) -> list[Interval]:
    """Every interval a pull request has been through, oldest first.

    The last interval has no end, whether it is still running or terminal.
    """
    ordered = sorted(
        events,
        key=lambda event: (
            event.occurred_at,
            event.kind is not EventKind.OPENED,
            _TERMINAL.get(event.kind, 0),
        ),
    )
    if not ordered:
        return []

    draft = _opened_as_draft(ordered)
    state = WorkflowState.DRAFT if draft else WorkflowState.UNTRIAGED
    blocked = BlockedOn.AUTHOR if draft else BlockedOn.UNKNOWN
    # An untriaged pull request has no answer until steward.toml supplies one.
    derivation = Derivation.EVENT if draft else Derivation.UNKNOWN

    intervals: list[Interval] = []
    start = ordered[0].occurred_at
    requested = False

    def switch(
        at: datetime,
        to: WorkflowState,
        on: BlockedOn,
        how: Derivation = Derivation.EVENT,
    ) -> None:
        nonlocal state, blocked, derivation, start
        if to is state and on is blocked:
            return
        if at > start:
            intervals.append(Interval(start, at, state, blocked, derivation))
        state, blocked, derivation, start = to, on, how, at

    for event in ordered:
        when = event.occurred_at

        if event.kind is EventKind.CONVERT_TO_DRAFT:
            switch(when, WorkflowState.DRAFT, BlockedOn.AUTHOR)

        elif event.kind is EventKind.READY_FOR_REVIEW:
            if requested:
                switch(when, WorkflowState.REVIEW_WAIT, BlockedOn.REVIEWER)
            else:
                switch(
                    when,
                    WorkflowState.UNTRIAGED,
                    BlockedOn.UNKNOWN,
                    Derivation.UNKNOWN,
                )

        elif event.kind is EventKind.REVIEW_REQUESTED:
            requested = True
            if state is not WorkflowState.DRAFT:
                switch(when, WorkflowState.REVIEW_WAIT, BlockedOn.REVIEWER)

        elif event.kind is EventKind.REVIEW:
            # A COMMENTED review creates no obligation: GitHub recorded neither
            # a request nor an approval, so neither does this.
            payload = event.payload
            if not isinstance(payload, ReviewPayload):
                continue
            if payload.state is PullRequestReviewState.CHANGES_REQUESTED:
                switch(when, WorkflowState.CHANGES_REQUESTED, BlockedOn.AUTHOR)
            elif payload.state is PullRequestReviewState.APPROVED:
                switch(when, WorkflowState.APPROVED, BlockedOn.MERGER)

        elif event.kind in (EventKind.COMMIT, EventKind.FORCE_PUSHED):
            # New work answers a review, approving or otherwise.
            if state in (WorkflowState.CHANGES_REQUESTED, WorkflowState.APPROVED):
                switch(when, WorkflowState.RE_REVIEW_WAIT, BlockedOn.REVIEWER)

        elif event.kind is EventKind.MERGED:
            switch(when, WorkflowState.MERGED, BlockedOn.NOBODY)
            break

        elif event.kind is EventKind.CLOSED:
            switch(when, WorkflowState.CLOSED, BlockedOn.NOBODY)
            break

    intervals.append(Interval(start, None, state, blocked, derivation))
    return intervals


def current(events: Iterable[Event]) -> Interval | None:
    """Where a pull request stands now."""
    intervals = fold(events)
    return intervals[-1] if intervals else None


def _opened_as_draft(ordered: Sequence[Event]) -> bool:
    """Whether the pull request was opened as a draft.

    GitHub emits no event for it, and `isDraft` reads false on every merged pull
    request whatever it was opened as. Whichever of the two draft events comes
    first says what the pull request was before it.

    One opened as a draft and never marked ready emits neither, and reads here
    as not a draft. No event in the log carries the opening state.
    """
    for event in ordered:
        if event.kind is EventKind.READY_FOR_REVIEW:
            return True
        if event.kind is EventKind.CONVERT_TO_DRAFT:
            return False
    return False
