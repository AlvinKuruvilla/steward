from typing import Any, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CommentAuthorAssociation, PullRequestState


class PullRequestSnapshot(BaseModel):
    id: str
    number: int
    title: str
    state: PullRequestState
    is_draft: bool = Field(alias="isDraft")
    created_at: Any = Field(alias="createdAt")
    closed_at: Optional[Any] = Field(alias="closedAt")
    merged_at: Optional[Any] = Field(alias="mergedAt")
    additions: int
    deletions: int
    changed_files: int = Field(alias="changedFiles")
    base_ref_name: str = Field(alias="baseRefName")
    head_ref_name: str = Field(alias="headRefName")
    author_association: CommentAuthorAssociation = Field(alias="authorAssociation")
    author: Optional["PullRequestSnapshotAuthor"]
    labels: Optional["PullRequestSnapshotLabels"]


class PullRequestSnapshotAuthor(BaseModel):
    typename__: Literal[
        "Actor", "Bot", "EnterpriseUserAccount", "Mannequin", "Organization", "User"
    ] = Field(alias="__typename")
    login: str


class PullRequestSnapshotLabels(BaseModel):
    nodes: Optional[list[Optional["PullRequestSnapshotLabelsNodes"]]]


class PullRequestSnapshotLabelsNodes(BaseModel):
    name: str


PullRequestSnapshot.model_rebuild()
