from datetime import datetime
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import CommentAuthorAssociation, IssueStateReason, PullRequestReviewState
from .fragments import (  # noqa: F401
    PullRequestSnapshot,
    PullRequestSnapshotAuthor,
    PullRequestSnapshotLabels,
)


class PullRequestPage(BaseModel):
    repository: Optional["PullRequestPageRepository"]


class PullRequestPageRepository(BaseModel):
    pull_requests: "PullRequestPageRepositoryPullRequests" = Field(alias="pullRequests")


class PullRequestPageRepositoryPullRequests(BaseModel):
    page_info: "PullRequestPageRepositoryPullRequestsPageInfo" = Field(alias="pageInfo")
    nodes: Optional[list[Optional["PullRequestPageRepositoryPullRequestsNodes"]]]


class PullRequestPageRepositoryPullRequestsPageInfo(BaseModel):
    has_next_page: bool = Field(alias="hasNextPage")
    end_cursor: Optional[str] = Field(alias="endCursor")


class PullRequestPageRepositoryPullRequestsNodes(PullRequestSnapshot):
    timeline_items: "PullRequestPageRepositoryPullRequestsNodesTimelineItems" = Field(
        alias="timelineItems"
    )


class PullRequestPageRepositoryPullRequestsNodesTimelineItems(BaseModel):
    total_count: int = Field(alias="totalCount")
    page_info: "PullRequestPageRepositoryPullRequestsNodesTimelineItemsPageInfo" = (
        Field(alias="pageInfo")
    )
    nodes: Optional[
        list[
            Optional[
                Annotated[
                    Union[
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2Event",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueComment",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommit",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitCommentThread",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReview",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewThread",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestRevisionMarker",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2Event",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEvent",
                        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEvent",
                    ],
                    Field(discriminator="typename__"),
                ]
            ]
        ]
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsPageInfo(BaseModel):
    has_next_page: bool = Field(alias="hasNextPage")
    end_cursor: Optional[str] = Field(alias="endCursor")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEvent(
    BaseModel
):
    typename__: Literal["AddedToMergeQueueEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEvent(
    BaseModel
):
    typename__: Literal["AddedToProjectEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2Event(
    BaseModel
):
    typename__: Literal["AddedToProjectV2Event"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEvent(
    BaseModel
):
    typename__: Literal["AssignedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    assignee: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEvent(
    BaseModel
):
    typename__: Literal["AutoMergeDisabledEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoMergeEnabledEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoRebaseEnabledEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoSquashEnabledEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeFailedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeSucceededEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEvent(
    BaseModel
):
    typename__: Literal["BaseRefChangedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEvent(
    BaseModel
):
    typename__: Literal["BaseRefDeletedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEvent(
    BaseModel
):
    typename__: Literal["BaseRefForcePushedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEvent(
    BaseModel
):
    typename__: Literal["BlockedByAddedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockedByRemovedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEvent(
    BaseModel
):
    typename__: Literal["BlockingAddedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockingRemovedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEvent(
    BaseModel
):
    typename__: Literal["ClosedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    closer: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserCommit",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserProjectV2",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    duplicate_of: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventDuplicateOfIssue",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventDuplicateOfPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="duplicateOf")
    id: str
    state_reason: Optional[IssueStateReason] = Field(alias="stateReason")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserCommit(
    BaseModel
):
    typename__: Literal["Commit"] = Field(alias="__typename")
    id: str
    oid: str
    abbreviated_oid: str = Field(alias="abbreviatedOid")
    authored_date: datetime = Field(alias="authoredDate")
    committed_date: datetime = Field(alias="committedDate")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserProjectV2(
    BaseModel
):
    typename__: Literal["ProjectV2"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    merged_at: Optional[datetime] = Field(alias="mergedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventDuplicateOfIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventDuplicateOfPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    merged_at: Optional[datetime] = Field(alias="mergedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEvent(
    BaseModel
):
    typename__: Literal["CommentDeletedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEvent(
    BaseModel
):
    typename__: Literal["ConnectedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEvent(
    BaseModel
):
    typename__: Literal["ConvertToDraftEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEvent(
    BaseModel
):
    typename__: Literal["ConvertedFromDraftEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEvent(
    BaseModel
):
    typename__: Literal["ConvertedNoteToIssueEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEvent(
    BaseModel
):
    typename__: Literal["ConvertedToDiscussionEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEvent(
    BaseModel
):
    typename__: Literal["CrossReferencedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    referenced_at: datetime = Field(alias="referencedAt")
    source: Union[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventSourceIssue",
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventSourcePullRequest",
    ] = Field(discriminator="typename__")
    target: Union[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventTargetIssue",
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventTargetPullRequest",
    ] = Field(discriminator="typename__")
    will_close_target: bool = Field(alias="willCloseTarget")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    merged_at: Optional[datetime] = Field(alias="mergedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventTargetIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventTargetPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    id: str
    number: int
    closed_at: Optional[datetime] = Field(alias="closedAt")
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    merged_at: Optional[datetime] = Field(alias="mergedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEvent(
    BaseModel
):
    typename__: Literal["DemilestonedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEvent(
    BaseModel
):
    typename__: Literal["DeployedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEvent(
    BaseModel
):
    typename__: Literal["DeploymentEnvironmentChangedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEvent(
    BaseModel
):
    typename__: Literal["DisconnectedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEvent(
    BaseModel
):
    typename__: Literal["HeadRefDeletedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEvent(
    BaseModel
):
    typename__: Literal["HeadRefForcePushedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    after_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventAfterCommit"
    ] = Field(alias="afterCommit")
    before_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventBeforeCommit"
    ] = Field(alias="beforeCommit")
    created_at: datetime = Field(alias="createdAt")
    id: str
    ref: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventRef"
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventAfterCommit(
    BaseModel
):
    id: str
    oid: str
    abbreviated_oid: str = Field(alias="abbreviatedOid")
    authored_date: datetime = Field(alias="authoredDate")
    committed_date: datetime = Field(alias="committedDate")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventBeforeCommit(
    BaseModel
):
    id: str
    oid: str
    abbreviated_oid: str = Field(alias="abbreviatedOid")
    authored_date: datetime = Field(alias="authoredDate")
    committed_date: datetime = Field(alias="committedDate")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventRef(
    BaseModel
):
    id: str
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEvent(
    BaseModel
):
    typename__: Literal["HeadRefRestoredEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueComment(
    BaseModel
):
    typename__: Literal["IssueComment"] = Field(alias="__typename")
    author: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    author_association: CommentAuthorAssociation = Field(alias="authorAssociation")
    created_at: datetime = Field(alias="createdAt")
    created_via_email: bool = Field(alias="createdViaEmail")
    editor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    full_database_id: Optional[Any] = Field(alias="fullDatabaseId")
    id: str
    includes_created_edit: bool = Field(alias="includesCreatedEdit")
    is_minimized: bool = Field(alias="isMinimized")
    is_pinned: Optional[bool] = Field(alias="isPinned")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    minimized_reason: Optional[str] = Field(alias="minimizedReason")
    pinned_at: Optional[datetime] = Field(alias="pinnedAt")
    pinned_by: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedBy"
    ] = Field(alias="pinnedBy")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    reaction_groups: Optional[
        list[
            "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentReactionGroups"
        ]
    ] = Field(alias="reactionGroups")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedBy(
    BaseModel
):
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentReactionGroups(
    BaseModel
):
    created_at: Optional[datetime] = Field(alias="createdAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEvent(
    BaseModel
):
    typename__: Literal["IssueCommentPinnedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEvent(
    BaseModel
):
    typename__: Literal["IssueCommentUnpinnedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldAddedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldChangedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldRemovedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeAddedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeChangedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeRemovedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEvent(
    BaseModel
):
    typename__: Literal["LabeledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str
    label: (
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventLabel"
    )


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventLabel(
    BaseModel
):
    id: str
    name: str
    created_at: Optional[datetime] = Field(alias="createdAt")
    updated_at: Optional[datetime] = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEvent(
    BaseModel
):
    typename__: Literal["LockedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["MarkedAsDuplicateEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEvent(
    BaseModel
):
    typename__: Literal["MentionedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEvent(
    BaseModel
):
    typename__: Literal["MergedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    merged_event_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventMergedEventCommit"
    ] = Field(alias="mergedEvent_commit")
    created_at: datetime = Field(alias="createdAt")
    id: str
    merge_ref: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventMergeRef"
    ] = Field(alias="mergeRef")
    merge_ref_name: str = Field(alias="mergeRefName")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventMergedEventCommit(
    BaseModel
):
    id: str
    oid: str
    abbreviated_oid: str = Field(alias="abbreviatedOid")
    authored_date: datetime = Field(alias="authoredDate")
    committed_date: datetime = Field(alias="committedDate")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventMergeRef(
    BaseModel
):
    id: str
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEvent(
    BaseModel
):
    typename__: Literal["MilestonedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEvent(
    BaseModel
):
    typename__: Literal["MovedColumnsInProjectEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueAddedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueRemovedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEvent(
    BaseModel
):
    typename__: Literal["PinnedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEvent(
    BaseModel
):
    typename__: Literal["ProjectV2ItemStatusChangedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommit(
    BaseModel
):
    typename__: Literal["PullRequestCommit"] = Field(alias="__typename")
    pull_request_commit_commit: "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitPullRequestCommitCommit" = Field(
        alias="pullRequestCommit_commit"
    )
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitPullRequestCommitCommit(
    BaseModel
):
    id: str
    oid: str
    abbreviated_oid: str = Field(alias="abbreviatedOid")
    authored_date: datetime = Field(alias="authoredDate")
    committed_date: datetime = Field(alias="committedDate")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitCommentThread(
    BaseModel
):
    typename__: Literal["PullRequestCommitCommentThread"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReview(
    BaseModel
):
    typename__: Literal["PullRequestReview"] = Field(alias="__typename")
    author: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    author_association: CommentAuthorAssociation = Field(alias="authorAssociation")
    author_can_push_to_repository: bool = Field(alias="authorCanPushToRepository")
    pull_request_review_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewPullRequestReviewCommit"
    ] = Field(alias="pullRequestReview_commit")
    created_at: datetime = Field(alias="createdAt")
    created_via_email: bool = Field(alias="createdViaEmail")
    editor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    full_database_id: Optional[Any] = Field(alias="fullDatabaseId")
    id: str
    includes_created_edit: bool = Field(alias="includesCreatedEdit")
    is_minimized: bool = Field(alias="isMinimized")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    minimized_reason: Optional[str] = Field(alias="minimizedReason")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    reaction_groups: Optional[
        list[
            "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewReactionGroups"
        ]
    ] = Field(alias="reactionGroups")
    state: PullRequestReviewState
    submitted_at: Optional[datetime] = Field(alias="submittedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewPullRequestReviewCommit(
    BaseModel
):
    id: str
    oid: str
    abbreviated_oid: str = Field(alias="abbreviatedOid")
    authored_date: datetime = Field(alias="authoredDate")
    committed_date: datetime = Field(alias="committedDate")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewReactionGroups(
    BaseModel
):
    created_at: Optional[datetime] = Field(alias="createdAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewThread(
    BaseModel
):
    typename__: Literal["PullRequestReviewThread"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestRevisionMarker(
    BaseModel
):
    typename__: Literal["PullRequestRevisionMarker"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEvent(
    BaseModel
):
    typename__: Literal["ReadyForReviewEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEvent(
    BaseModel
):
    typename__: Literal["ReferencedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEvent(
    BaseModel
):
    typename__: Literal["RemovedFromMergeQueueEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEvent(
    BaseModel
):
    typename__: Literal["RemovedFromProjectEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2Event(
    BaseModel
):
    typename__: Literal["RemovedFromProjectV2Event"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEvent(
    BaseModel
):
    typename__: Literal["RenamedTitleEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEvent(
    BaseModel
):
    typename__: Literal["ReopenedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str
    state_reason: Optional[IssueStateReason] = Field(alias="stateReason")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEvent(
    BaseModel
):
    typename__: Literal["ReviewDismissedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    dismissal_message: Optional[str] = Field(alias="dismissalMessage")
    id: str
    previous_review_state: PullRequestReviewState = Field(alias="previousReviewState")
    pull_request_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventPullRequestCommit"
    ] = Field(alias="pullRequestCommit")
    review: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventReview"
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventPullRequestCommit(
    BaseModel
):
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventReview(
    BaseModel
):
    id: str
    created_at: datetime = Field(alias="createdAt")
    last_edited_at: Optional[datetime] = Field(alias="lastEditedAt")
    published_at: Optional[datetime] = Field(alias="publishedAt")
    submitted_at: Optional[datetime] = Field(alias="submittedAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEvent(
    BaseModel
):
    typename__: Literal["ReviewRequestRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str
    requested_reviewer: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerEnterpriseTeam",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerTeam",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerUser",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="requestedReviewer")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerEnterpriseTeam(
    BaseModel
):
    typename__: Literal["EnterpriseTeam"] = Field(alias="__typename")
    id: str
    slug: str
    enterprise_team_name: str = Field(alias="enterpriseTeam_name")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    mannequin_name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerTeam(
    BaseModel
):
    typename__: Literal["Team"] = Field(alias="__typename")
    id: str
    slug: str
    team_name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    user_name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEvent(
    BaseModel
):
    typename__: Literal["ReviewRequestedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str
    requested_reviewer: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerEnterpriseTeam",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerTeam",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerUser",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="requestedReviewer")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerEnterpriseTeam(
    BaseModel
):
    typename__: Literal["EnterpriseTeam"] = Field(alias="__typename")
    id: str
    slug: str
    enterprise_team_name: str = Field(alias="enterpriseTeam_name")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    mannequin_name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerTeam(
    BaseModel
):
    typename__: Literal["Team"] = Field(alias="__typename")
    id: str
    slug: str
    team_name: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    user_name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEvent(
    BaseModel
):
    typename__: Literal["SubIssueAddedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["SubIssueRemovedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEvent(
    BaseModel
):
    typename__: Literal["SubscribedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEvent(
    BaseModel
):
    typename__: Literal["TransferredEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEvent(
    BaseModel
):
    typename__: Literal["UnassignedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    assignee: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEvent(
    BaseModel
):
    typename__: Literal["UnlabeledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: datetime = Field(alias="createdAt")
    id: str
    label: "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventLabel"


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    id: str
    login: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    archived_at: Optional[datetime] = Field(alias="archivedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    id: str
    login: str
    name: Optional[str]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventLabel(
    BaseModel
):
    id: str
    name: str
    created_at: Optional[datetime] = Field(alias="createdAt")
    updated_at: Optional[datetime] = Field(alias="updatedAt")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEvent(
    BaseModel
):
    typename__: Literal["UnlockedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["UnmarkedAsDuplicateEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEvent(
    BaseModel
):
    typename__: Literal["UnpinnedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEvent(
    BaseModel
):
    typename__: Literal["UnsubscribedEvent"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEvent(
    BaseModel
):
    typename__: Literal["UserBlockedEvent"] = Field(alias="__typename")


PullRequestPage.model_rebuild()
PullRequestPageRepository.model_rebuild()
PullRequestPageRepositoryPullRequests.model_rebuild()
PullRequestPageRepositoryPullRequestsNodes.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItems.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueComment.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommit.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReview.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEvent.model_rebuild()
