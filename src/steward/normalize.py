"""GitHub's timeline, as Steward's events.

The log stores normalized events and nothing else, so this is the one place a
mistake becomes permanent: an event mapped wrong is written wrong, and fixing it
means re-syncing the repository, which re-reads GitHub as it is now rather than
as it was. Every event goes through `validate_payload` before it is constructed,
and anything this module cannot account for raises rather than being skipped.

Dispatch is a chain on `node.typename__`, the discriminator ariadne-codegen puts
on each generated model. Two things about its shape are forced rather than
chosen. The union of timeline types is spelled out inline in the generated model
with no alias to import, and each class name runs to eighty-five characters, so
a helper taking one node cannot be annotated without seventeen imports that no
line-length limit survives -- the chain therefore lives inside the loop, where
the union is already in scope. And each branch tests `node.typename__` directly
rather than through a local, because mypy narrows the union on the attribute
expression; bind it to a name first and every branch sees all seventeen types.
"""

from __future__ import annotations

from datetime import datetime

from steward.github_api.pull_request_page import (
    PullRequestPageRepositoryPullRequestsNodes as PullRequestNode,
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


class NormalizationError(Exception):
    """A timeline item that cannot be stored without losing or inventing a fact."""


def events_for_pull_request(pr: PullRequestNode) -> list[Event]:
    """Every event this page of a pull request's timeline carries, oldest first.

    OPENED is not necessarily first. A commit's committedDate is
    author-controlled and survives a rebase, so it routinely predates the pull
    request it lands on -- 106 of 125 pull requests across the five corpus
    repositories on 2026-09-21, worst case 21 days early.

    The audit prototype clamped those times forward to the pull request's
    createdAt. This does not: the log records what GitHub reported, and a
    clamped timestamp is a conclusion about which events should count as
    "during" the pull request. The fold makes that call at read time, where it
    can be changed without a re-sync. Ties break toward OPENED so that a commit
    sharing the pull request's exact timestamp does not sort ahead of it.
    """
    events = [_opened(pr)]

    for node in pr.timeline_items.nodes or []:
        if node is None:
            continue

        kind: EventKind
        occurred_at: datetime
        acted_by: object = None
        payload: Payload = None

        if node.typename__ == "ReadyForReviewEvent":
            kind, occurred_at, acted_by = (
                EventKind.READY_FOR_REVIEW,
                node.created_at,
                node.actor,
            )
        elif node.typename__ == "ConvertToDraftEvent":
            kind, occurred_at, acted_by = (
                EventKind.CONVERT_TO_DRAFT,
                node.created_at,
                node.actor,
            )
        elif node.typename__ == "ReopenedEvent":
            kind, occurred_at, acted_by = (
                EventKind.REOPENED,
                node.created_at,
                node.actor,
            )
        elif node.typename__ == "MergedEvent":
            kind, occurred_at, acted_by = EventKind.MERGED, node.created_at, node.actor
        elif node.typename__ == "HeadRefForcePushedEvent":
            kind, occurred_at, acted_by = (
                EventKind.FORCE_PUSHED,
                node.created_at,
                node.actor,
            )
        elif node.typename__ == "IssueComment":
            kind, occurred_at, acted_by = (
                EventKind.COMMENT,
                node.created_at,
                node.author,
            )

        elif node.typename__ == "ClosedEvent":
            kind, occurred_at, acted_by = EventKind.CLOSED, node.created_at, node.actor
            # Only issues close with a reason; a pull request carries none.
            if node.state_reason is not None:
                payload = StateReasonPayload(IssueStateReason(node.state_reason.value))

        elif node.typename__ == "PullRequestCommit":
            commit = node.pull_request_commit_commit
            # PullRequestCommit has no createdAt of its own, so the commit's
            # own date is the only time it carries. Nobody acted: the commit's
            # author is not the person who put it on this branch.
            kind, occurred_at = EventKind.COMMIT, commit.committed_date
            payload = CommitPayload(oid=commit.oid)

        elif node.typename__ == "PullRequestReview":
            # A PENDING review has never been submitted and has no submittedAt.
            # You can only see your own, so we never ingest one; reaching this
            # means the query changed, not that GitHub did.
            if node.submitted_at is None:
                raise NormalizationError(
                    f"review {node.id} has no submittedAt, state {node.state.value}"
                )
            kind, occurred_at, acted_by = (
                EventKind.REVIEW,
                node.submitted_at,
                node.author,
            )
            payload = ReviewPayload(PullRequestReviewState(node.state.value))

        elif node.typename__ == "ReviewRequestedEvent":
            kind, occurred_at, acted_by = (
                EventKind.REVIEW_REQUESTED,
                node.created_at,
                node.actor,
            )
            payload = _named(node.requested_reviewer, node.id, "requestedReviewer")
        elif node.typename__ == "ReviewRequestRemovedEvent":
            kind, occurred_at, acted_by = (
                EventKind.REVIEW_REQUEST_REMOVED,
                node.created_at,
                node.actor,
            )
            payload = _named(node.requested_reviewer, node.id, "requestedReviewer")
        elif node.typename__ == "AssignedEvent":
            kind, occurred_at, acted_by = (
                EventKind.ASSIGNED,
                node.created_at,
                node.actor,
            )
            payload = _named(node.assignee, node.id, "assignee")
        elif node.typename__ == "UnassignedEvent":
            kind, occurred_at, acted_by = (
                EventKind.UNASSIGNED,
                node.created_at,
                node.actor,
            )
            payload = _named(node.assignee, node.id, "assignee")

        elif node.typename__ == "ReviewDismissedEvent":
            # previousReviewState is the only record of what the review held:
            # GitHub overwrites the review's own state in place on dismissal.
            if node.review is None:
                raise NormalizationError(
                    f"dismissal {node.id} names no review, so what it held is lost"
                )
            kind, occurred_at, acted_by = (
                EventKind.REVIEW_DISMISSED,
                node.created_at,
                node.actor,
            )
            payload = DismissalPayload(
                previous_state=PullRequestReviewState(node.previous_review_state.value),
                review_id=node.review.id,
            )

        elif node.typename__ == "LabeledEvent":
            kind, occurred_at, acted_by = EventKind.LABELED, node.created_at, node.actor
            payload = LabelPayload(name=node.label.name)
        elif node.typename__ == "UnlabeledEvent":
            kind, occurred_at, acted_by = (
                EventKind.UNLABELED,
                node.created_at,
                node.actor,
            )
            payload = LabelPayload(name=node.label.name)

        elif node.typename__ == "CrossReferencedEvent":
            source = node.source
            if source.typename__ == "Issue":
                source_type = SubjectType.ISSUE
            elif source.typename__ == "PullRequest":
                source_type = SubjectType.PULL_REQUEST
            else:
                raise NormalizationError(
                    f"cross-reference {node.id} comes from {source.typename__}"
                )
            # referencedAt is when the reference was made, createdAt when GitHub
            # recorded it. They differ when a commit is pushed and linked later.
            kind, occurred_at, acted_by = (
                EventKind.CROSS_REFERENCED,
                node.referenced_at,
                node.actor,
            )
            payload = CrossReferencePayload(
                source_type=source_type,
                source_number=source.number,
                will_close=node.will_close_target,
            )

        else:
            # itemTypes asks for exactly the types KIND_FOR_TYPENAME lists, so
            # this is the query and the model having come apart.
            raise NormalizationError(f"unexpected timeline item {node.typename__}")

        validate_payload(kind, payload)
        actor, actor_type = _actor(acted_by)
        events.append(
            Event(
                subject_type=SubjectType.PULL_REQUEST,
                subject_number=pr.number,
                kind=kind,
                occurred_at=occurred_at,
                source_id=node.id,
                actor=actor,
                actor_type=actor_type,
                payload=payload,
            )
        )

    events.sort(
        key=lambda event: (event.occurred_at, event.kind is not EventKind.OPENED)
    )
    return events


def _opened(pr: PullRequestNode) -> Event:
    # GitHub emits no timeline item when a pull request opens, so there is no
    # node id to key on. The synthesized one has to be derivable from the pull
    # request alone, or a second sync would insert a second copy.
    actor, actor_type = _actor(pr.author)
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


def _named(holder: object, node_id: str, field: str) -> ActorRef | None:
    """The user, bot or team an event names, as opposed to the one who acted.

    None where GitHub declines to say. A review requested from a team the token
    cannot see comes back null -- 9 of ruff's 32 requests on one page, and the
    same null appears on the live `reviewRequests` connection, so it is a
    permission boundary rather than anything about the timeline.

    The event is still stored. That a review was requested is what opens a
    waiting interval, and dropping the event to avoid an unnamed reviewer would
    lose the transition as well as the name. `PAYLOAD_FOR` allows this: it gives
    the shape a kind may carry, not one it always carries.
    """
    if holder is None:
        return None
    name, actor_type = _actor(holder)
    if name is None or actor_type is None:
        raise NormalizationError(f"{node_id}.{field} has no name to key on")
    return ActorRef(name=name, type=actor_type)


def _actor(holder: object) -> tuple[str | None, ActorType | None]:
    """A login, or a team's slug, and what kind of account it is.

    Both halves go null together, for an account GitHub has deleted. That is a
    fact about the history rather than a broken row.
    """
    if holder is None:
        return None, None
    typename = getattr(holder, "typename__", None)
    if not isinstance(typename, str):
        raise NormalizationError(f"{type(holder).__name__} carries no __typename")
    try:
        actor_type = ActorType(typename)
    except ValueError as err:
        # A __typename outside ActorType means GitHub widened the schema. The
        # pinned copy is how that is supposed to arrive -- as a diff someone
        # reads -- so a sync meeting one has drifted from what it was built on.
        raise NormalizationError(f"unknown actor type {typename!r}") from err
    # A Team exposes no login, so the query selects its slug instead.
    name = getattr(holder, "login", None) or getattr(holder, "slug", None)
    return (name if isinstance(name, str) else None), actor_type
