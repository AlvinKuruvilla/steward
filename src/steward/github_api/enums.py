from enum import Enum


class CommentAuthorAssociation(str, Enum):
    COLLABORATOR = "COLLABORATOR"
    CONTRIBUTOR = "CONTRIBUTOR"
    FIRST_TIMER = "FIRST_TIMER"
    FIRST_TIME_CONTRIBUTOR = "FIRST_TIME_CONTRIBUTOR"
    MANNEQUIN = "MANNEQUIN"
    MEMBER = "MEMBER"
    NONE = "NONE"
    OWNER = "OWNER"


class IssueStateReason(str, Enum):
    COMPLETED = "COMPLETED"
    DUPLICATE = "DUPLICATE"
    NOT_PLANNED = "NOT_PLANNED"
    REOPENED = "REOPENED"


class PullRequestReviewState(str, Enum):
    APPROVED = "APPROVED"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    COMMENTED = "COMMENTED"
    DISMISSED = "DISMISSED"
    PENDING = "PENDING"


class PullRequestState(str, Enum):
    CLOSED = "CLOSED"
    MERGED = "MERGED"
    OPEN = "OPEN"
