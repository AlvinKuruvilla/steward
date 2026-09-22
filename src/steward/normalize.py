"""GitHub's timeline, as Steward's events.

The log stores normalized events and nothing else, so this is the one place a
mistake becomes permanent: an event mapped wrong is written wrong, and fixing it
means re-syncing the repository, which re-reads GitHub as it is now rather than
as it was. Every event goes through `validate_payload` before it is constructed.

Dispatch is `isinstance` against githubkit's models, except for the six kinds
that arrive as `StateChangeIssueEvent` -- REST gives closes, merges, reopens,
draft conversions and force pushes one model discriminated by an `event` string,
so those branch on the string instead.

Unlike GraphQL's timeline, REST has no `itemTypes` filter, so this module is the
filter. Events with no bearing on who a pull request waits for are named in
`IGNORED`; anything in neither that set nor the dispatch raises, so a type
GitHub adds surfaces at sync time rather than leaving a silent gap in the log.
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import datetime

from githubkit.utils import UNSET
from githubkit_schemas.latest.models import (
    LabeledIssueEvent,
    PullRequestSimple,
    ReviewDismissedIssueEvent,
    ReviewRequestedIssueEvent,
    ReviewRequestRemovedIssueEvent,
    SimpleUser,
    StateChangeIssueEvent,
    Team,
    TimelineAssignedIssueEvent,
    TimelineCommentEvent,
    TimelineCommittedEvent,
    TimelineCrossReferencedEvent,
    TimelineReviewedEvent,
    TimelineUnassignedIssueEvent,
    UnlabeledIssueEvent,
)

from steward.model import (
    ActorRef,
    ActorType,
    CommitPayload,
    CrossReferencePayload,
    DismissalPayload,
    Event,
    EventKind,
    IssueStateReason,
    LabelPayload,
    Payload,
    PullRequestReviewState,
    ReviewPayload,
    StateReasonPayload,
    SubjectType,
    validate_payload,
)

# What a `StateChangeIssueEvent` is, when it is one of ours.
STATE_CHANGE_KINDS = {
    "closed": EventKind.CLOSED,
    "merged": EventKind.MERGED,
    "reopened": EventKind.REOPENED,
    "ready_for_review": EventKind.READY_FOR_REVIEW,
    "convert_to_draft": EventKind.CONVERT_TO_DRAFT,
    "head_ref_force_pushed": EventKind.FORCE_PUSHED,
}

# Events that reach the timeline and say nothing about who a pull request waits
# for. Naming them, rather than ignoring everything unrecognized, is what makes
# a new GitHub event type an error instead of a silent gap.
IGNORED = frozenset(
    {
        "added_to_project",
        "added_to_project_v2",
        "added_to_stack",
        "auto_merge_disabled",
        "auto_merge_enabled",
        "auto_rebase_enabled",
        "auto_squash_enabled",
        "automatic_base_change_failed",
        "automatic_base_change_succeeded",
        "base_ref_changed",
        "base_ref_force_pushed",
        "comment_deleted",
        "connected",
        "convert_to_issue",
        "copilot_work_finished",
        "copilot_work_started",
        "demilestoned",
        "deployed",
        "deployment_environment_changed",
        "disconnected",
        "head_ref_deleted",
        "head_ref_restored",
        "locked",
        "marked_as_duplicate",
        "mentioned",
        "milestoned",
        "moved_columns_in_project",
        "pinned",
        "project_v2_item_status_changed",
        "referenced",
        "removed_from_project",
        "removed_from_project_v2",
        "removed_from_stack",
        "renamed",
        "subscribed",
        "transferred",
        "unlocked",
        "unmarked_as_duplicate",
        "unpinned",
        "unsubscribed",
        "user_blocked",
    }
)


class NormalizationError(Exception):
    """A timeline item that cannot be stored without losing or inventing a fact."""


def events_for_pull_request(
    pr: PullRequestSimple, timeline: Iterable[object]
) -> list[Event]:
    """Every event this pull request's timeline carries, oldest first.

    OPENED is not necessarily first. A commit's date is author-controlled and
    survives a rebase, so it can predate the pull request it lands on -- by
    seconds usually, by up to three weeks in the corpus. The log keeps GitHub's
    timestamp; clamping it forward is a read-time decision for the fold.
    """
    events = [_opened(pr)]

    for item in timeline:
        kind: EventKind
        occurred_at: datetime
        source_id: str
        acted_by: SimpleUser | Team | None = None
        payload: Payload = None

        if isinstance(item, TimelineCommittedEvent):
            # No actor. REST names the commit's author, who is not necessarily
            # whoever put it on this branch, and guessing would be inventing.
            kind = EventKind.COMMIT
            occurred_at = _when(item.committer.date, "commit")
            source_id = item.node_id
            payload = CommitPayload(oid=item.sha)

        elif isinstance(item, TimelineCommentEvent):
            kind, occurred_at, source_id = (
                EventKind.COMMENT,
                item.created_at,
                item.node_id,
            )
            acted_by = _user(item.user)

        elif isinstance(item, TimelineReviewedEvent):
            # A pending review has never been submitted. You can only ever see
            # your own, so one reaching here means the fetch changed.
            if item.submitted_at is UNSET or item.submitted_at is None:
                raise NormalizationError(
                    f"review {item.node_id} has no submitted_at, state {item.state!r}"
                )
            kind, occurred_at, source_id = (
                EventKind.REVIEW,
                item.submitted_at,
                item.node_id,
            )
            acted_by = _user(item.user)
            payload = ReviewPayload(PullRequestReviewState(item.state.upper()))

        elif isinstance(
            item, ReviewRequestedIssueEvent | ReviewRequestRemovedIssueEvent
        ):
            kind = (
                EventKind.REVIEW_REQUESTED
                if isinstance(item, ReviewRequestedIssueEvent)
                else EventKind.REVIEW_REQUEST_REMOVED
            )
            occurred_at = _when(item.created_at, "review request")
            source_id = item.node_id
            acted_by = _user(item.actor)
            # REST names the team. GraphQL returned null for one it would not
            # resolve, which is the reason this module is not built on GraphQL.
            payload = _named(item.requested_reviewer, item.requested_team, item.node_id)

        elif isinstance(item, ReviewDismissedIssueEvent):
            # dismissed_review is the only record of what the review held:
            # GitHub overwrites the review's own state in place on dismissal.
            review = item.dismissed_review
            kind = EventKind.REVIEW_DISMISSED
            occurred_at = _when(item.created_at, "dismissal")
            source_id = item.node_id
            acted_by = _user(item.actor)
            payload = DismissalPayload(
                previous_state=PullRequestReviewState(review.state.upper()),
                review_id=str(review.review_id),
            )

        elif isinstance(
            item, TimelineAssignedIssueEvent | TimelineUnassignedIssueEvent
        ):
            kind = (
                EventKind.ASSIGNED
                if isinstance(item, TimelineAssignedIssueEvent)
                else EventKind.UNASSIGNED
            )
            occurred_at = _when(item.created_at, "assignment")
            source_id = item.node_id
            acted_by = _user(item.actor)
            payload = _named(item.assignee, None, item.node_id)

        elif isinstance(item, LabeledIssueEvent | UnlabeledIssueEvent):
            kind = (
                EventKind.LABELED
                if isinstance(item, LabeledIssueEvent)
                else EventKind.UNLABELED
            )
            occurred_at = _when(item.created_at, "label change")
            source_id = item.node_id
            acted_by = _user(item.actor)
            payload = LabelPayload(name=item.label.name)

        elif isinstance(item, TimelineCrossReferencedEvent):
            source = item.source.issue
            if source is UNSET or source is None:
                raise NormalizationError("cross-reference names no source")
            source_type = (
                SubjectType.PULL_REQUEST
                if getattr(source, "pull_request", None) not in (UNSET, None)
                else SubjectType.ISSUE
            )
            kind, occurred_at = EventKind.CROSS_REFERENCED, item.created_at
            # The one timeline event REST gives no id of any kind. The key must
            # be derivable from the event and stable across syncs, so it is
            # built from what the event reports and never from arrival order.
            source_id = (
                f"xref:{pr.number}:{source_type.value}:{source.number}"
                f":{occurred_at.isoformat()}"
            )
            acted_by = _user(item.actor)
            payload = CrossReferencePayload(
                source_type=source_type,
                source_number=source.number,
                # REST has no equivalent of GraphQL's willCloseTarget.
                will_close=False,
            )

        elif isinstance(item, StateChangeIssueEvent):
            if item.event in IGNORED:
                continue
            if item.event not in STATE_CHANGE_KINDS:
                raise NormalizationError(f"unhandled state change {item.event!r}")
            kind = STATE_CHANGE_KINDS[item.event]
            occurred_at = _when(item.created_at, item.event)
            source_id = item.node_id
            acted_by = _user(item.actor)
            if kind is EventKind.CLOSED and item.state_reason not in (UNSET, None):
                # Only issues close with a reason; a pull request carries none.
                payload = StateReasonPayload(
                    IssueStateReason(str(item.state_reason).upper())
                )

        else:
            name = getattr(item, "event", type(item).__name__)
            if name in IGNORED:
                continue
            raise NormalizationError(f"unhandled timeline item {name!r}")

        validate_payload(kind, payload)
        actor, actor_type = _actor(acted_by)
        events.append(
            Event(
                subject_type=SubjectType.PULL_REQUEST,
                subject_number=pr.number,
                kind=kind,
                occurred_at=occurred_at,
                source_id=source_id,
                actor=actor,
                actor_type=actor_type,
                payload=payload,
            )
        )

    events.sort(
        key=lambda event: (event.occurred_at, event.kind is not EventKind.OPENED)
    )
    return events


def _opened(pr: PullRequestSimple) -> Event:
    # GitHub emits no timeline item when a pull request opens, so there is no
    # id to key on. The synthesized one has to be derivable from the pull
    # request alone, or a second sync would insert a second copy.
    actor, actor_type = _actor(_user(pr.user))
    return Event(
        subject_type=SubjectType.PULL_REQUEST,
        subject_number=pr.number,
        kind=EventKind.OPENED,
        occurred_at=pr.created_at,
        source_id=f"pr:{pr.number}:opened",
        actor=actor,
        actor_type=actor_type,
        payload=None,
    )


def _named(user: object, team: object, node_id: str) -> ActorRef:
    """The user or team an event names, as opposed to the one who acted."""
    if isinstance(user, SimpleUser):
        return ActorRef(name=user.login, type=_actor_type(user.type))
    if isinstance(team, Team):
        # A team has no login. Its slug is what a config file would name.
        return ActorRef(name=team.slug, type=ActorType.TEAM)
    raise NormalizationError(f"{node_id} names neither a user nor a team")


def _user(value: object) -> SimpleUser | None:
    """A user, or None where GitHub sends null or leaves the field out."""
    if value is UNSET or value is None:
        return None
    if isinstance(value, SimpleUser):
        return value
    raise NormalizationError(f"expected a user, got {type(value).__name__}")


def _actor(holder: SimpleUser | Team | None) -> tuple[str | None, ActorType | None]:
    """A login, or a team's slug, and what kind of account it is.

    Both halves go null together, for an account GitHub has deleted. That is a
    fact about the history rather than a broken row.
    """
    if holder is None:
        return None, None
    if isinstance(holder, Team):
        return holder.slug, ActorType.TEAM
    return holder.login, _actor_type(holder.type)


def _actor_type(name: str) -> ActorType:
    try:
        return ActorType(name)
    except ValueError as err:
        # GitHub widening the set of account types. Better a failed sync than a
        # row whose actor_type the model cannot read back.
        raise NormalizationError(f"unknown actor type {name!r}") from err


def _when(value: object, what: str) -> datetime:
    """A timestamp, from either of the two shapes GitHub's schema uses.

    The issue-event models type `created_at` as a string and the timeline
    models as a datetime -- GitHub's OpenAPI spec disagreeing with itself,
    reproduced faithfully by the models generated from it.
    """
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        return datetime.fromisoformat(value)
    raise NormalizationError(f"{what} has no usable timestamp: {value!r}")
