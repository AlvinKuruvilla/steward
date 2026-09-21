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


class CommentCannotUpdateReason(str, Enum):
    ARCHIVED = "ARCHIVED"
    DENIED = "DENIED"
    INSUFFICIENT_ACCESS = "INSUFFICIENT_ACCESS"
    LOCKED = "LOCKED"
    LOGIN_REQUIRED = "LOGIN_REQUIRED"
    MAINTENANCE = "MAINTENANCE"
    VERIFIED_EMAIL_REQUIRED = "VERIFIED_EMAIL_REQUIRED"


class DiffSide(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class IssueStateReason(str, Enum):
    COMPLETED = "COMPLETED"
    DUPLICATE = "DUPLICATE"
    NOT_PLANNED = "NOT_PLANNED"
    REOPENED = "REOPENED"


class LockReason(str, Enum):
    OFF_TOPIC = "OFF_TOPIC"
    RESOLVED = "RESOLVED"
    SPAM = "SPAM"
    TOO_HEATED = "TOO_HEATED"


class PullRequestReviewState(str, Enum):
    APPROVED = "APPROVED"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    COMMENTED = "COMMENTED"
    DISMISSED = "DISMISSED"
    PENDING = "PENDING"


class PullRequestReviewThreadSubjectType(str, Enum):
    FILE = "FILE"
    LINE = "LINE"


class PullRequestState(str, Enum):
    CLOSED = "CLOSED"
    MERGED = "MERGED"
    OPEN = "OPEN"


class UserBlockDuration(str, Enum):
    ONE_DAY = "ONE_DAY"
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    PERMANENT = "PERMANENT"
    THREE_DAYS = "THREE_DAYS"
