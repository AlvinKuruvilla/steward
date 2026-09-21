from typing import Annotated, Any, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    IssueStateReason,
    PullRequestReviewState,
)


class PullRequestTimelinePage(BaseModel):
    repository: Optional["PullRequestTimelinePageRepository"]


class PullRequestTimelinePageRepository(BaseModel):
    pull_request: Optional["PullRequestTimelinePageRepositoryPullRequest"] = Field(
        alias="pullRequest"
    )


class PullRequestTimelinePageRepositoryPullRequest(BaseModel):
    number: int
    timeline_items: "PullRequestTimelinePageRepositoryPullRequestTimelineItems" = Field(
        alias="timelineItems"
    )


class PullRequestTimelinePageRepositoryPullRequestTimelineItems(BaseModel):
    page_info: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsPageInfo" = (
        Field(alias="pageInfo")
    )
    nodes: Optional[
        list[
            Optional[
                Annotated[
                    Union[
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2Event",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueComment",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommit",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitCommentThread",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReview",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewThread",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestRevisionMarker",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2Event",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEvent",
                        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEvent",
                    ],
                    Field(discriminator="typename__"),
                ]
            ]
        ]
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsPageInfo(BaseModel):
    has_next_page: bool = Field(alias="hasNextPage")
    end_cursor: Optional[str] = Field(alias="endCursor")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEvent(
    BaseModel
):
    typename__: Literal["AddedToMergeQueueEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEvent(
    BaseModel
):
    typename__: Literal["AddedToProjectEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2Event(
    BaseModel
):
    typename__: Literal["AddedToProjectV2Event"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEvent(
    BaseModel
):
    typename__: Literal["AssignedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    assignee: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEventAssigneeUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEvent(
    BaseModel
):
    typename__: Literal["AutoMergeDisabledEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoMergeEnabledEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoRebaseEnabledEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoSquashEnabledEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeFailedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeSucceededEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEvent(
    BaseModel
):
    typename__: Literal["BaseRefChangedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEvent(
    BaseModel
):
    typename__: Literal["BaseRefDeletedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEvent(
    BaseModel
):
    typename__: Literal["BaseRefForcePushedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEvent(
    BaseModel
):
    typename__: Literal["BlockedByAddedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockedByRemovedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEvent(
    BaseModel
):
    typename__: Literal["BlockingAddedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockingRemovedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEvent(
    BaseModel
):
    typename__: Literal["ClosedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    closer: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventCloserCommit",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventCloserProjectV2",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventCloserPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    duplicate_of: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventDuplicateOfIssue",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventDuplicateOfPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="duplicateOf")
    id: str
    state_reason: Optional[IssueStateReason] = Field(alias="stateReason")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventCloserCommit(
    BaseModel
):
    typename__: Literal["Commit"] = Field(alias="__typename")
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventCloserProjectV2(
    BaseModel
):
    typename__: Literal["ProjectV2"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventCloserPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventDuplicateOfIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEventDuplicateOfPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEvent(
    BaseModel
):
    typename__: Literal["CommentDeletedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEvent(
    BaseModel
):
    typename__: Literal["ConnectedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEvent(
    BaseModel
):
    typename__: Literal["ConvertToDraftEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEvent(
    BaseModel
):
    typename__: Literal["ConvertedFromDraftEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEvent(
    BaseModel
):
    typename__: Literal["ConvertedNoteToIssueEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEvent(
    BaseModel
):
    typename__: Literal["ConvertedToDiscussionEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEvent(
    BaseModel
):
    typename__: Literal["CrossReferencedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    referenced_at: Any = Field(alias="referencedAt")
    source: Union[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventSourceIssue",
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventSourcePullRequest",
    ] = Field(discriminator="typename__")
    target: Union[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventTargetIssue",
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventTargetPullRequest",
    ] = Field(discriminator="typename__")
    will_close_target: bool = Field(alias="willCloseTarget")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventTargetIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEventTargetPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEvent(
    BaseModel
):
    typename__: Literal["DemilestonedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEvent(
    BaseModel
):
    typename__: Literal["DeployedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEvent(
    BaseModel
):
    typename__: Literal["DeploymentEnvironmentChangedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEvent(
    BaseModel
):
    typename__: Literal["DisconnectedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEvent(
    BaseModel
):
    typename__: Literal["HeadRefDeletedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEvent(
    BaseModel
):
    typename__: Literal["HeadRefForcePushedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    after_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventAfterCommit"
    ] = Field(alias="afterCommit")
    before_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventBeforeCommit"
    ] = Field(alias="beforeCommit")
    created_at: Any = Field(alias="createdAt")
    id: str
    ref: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventRef"
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventAfterCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventBeforeCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEventRef(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEvent(
    BaseModel
):
    typename__: Literal["HeadRefRestoredEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueComment(
    BaseModel
):
    typename__: Literal["IssueComment"] = Field(alias="__typename")
    author: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorUser",
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
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorUser",
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
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedBy"
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


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentEditorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedBy(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEvent(
    BaseModel
):
    typename__: Literal["IssueCommentPinnedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEvent(
    BaseModel
):
    typename__: Literal["IssueCommentUnpinnedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldAddedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldChangedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldRemovedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeAddedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeChangedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeRemovedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEvent(
    BaseModel
):
    typename__: Literal["LabeledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    label: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventLabel"


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEventLabel(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEvent(
    BaseModel
):
    typename__: Literal["LockedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["MarkedAsDuplicateEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEvent(
    BaseModel
):
    typename__: Literal["MentionedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEvent(
    BaseModel
):
    typename__: Literal["MergedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    merged_event_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventMergedEventCommit"
    ] = Field(alias="mergedEvent_commit")
    created_at: Any = Field(alias="createdAt")
    id: str
    merge_ref: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventMergeRef"
    ] = Field(alias="mergeRef")
    merge_ref_name: str = Field(alias="mergeRefName")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventMergedEventCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEventMergeRef(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEvent(
    BaseModel
):
    typename__: Literal["MilestonedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEvent(
    BaseModel
):
    typename__: Literal["MovedColumnsInProjectEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueAddedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueRemovedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEvent(
    BaseModel
):
    typename__: Literal["PinnedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEvent(
    BaseModel
):
    typename__: Literal["ProjectV2ItemStatusChangedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommit(
    BaseModel
):
    typename__: Literal["PullRequestCommit"] = Field(alias="__typename")
    pull_request_commit_commit: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitPullRequestCommitCommit" = Field(
        alias="pullRequestCommit_commit"
    )
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitPullRequestCommitCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitCommentThread(
    BaseModel
):
    typename__: Literal["PullRequestCommitCommentThread"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReview(
    BaseModel
):
    typename__: Literal["PullRequestReview"] = Field(alias="__typename")
    author: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    author_association: CommentAuthorAssociation = Field(alias="authorAssociation")
    author_can_push_to_repository: bool = Field(alias="authorCanPushToRepository")
    pull_request_review_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewPullRequestReviewCommit"
    ] = Field(alias="pullRequestReview_commit")
    created_at: Any = Field(alias="createdAt")
    created_via_email: bool = Field(alias="createdViaEmail")
    editor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorUser",
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


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewPullRequestReviewCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewEditorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewThread(
    BaseModel
):
    typename__: Literal["PullRequestReviewThread"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestRevisionMarker(
    BaseModel
):
    typename__: Literal["PullRequestRevisionMarker"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEvent(
    BaseModel
):
    typename__: Literal["ReadyForReviewEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEvent(
    BaseModel
):
    typename__: Literal["ReferencedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEvent(
    BaseModel
):
    typename__: Literal["RemovedFromMergeQueueEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEvent(
    BaseModel
):
    typename__: Literal["RemovedFromProjectEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2Event(
    BaseModel
):
    typename__: Literal["RemovedFromProjectV2Event"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEvent(
    BaseModel
):
    typename__: Literal["RenamedTitleEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEvent(
    BaseModel
):
    typename__: Literal["ReopenedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    state_reason: Optional[IssueStateReason] = Field(alias="stateReason")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEvent(
    BaseModel
):
    typename__: Literal["ReviewDismissedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    dismissal_message: Optional[str] = Field(alias="dismissalMessage")
    id: str
    previous_review_state: PullRequestReviewState = Field(alias="previousReviewState")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEvent(
    BaseModel
):
    typename__: Literal["ReviewRequestRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    requested_reviewer: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerEnterpriseTeam",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerTeam",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerUser",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="requestedReviewer")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerEnterpriseTeam(
    BaseModel
):
    typename__: Literal["EnterpriseTeam"] = Field(alias="__typename")
    slug: str
    enterprise_team_name: str = Field(alias="enterpriseTeam_name")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    mannequin_name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerTeam(
    BaseModel
):
    typename__: Literal["Team"] = Field(alias="__typename")
    slug: str
    team_name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEventRequestedReviewerUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    user_name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEvent(
    BaseModel
):
    typename__: Literal["ReviewRequestedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    requested_reviewer: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerEnterpriseTeam",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerTeam",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerUser",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="requestedReviewer")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerEnterpriseTeam(
    BaseModel
):
    typename__: Literal["EnterpriseTeam"] = Field(alias="__typename")
    slug: str
    enterprise_team_name: str = Field(alias="enterpriseTeam_name")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    mannequin_name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerTeam(
    BaseModel
):
    typename__: Literal["Team"] = Field(alias="__typename")
    slug: str
    team_name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEventRequestedReviewerUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    user_name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEvent(
    BaseModel
):
    typename__: Literal["SubIssueAddedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["SubIssueRemovedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEvent(
    BaseModel
):
    typename__: Literal["SubscribedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEvent(
    BaseModel
):
    typename__: Literal["TransferredEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEvent(
    BaseModel
):
    typename__: Literal["UnassignedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    assignee: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEventAssigneeUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEvent(
    BaseModel
):
    typename__: Literal["UnlabeledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    label: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventLabel"


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEventLabel(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEvent(
    BaseModel
):
    typename__: Literal["UnlockedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["UnmarkedAsDuplicateEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEvent(
    BaseModel
):
    typename__: Literal["UnpinnedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEvent(
    BaseModel
):
    typename__: Literal["UnsubscribedEvent"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEvent(
    BaseModel
):
    typename__: Literal["UserBlockedEvent"] = Field(alias="__typename")


PullRequestTimelinePage.model_rebuild()
PullRequestTimelinePageRepository.model_rebuild()
PullRequestTimelinePageRepositoryPullRequest.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItems.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueComment.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommit.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReview.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEvent.model_rebuild()
