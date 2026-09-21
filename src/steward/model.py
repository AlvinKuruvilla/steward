"""
Steward's data model
"""

from collections.abc import Mapping
from dataclasses import dataclass, fields
from datetime import datetime
from enum import Enum, StrEnum


class PullRequestReviewState(StrEnum):
    "The radio button a reviewer picked when they submitted a review"

    # Ref: https://docs.github.com/en/graphql/reference/pulls#enum-pullrequestreviewstate

    # NOTE: Values mirror GitHub's enum verbatim; they arrive over the wire.

    # A review still being drafted. You only ever see your own, so we never
    # ingest one.
    PENDING = "PENDING"
    # NOTE: Creates no obligation. GitHub records neither a request nor an
    # approval, so neither do we.
    COMMENTED = "COMMENTED"
    APPROVED = "APPROVED"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    # NOTE: Not trustworthy as a review's state. GitHub rewrites the review in
    # place on dismissal; the original is ReviewDismissedEvent.previousReviewState.
    DISMISSED = "DISMISSED"


class ActorType(StrEnum):
    "What kind of account acted, or was named by an event"

    # Ref: https://docs.github.com/en/graphql/reference/users#interface-actor

    # NOTE: Values mirror GraphQL __typename verbatim; they arrive over the wire.
    # Teams appear here because a review can be requested from one, and a Team
    # has no login -- see ActorRef.
    USER = "User"
    BOT = "Bot"
    ORGANIZATION = "Organization"
    MANNEQUIN = "Mannequin"
    TEAM = "Team"
    ENTERPRISE_TEAM = "EnterpriseTeam"
    ENTERPRISE_USER_ACCOUNT = "EnterpriseUserAccount"


class IssueStateReason(StrEnum):
    "Why an issue is in the state it is in"

    # Ref: https://docs.github.com/en/graphql/reference/issues#enum-issuestatereason

    # NOTE: Values mirror GitHub's enum verbatim; they arrive over the wire.
    # REOPENED is here because this is the issue's state reason, not a reason
    # for closing.
    COMPLETED = "COMPLETED"
    NOT_PLANNED = "NOT_PLANNED"
    DUPLICATE = "DUPLICATE"
    REOPENED = "REOPENED"


class SubjectType(StrEnum):
    "What an event happened to"

    # NOTE: These values are ours, not GitHub's, and must match the CHECK
    # constraint in db/migrations/0001_events.sql. A mismatch fails at INSERT,
    # not at type-check.
    PULL_REQUEST = "pull_request"
    ISSUE = "issue"


class EventKind(StrEnum):
    """Something that happened to a subject, as GitHub reported it.

    Facts only. No STALE, no NEEDS_ATTENTION -- those are conclusions, and a
    conclusion written into an append-only log can never be revised. The fold
    computes them at read time from these plus repo policy.
    """

    # Ref: https://docs.github.com/en/graphql/reference/pulls#union-pullrequesttimelineitems

    # GitHub emits no event when a PR opens; we derive it from createdAt. With
    # no node ID to key on, source_id is synthesized as "pr:<number>:opened".
    OPENED = "opened"

    # A PR opened as a draft emits neither, so the opening state is recovered
    # backwards from whichever of these fires first.
    READY_FOR_REVIEW = "ready_for_review"
    CONVERT_TO_DRAFT = "convert_to_draft"

    REOPENED = "reopened"
    # NOTE: Merging also closes, so both fire and can share a timestamp. A fold
    # that stops at the first terminal event must break the tie toward MERGED,
    # or it reports merges as closes.
    CLOSED = "closed"
    MERGED = "merged"

    # NOTE: committedDate is author-controlled and survives rebase, so a COMMIT
    # can predate the PR itself. FORCE_PUSHED is the only push time we can trust.
    COMMIT = "commit"
    FORCE_PUSHED = "force_pushed"

    REVIEW = "review"
    # The requested reviewer may be a team rather than a user.
    REVIEW_REQUESTED = "review_requested"
    REVIEW_REQUEST_REMOVED = "review_request_removed"
    # Carries previousReviewState, the only record of what a review was before
    # GitHub overwrote it.
    REVIEW_DISMISSED = "review_dismissed"

    ASSIGNED = "assigned"
    UNASSIGNED = "unassigned"
    # NOTE: Some repos keep merge state in bot-applied labels rather than in
    # review objects -- kubernetes uses lgtm, approved and do-not-merge/*.
    LABELED = "labeled"
    UNLABELED = "unlabeled"

    COMMENT = "comment"
    CROSS_REFERENCED = "cross_referenced"


@dataclass(frozen=True, slots=True)
class ActorRef:
    "A user, bot or team an event names"

    # Ref: https://docs.github.com/en/graphql/reference/pulls#union-requestedreviewer

    # NOTE: login for users and bots, slug for teams. Team exposes no login
    # field, so a field called login would be null for every team request.
    name: str
    type: ActorType


@dataclass(frozen=True, slots=True)
class ReviewPayload:
    "The state a reviewer submitted"

    # Ref: https://docs.github.com/en/graphql/reference/pulls#object-pullrequestreview

    state: PullRequestReviewState


@dataclass(frozen=True, slots=True)
class DismissalPayload:
    "What a review held before it was dismissed"

    # Ref: https://docs.github.com/en/graphql/reference/pulls#object-reviewdismissedevent

    # NOTE: Nothing else survives the dismissal; GitHub overwrites the review's
    # own state in place.
    previous_state: PullRequestReviewState
    review_id: str


@dataclass(frozen=True, slots=True)
class LabelPayload:
    "The label added or removed"

    # Ref: https://docs.github.com/en/graphql/reference/issues#object-label

    name: str


@dataclass(frozen=True, slots=True)
class CommitPayload:
    "The commit that landed on the branch"

    # Ref: https://docs.github.com/en/graphql/reference/commits#object-commit

    oid: str


@dataclass(frozen=True, slots=True)
class CrossReferencePayload:
    "Another subject that referenced this one"

    # Ref: https://docs.github.com/en/graphql/reference/issues#object-crossreferencedevent

    source_type: SubjectType
    source_number: int
    # GitHub's own read of whether merging the source would close this subject.
    will_close: bool


@dataclass(frozen=True, slots=True)
class StateReasonPayload:
    "Why an issue changed state"

    # Ref: https://docs.github.com/en/graphql/reference/issues#object-closedevent

    reason: IssueStateReason


# NOTE: None is the payload for kinds that carry nothing beyond an actor and a
# timestamp. Matching on this union is what makes mypy reject a fold that
# forgets a shape, so widen it only alongside the folds that consume it.
Payload = (
    ActorRef
    | ReviewPayload
    | DismissalPayload
    | LabelPayload
    | CommitPayload
    | CrossReferencePayload
    | StateReasonPayload
    | None
)

PayloadType = (
    type[ActorRef]
    | type[ReviewPayload]
    | type[DismissalPayload]
    | type[LabelPayload]
    | type[CommitPayload]
    | type[CrossReferencePayload]
    | type[StateReasonPayload]
)

PAYLOAD_FOR: dict[EventKind, PayloadType | None] = {
    EventKind.OPENED: None,
    EventKind.READY_FOR_REVIEW: None,
    EventKind.CONVERT_TO_DRAFT: None,
    EventKind.REOPENED: None,
    # NOTE: Pull requests carry no reason, so their CLOSED payload is None. The
    # mapping gives the shape a kind may carry, not one it always carries.
    EventKind.CLOSED: StateReasonPayload,
    EventKind.MERGED: None,
    EventKind.COMMIT: CommitPayload,
    EventKind.FORCE_PUSHED: None,
    EventKind.REVIEW: ReviewPayload,
    EventKind.REVIEW_REQUESTED: ActorRef,
    EventKind.REVIEW_REQUEST_REMOVED: ActorRef,
    EventKind.REVIEW_DISMISSED: DismissalPayload,
    EventKind.ASSIGNED: ActorRef,
    EventKind.UNASSIGNED: ActorRef,
    EventKind.LABELED: LabelPayload,
    EventKind.UNLABELED: LabelPayload,
    EventKind.COMMENT: None,
    EventKind.CROSS_REFERENCED: CrossReferencePayload,
}


# The log stores normalized events and nothing else, so a timeline item with no
# kind here is discarded at sync time and is only recoverable by re-syncing the
# repository. `scripts/gen_timeline_query.py` reads this to build the query's
# itemTypes filter, which is what keeps the query from asking for items the
# model would throw away.
#
# EventKind.OPENED is absent on purpose: GitHub emits no timeline item when a
# pull request opens, and it is derived from createdAt instead.
KIND_FOR_TYPENAME: dict[str, EventKind] = {
    "ReadyForReviewEvent": EventKind.READY_FOR_REVIEW,
    "ConvertToDraftEvent": EventKind.CONVERT_TO_DRAFT,
    "ReopenedEvent": EventKind.REOPENED,
    "ClosedEvent": EventKind.CLOSED,
    "MergedEvent": EventKind.MERGED,
    "PullRequestCommit": EventKind.COMMIT,
    "HeadRefForcePushedEvent": EventKind.FORCE_PUSHED,
    "PullRequestReview": EventKind.REVIEW,
    "ReviewRequestedEvent": EventKind.REVIEW_REQUESTED,
    "ReviewRequestRemovedEvent": EventKind.REVIEW_REQUEST_REMOVED,
    "ReviewDismissedEvent": EventKind.REVIEW_DISMISSED,
    "AssignedEvent": EventKind.ASSIGNED,
    "UnassignedEvent": EventKind.UNASSIGNED,
    "LabeledEvent": EventKind.LABELED,
    "UnlabeledEvent": EventKind.UNLABELED,
    "IssueComment": EventKind.COMMENT,
    "CrossReferencedEvent": EventKind.CROSS_REFERENCED,
}


@dataclass(frozen=True, slots=True)
class Event:
    "One row of the event log"

    # No repo_id: a sync runs against one repository, and the writer holds it.
    subject_type: SubjectType
    subject_number: int
    kind: EventKind
    occurred_at: datetime
    # GitHub's node ID, or a synthesized key for the kinds GitHub emits no object
    # for. Unique per repository, which is what makes a re-sync idempotent.
    source_id: str
    # Both None for a deleted account: GitHub returns a null author rather than
    # dropping the event.
    actor: str | None
    actor_type: ActorType | None
    payload: Payload


def validate_payload(kind: EventKind, payload: Payload) -> None:
    """Check a payload against the shape its kind declares in `PAYLOAD_FOR`.

    The normalizer calls this before constructing an `Event`. The decoder that
    reads rows back does not: those rows were checked on the way in, and the log
    is append-only.

    Raises `ValueError` if the payload is of the wrong shape.
    """
    expected = PAYLOAD_FOR[kind]
    if expected is None:
        if payload is not None:
            raise ValueError(
                f"{kind.name} carries no payload, got {type(payload).__name__}"
            )
        return
    # A kind declares the shape it may carry, not one it always carries: a pull
    # request closes with no reason. A payload the normalizer dropped therefore
    # reads the same as one that was never there, and this will not catch it.
    if payload is None:
        return
    if not isinstance(payload, expected):
        raise ValueError(
            f"{kind.name} carries {expected.__name__}, got {type(payload).__name__}"
        )


# The JSONB round trip.
#
# Payload shapes are flat and hold only str, int, bool and StrEnum fields, so
# both directions are plain field access. Encoding is uniform enough to do by
# reflection; decoding is written out per shape instead, so that mypy checks
# every construction against the dataclass it is rebuilding. The cost is that
# field names appear here as well as on the dataclass, and only
# `test_payload_round_trips` catches a rename that misses one.

type JsonValue = str | int | bool


def payload_to_dict(payload: Payload) -> dict[str, JsonValue]:
    """Render a payload as the JSONB that `events.payload` holds.

    A kind carrying no payload stores `{}`, matching the column default.
    """
    if payload is None:
        return {}
    return {f.name: _scalar(getattr(payload, f.name)) for f in fields(payload)}


def payload_from_dict(kind: EventKind, data: Mapping[str, JsonValue]) -> Payload:
    """Rebuild the payload a row holds, using `kind` to choose the shape.

    Raises `ValueError` if a field is missing, holds the wrong type, or holds a
    value outside the enum it is read into.
    """
    shape = PAYLOAD_FOR[kind]
    # An empty payload is how a kind that carries nothing is stored, and also
    # how a kind that carries something optional stores its absence.
    if shape is None or not data:
        return None
    if shape is ActorRef:
        return ActorRef(
            name=_str(data, "name"),
            type=ActorType(_str(data, "type")),
        )
    if shape is ReviewPayload:
        return ReviewPayload(state=PullRequestReviewState(_str(data, "state")))
    if shape is DismissalPayload:
        return DismissalPayload(
            previous_state=PullRequestReviewState(_str(data, "previous_state")),
            review_id=_str(data, "review_id"),
        )
    if shape is LabelPayload:
        return LabelPayload(name=_str(data, "name"))
    if shape is CommitPayload:
        return CommitPayload(oid=_str(data, "oid"))
    if shape is CrossReferencePayload:
        return CrossReferencePayload(
            source_type=SubjectType(_str(data, "source_type")),
            source_number=_int(data, "source_number"),
            will_close=_bool(data, "will_close"),
        )
    if shape is StateReasonPayload:
        return StateReasonPayload(reason=IssueStateReason(_str(data, "reason")))
    raise ValueError(f"{kind.name} declares {shape.__name__}, which has no decoder")


def _scalar(value: object) -> JsonValue:
    if isinstance(value, Enum):
        # A StrEnum member is a str, so it would serialize without this. An
        # IntEnum or a plain Enum would not, and nothing stops one being added.
        return str(value.value)
    if isinstance(value, str | int | bool):
        return value
    raise TypeError(f"payload fields must be scalar, got {type(value).__name__}")


def _field(data: Mapping[str, JsonValue], name: str) -> JsonValue:
    try:
        return data[name]
    except KeyError:
        raise ValueError(f"payload needs {name}; row has {sorted(data)}") from None


def _str(data: Mapping[str, JsonValue], name: str) -> str:
    value = _field(data, name)
    if not isinstance(value, str):
        raise ValueError(f"payload field {name} must be a string, got {value!r}")
    return value


def _int(data: Mapping[str, JsonValue], name: str) -> int:
    value = _field(data, name)
    # bool is an int in Python, and `will_close` sitting next to `source_number`
    # makes a JSON `true` reaching an int field a live mistake.
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"payload field {name} must be an integer, got {value!r}")
    return value


def _bool(data: Mapping[str, JsonValue], name: str) -> bool:
    value = _field(data, name)
    if not isinstance(value, bool):
        raise ValueError(f"payload field {name} must be a boolean, got {value!r}")
    return value
