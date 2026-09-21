from typing import Annotated, Any, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    DiffSide,
    IssueStateReason,
    LockReason,
    PullRequestReviewState,
    PullRequestReviewThreadSubjectType,
    UserBlockDuration,
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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enqueuer: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventEnqueuer"
    ]
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEventEnqueuer(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEvent(
    BaseModel
):
    typename__: Literal["AddedToProjectEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2Event(
    BaseModel
):
    typename__: Literal["AddedToProjectV2Event"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventProject"
    ]
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2EventProject(
    BaseModel
):
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    disabler: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventDisabler"
    ]
    id: str
    reason: Optional[str]
    reason_code: Optional[str] = Field(alias="reasonCode")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEventDisabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoMergeEnabledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enabler: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventEnabler"
    ]
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEventEnabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoRebaseEnabledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enabler: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventEnabler"
    ]
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEventEnabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoSquashEnabledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enabler: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventEnabler"
    ]
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEventEnabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeFailedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    new_base: str = Field(alias="newBase")
    old_base: str = Field(alias="oldBase")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeSucceededEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    new_base: str = Field(alias="newBase")
    old_base: str = Field(alias="oldBase")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEvent(
    BaseModel
):
    typename__: Literal["BaseRefChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    current_ref_name: str = Field(alias="currentRefName")
    id: str
    previous_ref_name: str = Field(alias="previousRefName")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEvent(
    BaseModel
):
    typename__: Literal["BaseRefDeletedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    base_ref_name: Optional[str] = Field(alias="baseRefName")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEvent(
    BaseModel
):
    typename__: Literal["BaseRefForcePushedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    after_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventAfterCommit"
    ] = Field(alias="afterCommit")
    before_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventBeforeCommit"
    ] = Field(alias="beforeCommit")
    created_at: Any = Field(alias="createdAt")
    id: str
    ref: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventRef"
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventAfterCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventBeforeCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEventRef(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEvent(
    BaseModel
):
    typename__: Literal["BlockedByAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocking_issue: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventBlockingIssue"
    ] = Field(alias="blockingIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEventBlockingIssue(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockedByRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocking_issue: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventBlockingIssue"
    ] = Field(alias="blockingIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEventBlockingIssue(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEvent(
    BaseModel
):
    typename__: Literal["BlockingAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocked_issue: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventBlockedIssue"
    ] = Field(alias="blockedIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEventBlockedIssue(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockingRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocked_issue: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventBlockedIssue"
    ] = Field(alias="blockedIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEventBlockedIssue(
    BaseModel
):
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    deleted_comment_author: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="deletedCommentAuthor")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEvent(
    BaseModel
):
    typename__: Literal["ConnectedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    source: Union[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventSourceIssue",
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventSourcePullRequest",
    ] = Field(discriminator="typename__")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventProject"
    ]
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEventProject(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEvent(
    BaseModel
):
    typename__: Literal["ConvertedNoteToIssueEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project_column_name: str = Field(alias="projectColumnName")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEvent(
    BaseModel
):
    typename__: Literal["ConvertedToDiscussionEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    discussion: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventDiscussion"
    ]
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEventDiscussion(
    BaseModel
):
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    milestone_title: str = Field(alias="milestoneTitle")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEvent(
    BaseModel
):
    typename__: Literal["DeployedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    ref: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventRef"
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEventRef(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEvent(
    BaseModel
):
    typename__: Literal["DeploymentEnvironmentChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEvent(
    BaseModel
):
    typename__: Literal["DisconnectedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    source: Union[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventSourceIssue",
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventSourcePullRequest",
    ] = Field(discriminator="typename__")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEvent(
    BaseModel
):
    typename__: Literal["HeadRefDeletedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    head_ref: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventHeadRef"
    ] = Field(alias="headRef")
    head_ref_name: str = Field(alias="headRefName")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEventHeadRef(
    BaseModel
):
    name: str


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEvent(
    BaseModel
):
    typename__: Literal["IssueCommentUnpinnedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    color: Optional[str]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_field: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldDate",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldMultiSelect",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldNumber",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldSingleSelect",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldText",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="issueField")
    options: Optional[
        list[
            "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventOptions"
        ]
    ]
    value: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldDate(
    BaseModel
):
    typename__: Literal["IssueFieldDate"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldMultiSelect(
    BaseModel
):
    typename__: Literal["IssueFieldMultiSelect"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldNumber(
    BaseModel
):
    typename__: Literal["IssueFieldNumber"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldSingleSelect(
    BaseModel
):
    typename__: Literal["IssueFieldSingleSelect"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldText(
    BaseModel
):
    typename__: Literal["IssueFieldText"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEventOptions(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_field: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldDate",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldMultiSelect",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldNumber",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldSingleSelect",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldText",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="issueField")
    new_color: Optional[str] = Field(alias="newColor")
    new_options: Optional[
        list[
            "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventNewOptions"
        ]
    ] = Field(alias="newOptions")
    new_value: Optional[str] = Field(alias="newValue")
    previous_color: Optional[str] = Field(alias="previousColor")
    previous_options: Optional[
        list[
            "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventPreviousOptions"
        ]
    ] = Field(alias="previousOptions")
    previous_value: Optional[str] = Field(alias="previousValue")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldDate(
    BaseModel
):
    typename__: Literal["IssueFieldDate"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldMultiSelect(
    BaseModel
):
    typename__: Literal["IssueFieldMultiSelect"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldNumber(
    BaseModel
):
    typename__: Literal["IssueFieldNumber"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldSingleSelect(
    BaseModel
):
    typename__: Literal["IssueFieldSingleSelect"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldText(
    BaseModel
):
    typename__: Literal["IssueFieldText"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventNewOptions(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEventPreviousOptions(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_field: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldDate",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldMultiSelect",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldNumber",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldSingleSelect",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldText",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="issueField")
    options: Optional[
        list[
            "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventOptions"
        ]
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldDate(
    BaseModel
):
    typename__: Literal["IssueFieldDate"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldMultiSelect(
    BaseModel
):
    typename__: Literal["IssueFieldMultiSelect"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldNumber(
    BaseModel
):
    typename__: Literal["IssueFieldNumber"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldSingleSelect(
    BaseModel
):
    typename__: Literal["IssueFieldSingleSelect"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldText(
    BaseModel
):
    typename__: Literal["IssueFieldText"] = Field(alias="__typename")
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEventOptions(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_type: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventIssueType"
    ] = Field(alias="issueType")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEventIssueType(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_type: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventIssueType"
    ] = Field(alias="issueType")
    prev_issue_type: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventPrevIssueType"
    ] = Field(alias="prevIssueType")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventIssueType(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEventPrevIssueType(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_type: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventIssueType"
    ] = Field(alias="issueType")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEventIssueType(
    BaseModel
):
    name: str


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    lock_reason: Optional[LockReason] = Field(alias="lockReason")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["MarkedAsDuplicateEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    canonical: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventCanonicalIssue",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventCanonicalPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    duplicate: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventDuplicateIssue",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventDuplicatePullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventCanonicalIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventCanonicalPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventDuplicateIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEventDuplicatePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEvent(
    BaseModel
):
    typename__: Literal["MentionedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    milestone_title: str = Field(alias="milestoneTitle")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEvent(
    BaseModel
):
    typename__: Literal["MovedColumnsInProjectEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    parent: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventParent"
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEventParent(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    parent: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventParent"
    ]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEventParent(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEvent(
    BaseModel
):
    typename__: Literal["PinnedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEvent(
    BaseModel
):
    typename__: Literal["ProjectV2ItemStatusChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    previous_status: str = Field(alias="previousStatus")
    project: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventProject"
    ]
    status: str
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEventProject(
    BaseModel
):
    number: int


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
    pull_request_commit_comment_thread_commit: "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitCommentThreadPullRequestCommitCommentThreadCommit" = Field(
        alias="pullRequestCommitCommentThread_commit"
    )
    id: str
    pull_request_commit_comment_thread_path: Optional[str] = Field(
        alias="pullRequestCommitCommentThread_path"
    )
    position: Optional[int]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitCommentThreadPullRequestCommitCommentThreadCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


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
    diff_side: DiffSide = Field(alias="diffSide")
    id: str
    is_collapsed: bool = Field(alias="isCollapsed")
    is_outdated: bool = Field(alias="isOutdated")
    is_resolved: bool = Field(alias="isResolved")
    line: Optional[int]
    original_line: Optional[int] = Field(alias="originalLine")
    original_start_line: Optional[int] = Field(alias="originalStartLine")
    pull_request_review_thread_path: str = Field(alias="pullRequestReviewThread_path")
    resolved_by: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewThreadResolvedBy"
    ] = Field(alias="resolvedBy")
    start_diff_side: Optional[DiffSide] = Field(alias="startDiffSide")
    start_line: Optional[int] = Field(alias="startLine")
    subject_type: PullRequestReviewThreadSubjectType = Field(alias="subjectType")
    viewer_can_reply: bool = Field(alias="viewerCanReply")
    viewer_can_resolve: bool = Field(alias="viewerCanResolve")
    viewer_can_unresolve: bool = Field(alias="viewerCanUnresolve")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewThreadResolvedBy(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestRevisionMarker(
    BaseModel
):
    typename__: Literal["PullRequestRevisionMarker"] = Field(alias="__typename")
    created_at: Any = Field(alias="createdAt")
    last_seen_commit: "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestRevisionMarkerLastSeenCommit" = Field(
        alias="lastSeenCommit"
    )


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestRevisionMarkerLastSeenCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    referenced_event_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventReferencedEventCommit"
    ] = Field(alias="referencedEvent_commit")
    commit_repository: "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventCommitRepository" = Field(
        alias="commitRepository"
    )
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    is_direct_reference: bool = Field(alias="isDirectReference")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventReferencedEventCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEventCommitRepository(
    BaseModel
):
    name: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEvent(
    BaseModel
):
    typename__: Literal["RemovedFromMergeQueueEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    before_commit: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventBeforeCommit"
    ] = Field(alias="beforeCommit")
    created_at: Any = Field(alias="createdAt")
    enqueuer: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventEnqueuer"
    ]
    id: str
    reason: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventBeforeCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEventEnqueuer(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEvent(
    BaseModel
):
    typename__: Literal["RemovedFromProjectEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2Event(
    BaseModel
):
    typename__: Literal["RemovedFromProjectV2Event"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventProject"
    ]
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2EventProject(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEvent(
    BaseModel
):
    typename__: Literal["RenamedTitleEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    current_title: str = Field(alias="currentTitle")
    id: str
    previous_title: str = Field(alias="previousTitle")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    sub_issue: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventSubIssue"
    ] = Field(alias="subIssue")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEventSubIssue(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["SubIssueRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    sub_issue: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventSubIssue"
    ] = Field(alias="subIssue")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEventSubIssue(
    BaseModel
):
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEvent(
    BaseModel
):
    typename__: Literal["SubscribedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEvent(
    BaseModel
):
    typename__: Literal["TransferredEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    from_repository: Optional[
        "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventFromRepository"
    ] = Field(alias="fromRepository")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEventFromRepository(
    BaseModel
):
    name: str


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["UnmarkedAsDuplicateEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    canonical: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalIssue",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    duplicate: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventDuplicateIssue",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventDuplicatePullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventDuplicateIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEventDuplicatePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEvent(
    BaseModel
):
    typename__: Literal["UnpinnedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEvent(
    BaseModel
):
    typename__: Literal["UnsubscribedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEvent(
    BaseModel
):
    typename__: Literal["UserBlockedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorActor",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorBot",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorEnterpriseUserAccount",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorMannequin",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorOrganization",
                "PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    block_duration: UserBlockDuration = Field(alias="blockDuration")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


PullRequestPage.model_rebuild()
PullRequestPageRepository.model_rebuild()
PullRequestPageRepositoryPullRequests.model_rebuild()
PullRequestPageRepositoryPullRequestsNodes.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItems.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToMergeQueueEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAddedToProjectV2Event.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAssignedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeDisabledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoMergeEnabledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoRebaseEnabledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutoSquashEnabledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeFailedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesAutomaticBaseChangeSucceededEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefChangedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefDeletedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBaseRefForcePushedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByAddedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockedByRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingAddedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesBlockingRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesClosedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCommentDeletedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConnectedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertToDraftEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedFromDraftEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedNoteToIssueEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesConvertedToDiscussionEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesCrossReferencedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDemilestonedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeployedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDeploymentEnvironmentChangedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesDisconnectedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefDeletedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefForcePushedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesHeadRefRestoredEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueComment.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentPinnedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueCommentUnpinnedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldAddedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldChangedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueFieldRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeAddedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeChangedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesIssueTypeRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLabeledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesLockedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMarkedAsDuplicateEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMentionedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMergedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMilestonedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesMovedColumnsInProjectEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueAddedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesParentIssueRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPinnedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesProjectV2ItemStatusChangedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommit.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestCommitCommentThread.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReview.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestReviewThread.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesPullRequestRevisionMarker.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReadyForReviewEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReferencedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromMergeQueueEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRemovedFromProjectV2Event.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesRenamedTitleEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReopenedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewDismissedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesReviewRequestedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueAddedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubIssueRemovedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesSubscribedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesTransferredEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnassignedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlabeledEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnlockedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnmarkedAsDuplicateEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnpinnedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUnsubscribedEvent.model_rebuild()
PullRequestPageRepositoryPullRequestsNodesTimelineItemsNodesUserBlockedEvent.model_rebuild()
