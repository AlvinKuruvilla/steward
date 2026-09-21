from typing import Annotated, Any, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    IssueStateReason,
    PullRequestReviewState,
)
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
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEventAssigneeUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserCommit(
    BaseModel
):
    typename__: Literal["Commit"] = Field(alias="__typename")
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserProjectV2(
    BaseModel
):
    typename__: Literal["ProjectV2"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventCloserPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventDuplicateOfIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEventDuplicateOfPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


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
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    referenced_at: Any = Field(alias="referencedAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventTargetIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEventTargetPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventAfterCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventBeforeCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEventRef(
    BaseModel
):
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
    created_at: Any = Field(alias="createdAt")
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
    last_edited_at: Optional[Any] = Field(alias="lastEditedAt")
    minimized_reason: Optional[str] = Field(alias="minimizedReason")
    pinned_at: Optional[Any] = Field(alias="pinnedAt")
    pinned_by: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedBy"
    ] = Field(alias="pinnedBy")
    published_at: Optional[Any] = Field(alias="publishedAt")
    updated_at: Any = Field(alias="updatedAt")
    viewer_can_delete: bool = Field(alias="viewerCanDelete")
    viewer_can_minimize: bool = Field(alias="viewerCanMinimize")
    viewer_can_pin: bool = Field(alias="viewerCanPin")
    viewer_can_react: bool = Field(alias="viewerCanReact")
    viewer_can_unminimize: bool = Field(alias="viewerCanUnminimize")
    viewer_can_unpin: bool = Field(alias="viewerCanUnpin")
    viewer_can_update: bool = Field(alias="viewerCanUpdate")
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason] = Field(
        alias="viewerCannotUpdateReasons"
    )
    viewer_did_author: bool = Field(alias="viewerDidAuthor")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentEditorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedBy(
    BaseModel
):
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEventLabel(
    BaseModel
):
    name: str


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventMergedEventCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEventMergeRef(
    BaseModel
):
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
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


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
    created_at: Any = Field(alias="createdAt")
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
    last_edited_at: Optional[Any] = Field(alias="lastEditedAt")
    minimized_reason: Optional[str] = Field(alias="minimizedReason")
    published_at: Optional[Any] = Field(alias="publishedAt")
    state: PullRequestReviewState
    submitted_at: Optional[Any] = Field(alias="submittedAt")
    updated_at: Any = Field(alias="updatedAt")
    viewer_can_delete: bool = Field(alias="viewerCanDelete")
    viewer_can_minimize: bool = Field(alias="viewerCanMinimize")
    viewer_can_react: bool = Field(alias="viewerCanReact")
    viewer_can_unminimize: bool = Field(alias="viewerCanUnminimize")
    viewer_can_update: bool = Field(alias="viewerCanUpdate")
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason] = Field(
        alias="viewerCannotUpdateReasons"
    )
    viewer_did_author: bool = Field(alias="viewerDidAuthor")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewPullRequestReviewCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewEditorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
    dismissal_message: Optional[str] = Field(alias="dismissalMessage")
    id: str
    previous_review_state: PullRequestReviewState = Field(alias="previousReviewState")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerEnterpriseTeam(
    BaseModel
):
    typename__: Literal["EnterpriseTeam"] = Field(alias="__typename")
    slug: str
    enterprise_team_name: str = Field(alias="enterpriseTeam_name")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    mannequin_name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerTeam(
    BaseModel
):
    typename__: Literal["Team"] = Field(alias="__typename")
    slug: str
    team_name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    user_name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerEnterpriseTeam(
    BaseModel
):
    typename__: Literal["EnterpriseTeam"] = Field(alias="__typename")
    slug: str
    enterprise_team_name: str = Field(alias="enterpriseTeam_name")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    mannequin_name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerTeam(
    BaseModel
):
    typename__: Literal["Team"] = Field(alias="__typename")
    slug: str
    team_name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEventRequestedReviewerUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    user_name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEventAssigneeUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    created_at: Any = Field(alias="createdAt")
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
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEventLabel(
    BaseModel
):
    name: str


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
