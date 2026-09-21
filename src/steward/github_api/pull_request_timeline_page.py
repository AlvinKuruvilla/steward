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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enqueuer: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventEnqueuer"
    ]
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEventEnqueuer(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEvent(
    BaseModel
):
    typename__: Literal["AddedToProjectEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2Event(
    BaseModel
):
    typename__: Literal["AddedToProjectV2Event"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventProject"
    ]
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2EventProject(
    BaseModel
):
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    disabler: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventDisabler"
    ]
    id: str
    reason: Optional[str]
    reason_code: Optional[str] = Field(alias="reasonCode")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEventDisabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoMergeEnabledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enabler: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventEnabler"
    ]
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEventEnabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoRebaseEnabledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enabler: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventEnabler"
    ]
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEventEnabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEvent(
    BaseModel
):
    typename__: Literal["AutoSquashEnabledEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    enabler: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventEnabler"
    ]
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEventEnabler(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeFailedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    new_base: str = Field(alias="newBase")
    old_base: str = Field(alias="oldBase")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEvent(
    BaseModel
):
    typename__: Literal["AutomaticBaseChangeSucceededEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    new_base: str = Field(alias="newBase")
    old_base: str = Field(alias="oldBase")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEvent(
    BaseModel
):
    typename__: Literal["BaseRefChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    current_ref_name: str = Field(alias="currentRefName")
    id: str
    previous_ref_name: str = Field(alias="previousRefName")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEvent(
    BaseModel
):
    typename__: Literal["BaseRefDeletedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    base_ref_name: Optional[str] = Field(alias="baseRefName")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEvent(
    BaseModel
):
    typename__: Literal["BaseRefForcePushedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    after_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventAfterCommit"
    ] = Field(alias="afterCommit")
    before_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventBeforeCommit"
    ] = Field(alias="beforeCommit")
    created_at: Any = Field(alias="createdAt")
    id: str
    ref: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventRef"
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventAfterCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventBeforeCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEventRef(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEvent(
    BaseModel
):
    typename__: Literal["BlockedByAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocking_issue: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventBlockingIssue"
    ] = Field(alias="blockingIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEventBlockingIssue(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockedByRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocking_issue: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventBlockingIssue"
    ] = Field(alias="blockingIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEventBlockingIssue(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEvent(
    BaseModel
):
    typename__: Literal["BlockingAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocked_issue: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventBlockedIssue"
    ] = Field(alias="blockedIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEventBlockedIssue(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEvent(
    BaseModel
):
    typename__: Literal["BlockingRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    blocked_issue: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventBlockedIssue"
    ] = Field(alias="blockedIssue")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEventBlockedIssue(
    BaseModel
):
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    deleted_comment_author: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="deletedCommentAuthor")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEventDeletedCommentAuthorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEvent(
    BaseModel
):
    typename__: Literal["ConnectedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    source: Union[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventSourceIssue",
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventSourcePullRequest",
    ] = Field(discriminator="typename__")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventProject"
    ]
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEventProject(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEvent(
    BaseModel
):
    typename__: Literal["ConvertedNoteToIssueEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project_column_name: str = Field(alias="projectColumnName")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEvent(
    BaseModel
):
    typename__: Literal["ConvertedToDiscussionEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    discussion: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventDiscussion"
    ]
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEventDiscussion(
    BaseModel
):
    number: int


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    milestone_title: str = Field(alias="milestoneTitle")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEvent(
    BaseModel
):
    typename__: Literal["DeployedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    ref: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventRef"
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEventRef(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEvent(
    BaseModel
):
    typename__: Literal["DeploymentEnvironmentChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEvent(
    BaseModel
):
    typename__: Literal["DisconnectedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    source: Union[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventSourceIssue",
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventSourcePullRequest",
    ] = Field(discriminator="typename__")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventSourceIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEventSourcePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEvent(
    BaseModel
):
    typename__: Literal["HeadRefDeletedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    head_ref: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventHeadRef"
    ] = Field(alias="headRef")
    head_ref_name: str = Field(alias="headRefName")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEventHeadRef(
    BaseModel
):
    name: str


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEvent(
    BaseModel
):
    typename__: Literal["IssueCommentUnpinnedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorUser",
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
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldDate",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldMultiSelect",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldNumber",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldSingleSelect",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldText",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="issueField")
    options: Optional[
        list[
            "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventOptions"
        ]
    ]
    value: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldDate(
    BaseModel
):
    typename__: Literal["IssueFieldDate"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldMultiSelect(
    BaseModel
):
    typename__: Literal["IssueFieldMultiSelect"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldNumber(
    BaseModel
):
    typename__: Literal["IssueFieldNumber"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldSingleSelect(
    BaseModel
):
    typename__: Literal["IssueFieldSingleSelect"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventIssueFieldIssueFieldText(
    BaseModel
):
    typename__: Literal["IssueFieldText"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEventOptions(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_field: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldDate",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldMultiSelect",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldNumber",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldSingleSelect",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldText",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="issueField")
    new_color: Optional[str] = Field(alias="newColor")
    new_options: Optional[
        list[
            "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventNewOptions"
        ]
    ] = Field(alias="newOptions")
    new_value: Optional[str] = Field(alias="newValue")
    previous_color: Optional[str] = Field(alias="previousColor")
    previous_options: Optional[
        list[
            "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventPreviousOptions"
        ]
    ] = Field(alias="previousOptions")
    previous_value: Optional[str] = Field(alias="previousValue")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldDate(
    BaseModel
):
    typename__: Literal["IssueFieldDate"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldMultiSelect(
    BaseModel
):
    typename__: Literal["IssueFieldMultiSelect"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldNumber(
    BaseModel
):
    typename__: Literal["IssueFieldNumber"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldSingleSelect(
    BaseModel
):
    typename__: Literal["IssueFieldSingleSelect"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventIssueFieldIssueFieldText(
    BaseModel
):
    typename__: Literal["IssueFieldText"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventNewOptions(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEventPreviousOptions(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueFieldRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_field: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldDate",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldMultiSelect",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldNumber",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldSingleSelect",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldText",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="issueField")
    options: Optional[
        list[
            "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventOptions"
        ]
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldDate(
    BaseModel
):
    typename__: Literal["IssueFieldDate"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldMultiSelect(
    BaseModel
):
    typename__: Literal["IssueFieldMultiSelect"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldNumber(
    BaseModel
):
    typename__: Literal["IssueFieldNumber"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldSingleSelect(
    BaseModel
):
    typename__: Literal["IssueFieldSingleSelect"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventIssueFieldIssueFieldText(
    BaseModel
):
    typename__: Literal["IssueFieldText"] = Field(alias="__typename")
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEventOptions(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_type: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventIssueType"
    ] = Field(alias="issueType")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEventIssueType(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_type: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventIssueType"
    ] = Field(alias="issueType")
    prev_issue_type: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventPrevIssueType"
    ] = Field(alias="prevIssueType")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventIssueType(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEventPrevIssueType(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEvent(
    BaseModel
):
    typename__: Literal["IssueTypeRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    issue_type: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventIssueType"
    ] = Field(alias="issueType")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEventIssueType(
    BaseModel
):
    name: str


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    lock_reason: Optional[LockReason] = Field(alias="lockReason")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["MarkedAsDuplicateEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    canonical: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventCanonicalIssue",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventCanonicalPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    duplicate: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventDuplicateIssue",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventDuplicatePullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventCanonicalIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventCanonicalPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventDuplicateIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEventDuplicatePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEvent(
    BaseModel
):
    typename__: Literal["MentionedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    milestone_title: str = Field(alias="milestoneTitle")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEvent(
    BaseModel
):
    typename__: Literal["MovedColumnsInProjectEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueAddedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    parent: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventParent"
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEventParent(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["ParentIssueRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    parent: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventParent"
    ]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEventParent(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEvent(
    BaseModel
):
    typename__: Literal["PinnedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEvent(
    BaseModel
):
    typename__: Literal["ProjectV2ItemStatusChangedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    previous_status: str = Field(alias="previousStatus")
    project: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventProject"
    ]
    status: str
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEventProject(
    BaseModel
):
    number: int


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
    pull_request_commit_comment_thread_commit: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitCommentThreadPullRequestCommitCommentThreadCommit" = Field(
        alias="pullRequestCommitCommentThread_commit"
    )
    id: str
    pull_request_commit_comment_thread_path: Optional[str] = Field(
        alias="pullRequestCommitCommentThread_path"
    )
    position: Optional[int]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitCommentThreadPullRequestCommitCommentThreadCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


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
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewThreadResolvedBy"
    ] = Field(alias="resolvedBy")
    start_diff_side: Optional[DiffSide] = Field(alias="startDiffSide")
    start_line: Optional[int] = Field(alias="startLine")
    subject_type: PullRequestReviewThreadSubjectType = Field(alias="subjectType")
    viewer_can_reply: bool = Field(alias="viewerCanReply")
    viewer_can_resolve: bool = Field(alias="viewerCanResolve")
    viewer_can_unresolve: bool = Field(alias="viewerCanUnresolve")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewThreadResolvedBy(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestRevisionMarker(
    BaseModel
):
    typename__: Literal["PullRequestRevisionMarker"] = Field(alias="__typename")
    created_at: Any = Field(alias="createdAt")
    last_seen_commit: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestRevisionMarkerLastSeenCommit" = Field(
        alias="lastSeenCommit"
    )


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestRevisionMarkerLastSeenCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    referenced_event_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventReferencedEventCommit"
    ] = Field(alias="referencedEvent_commit")
    commit_repository: "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventCommitRepository" = Field(
        alias="commitRepository"
    )
    created_at: Any = Field(alias="createdAt")
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")
    is_direct_reference: bool = Field(alias="isDirectReference")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventReferencedEventCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEventCommitRepository(
    BaseModel
):
    name: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEvent(
    BaseModel
):
    typename__: Literal["RemovedFromMergeQueueEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    before_commit: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventBeforeCommit"
    ] = Field(alias="beforeCommit")
    created_at: Any = Field(alias="createdAt")
    enqueuer: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventEnqueuer"
    ]
    id: str
    reason: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventBeforeCommit(
    BaseModel
):
    oid: Any
    abbreviated_oid: str = Field(alias="abbreviatedOid")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEventEnqueuer(
    BaseModel
):
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEvent(
    BaseModel
):
    typename__: Literal["RemovedFromProjectEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2Event(
    BaseModel
):
    typename__: Literal["RemovedFromProjectV2Event"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    project: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventProject"
    ]
    was_automated: bool = Field(alias="wasAutomated")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2EventProject(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEvent(
    BaseModel
):
    typename__: Literal["RenamedTitleEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    current_title: str = Field(alias="currentTitle")
    id: str
    previous_title: str = Field(alias="previousTitle")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    sub_issue: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventSubIssue"
    ] = Field(alias="subIssue")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEventSubIssue(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEvent(
    BaseModel
):
    typename__: Literal["SubIssueRemovedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str
    sub_issue: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventSubIssue"
    ] = Field(alias="subIssue")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEventSubIssue(
    BaseModel
):
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEvent(
    BaseModel
):
    typename__: Literal["SubscribedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEvent(
    BaseModel
):
    typename__: Literal["TransferredEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    from_repository: Optional[
        "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventFromRepository"
    ] = Field(alias="fromRepository")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEventFromRepository(
    BaseModel
):
    name: str


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
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEvent(
    BaseModel
):
    typename__: Literal["UnmarkedAsDuplicateEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    canonical: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalIssue",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalPullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    duplicate: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventDuplicateIssue",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventDuplicatePullRequest",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    id: str
    is_cross_repository: bool = Field(alias="isCrossRepository")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventCanonicalPullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventDuplicateIssue(
    BaseModel
):
    typename__: Literal["Issue"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEventDuplicatePullRequest(
    BaseModel
):
    typename__: Literal["PullRequest"] = Field(alias="__typename")
    number: int


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEvent(
    BaseModel
):
    typename__: Literal["UnpinnedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEvent(
    BaseModel
):
    typename__: Literal["UnsubscribedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEvent(
    BaseModel
):
    typename__: Literal["UserBlockedEvent"] = Field(alias="__typename")
    actor: Optional[
        Annotated[
            Union[
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorActor",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorBot",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorEnterpriseUserAccount",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorMannequin",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorOrganization",
                "PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorUser",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    block_duration: UserBlockDuration = Field(alias="blockDuration")
    created_at: Any = Field(alias="createdAt")
    id: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorActor(
    BaseModel
):
    typename__: Literal["Actor"] = Field(alias="__typename")


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorBot(
    BaseModel
):
    typename__: Literal["Bot"] = Field(alias="__typename")
    login: str


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorEnterpriseUserAccount(
    BaseModel
):
    typename__: Literal["EnterpriseUserAccount"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorMannequin(
    BaseModel
):
    typename__: Literal["Mannequin"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorOrganization(
    BaseModel
):
    typename__: Literal["Organization"] = Field(alias="__typename")
    login: str
    name: Optional[str]


class PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEventActorUser(
    BaseModel
):
    typename__: Literal["User"] = Field(alias="__typename")
    login: str
    name: Optional[str]


PullRequestTimelinePage.model_rebuild()
PullRequestTimelinePageRepository.model_rebuild()
PullRequestTimelinePageRepositoryPullRequest.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItems.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToMergeQueueEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAddedToProjectV2Event.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAssignedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeDisabledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoMergeEnabledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoRebaseEnabledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutoSquashEnabledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeFailedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesAutomaticBaseChangeSucceededEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefChangedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefDeletedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBaseRefForcePushedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByAddedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockedByRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingAddedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesBlockingRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesClosedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCommentDeletedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConnectedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertToDraftEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedFromDraftEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedNoteToIssueEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesConvertedToDiscussionEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesCrossReferencedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDemilestonedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeployedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDeploymentEnvironmentChangedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesDisconnectedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefDeletedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefForcePushedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesHeadRefRestoredEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueComment.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentPinnedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueCommentUnpinnedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldAddedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldChangedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueFieldRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeAddedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeChangedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesIssueTypeRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLabeledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesLockedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMarkedAsDuplicateEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMentionedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMergedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMilestonedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesMovedColumnsInProjectEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueAddedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesParentIssueRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPinnedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesProjectV2ItemStatusChangedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommit.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestCommitCommentThread.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReview.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestReviewThread.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesPullRequestRevisionMarker.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReadyForReviewEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReferencedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromMergeQueueEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRemovedFromProjectV2Event.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesRenamedTitleEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReopenedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewDismissedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesReviewRequestedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueAddedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubIssueRemovedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesSubscribedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesTransferredEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnassignedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlabeledEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnlockedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnmarkedAsDuplicateEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnpinnedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUnsubscribedEvent.model_rebuild()
PullRequestTimelinePageRepositoryPullRequestTimelineItemsNodesUserBlockedEvent.model_rebuild()
