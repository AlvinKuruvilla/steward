from typing import Any, Optional, Union

from .async_base_client import AsyncBaseClient
from .base_model import UNSET, UnsetType
from .pull_request_page import PullRequestPage
from .pull_request_timeline_page import PullRequestTimelinePage


def gql(q: str) -> str:
    return q


class GitHubClient(AsyncBaseClient):
    async def pull_request_page(
        self,
        owner: str,
        name: str,
        cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> PullRequestPage:
        query = gql("""
            query PullRequestPage($owner: String!, $name: String!, $cursor: String) {
              repository(owner: $owner, name: $name) {
                pullRequests(
                  first: 25
                  after: $cursor
                  orderBy: {field: CREATED_AT, direction: DESC}
                ) {
                  pageInfo {
                    hasNextPage
                    endCursor
                  }
                  nodes {
                    ...PullRequestSnapshot
                    timelineItems(
                      first: 100
                      itemTypes: [ASSIGNED_EVENT, CLOSED_EVENT, CONVERT_TO_DRAFT_EVENT, CROSS_REFERENCED_EVENT, HEAD_REF_FORCE_PUSHED_EVENT, ISSUE_COMMENT, LABELED_EVENT, MERGED_EVENT, PULL_REQUEST_COMMIT, PULL_REQUEST_REVIEW, READY_FOR_REVIEW_EVENT, REOPENED_EVENT, REVIEW_DISMISSED_EVENT, REVIEW_REQUESTED_EVENT, REVIEW_REQUEST_REMOVED_EVENT, UNASSIGNED_EVENT, UNLABELED_EVENT]
                    ) {
                      totalCount
                      pageInfo {
                        hasNextPage
                        endCursor
                      }
                      nodes {
                        ...TimelineItem
                      }
                    }
                  }
                }
              }
            }

            fragment PullRequestSnapshot on PullRequest {
              id
              number
              title
              state
              isDraft
              createdAt
              closedAt
              mergedAt
              additions
              deletions
              changedFiles
              baseRefName
              headRefName
              authorAssociation
              author {
                __typename
                login
              }
              labels(first: 100) {
                nodes {
                  name
                }
              }
            }

            fragment TimelineItem on PullRequestTimelineItems {
              __typename
              ... on AssignedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on ClosedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                closer {
                  __typename
                  ... on Commit {
                    id
                    oid
                    abbreviatedOid
                    authoredDate
                    committedDate
                  }
                  ... on ProjectV2 {
                    id
                    number
                    closedAt
                    createdAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                createdAt
                duplicateOf {
                  __typename
                  ... on Issue {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    publishedAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                id
                stateReason
              }
              ... on ConvertToDraftEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on CrossReferencedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                isCrossRepository
                referencedAt
                source {
                  __typename
                  ... on Issue {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    publishedAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                target {
                  __typename
                  ... on Issue {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    publishedAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                willCloseTarget
              }
              ... on HeadRefForcePushedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                afterCommit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                beforeCommit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                createdAt
                id
                ref {
                  id
                  name
                }
              }
              ... on IssueComment {
                author {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                authorAssociation
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                fullDatabaseId
                id
                includesCreatedEdit
                isMinimized
                isPinned
                lastEditedAt
                minimizedReason
                pinnedAt
                pinnedBy {
                  id
                  login
                  name
                  createdAt
                  updatedAt
                }
                publishedAt
                reactionGroups {
                  createdAt
                }
                updatedAt
              }
              ... on LabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                label {
                  id
                  name
                  createdAt
                  updatedAt
                }
              }
              ... on MergedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                mergedEvent_commit: commit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                createdAt
                id
                mergeRef {
                  id
                  name
                }
                mergeRefName
              }
              ... on PullRequestCommit {
                pullRequestCommit_commit: commit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                id
              }
              ... on PullRequestReview {
                author {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                authorAssociation
                authorCanPushToRepository
                pullRequestReview_commit: commit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                fullDatabaseId
                id
                includesCreatedEdit
                isMinimized
                lastEditedAt
                minimizedReason
                publishedAt
                reactionGroups {
                  createdAt
                }
                state
                submittedAt
                updatedAt
              }
              ... on ReadyForReviewEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on ReopenedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                stateReason
              }
              ... on ReviewDismissedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                dismissalMessage
                id
                previousReviewState
                pullRequestCommit {
                  id
                }
                review {
                  id
                  createdAt
                  lastEditedAt
                  publishedAt
                  submittedAt
                  updatedAt
                }
              }
              ... on ReviewRequestRemovedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseTeam {
                    id
                    slug
                    enterpriseTeam_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    mannequin_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Team {
                    id
                    slug
                    team_name: name
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    user_name: name
                    createdAt
                    updatedAt
                  }
                }
              }
              ... on ReviewRequestedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseTeam {
                    id
                    slug
                    enterpriseTeam_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    mannequin_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Team {
                    id
                    slug
                    team_name: name
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    user_name: name
                    createdAt
                    updatedAt
                  }
                }
              }
              ... on UnassignedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on UnlabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                label {
                  id
                  name
                  createdAt
                  updatedAt
                }
              }
            }
            """)
        variables: dict[str, object] = {"owner": owner, "name": name, "cursor": cursor}
        response = await self.execute(
            query=query, operation_name="PullRequestPage", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return PullRequestPage.model_validate(data)

    async def pull_request_timeline_page(
        self,
        owner: str,
        name: str,
        number: int,
        cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> PullRequestTimelinePage:
        query = gql("""
            query PullRequestTimelinePage($owner: String!, $name: String!, $number: Int!, $cursor: String) {
              repository(owner: $owner, name: $name) {
                pullRequest(number: $number) {
                  number
                  timelineItems(
                    first: 100
                    after: $cursor
                    itemTypes: [ASSIGNED_EVENT, CLOSED_EVENT, CONVERT_TO_DRAFT_EVENT, CROSS_REFERENCED_EVENT, HEAD_REF_FORCE_PUSHED_EVENT, ISSUE_COMMENT, LABELED_EVENT, MERGED_EVENT, PULL_REQUEST_COMMIT, PULL_REQUEST_REVIEW, READY_FOR_REVIEW_EVENT, REOPENED_EVENT, REVIEW_DISMISSED_EVENT, REVIEW_REQUESTED_EVENT, REVIEW_REQUEST_REMOVED_EVENT, UNASSIGNED_EVENT, UNLABELED_EVENT]
                  ) {
                    pageInfo {
                      hasNextPage
                      endCursor
                    }
                    nodes {
                      ...TimelineItem
                    }
                  }
                }
              }
            }

            fragment TimelineItem on PullRequestTimelineItems {
              __typename
              ... on AssignedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on ClosedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                closer {
                  __typename
                  ... on Commit {
                    id
                    oid
                    abbreviatedOid
                    authoredDate
                    committedDate
                  }
                  ... on ProjectV2 {
                    id
                    number
                    closedAt
                    createdAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                createdAt
                duplicateOf {
                  __typename
                  ... on Issue {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    publishedAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                id
                stateReason
              }
              ... on ConvertToDraftEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on CrossReferencedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                isCrossRepository
                referencedAt
                source {
                  __typename
                  ... on Issue {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    publishedAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                target {
                  __typename
                  ... on Issue {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    publishedAt
                    updatedAt
                  }
                  ... on PullRequest {
                    id
                    number
                    closedAt
                    createdAt
                    lastEditedAt
                    mergedAt
                    publishedAt
                    updatedAt
                  }
                }
                willCloseTarget
              }
              ... on HeadRefForcePushedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                afterCommit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                beforeCommit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                createdAt
                id
                ref {
                  id
                  name
                }
              }
              ... on IssueComment {
                author {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                authorAssociation
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                fullDatabaseId
                id
                includesCreatedEdit
                isMinimized
                isPinned
                lastEditedAt
                minimizedReason
                pinnedAt
                pinnedBy {
                  id
                  login
                  name
                  createdAt
                  updatedAt
                }
                publishedAt
                reactionGroups {
                  createdAt
                }
                updatedAt
              }
              ... on LabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                label {
                  id
                  name
                  createdAt
                  updatedAt
                }
              }
              ... on MergedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                mergedEvent_commit: commit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                createdAt
                id
                mergeRef {
                  id
                  name
                }
                mergeRefName
              }
              ... on PullRequestCommit {
                pullRequestCommit_commit: commit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                id
              }
              ... on PullRequestReview {
                author {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                authorAssociation
                authorCanPushToRepository
                pullRequestReview_commit: commit {
                  id
                  oid
                  abbreviatedOid
                  authoredDate
                  committedDate
                }
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                fullDatabaseId
                id
                includesCreatedEdit
                isMinimized
                lastEditedAt
                minimizedReason
                publishedAt
                reactionGroups {
                  createdAt
                }
                state
                submittedAt
                updatedAt
              }
              ... on ReadyForReviewEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on ReopenedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                stateReason
              }
              ... on ReviewDismissedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                dismissalMessage
                id
                previousReviewState
                pullRequestCommit {
                  id
                }
                review {
                  id
                  createdAt
                  lastEditedAt
                  publishedAt
                  submittedAt
                  updatedAt
                }
              }
              ... on ReviewRequestRemovedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseTeam {
                    id
                    slug
                    enterpriseTeam_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    mannequin_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Team {
                    id
                    slug
                    team_name: name
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    user_name: name
                    createdAt
                    updatedAt
                  }
                }
              }
              ... on ReviewRequestedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseTeam {
                    id
                    slug
                    enterpriseTeam_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    mannequin_name: name
                    createdAt
                    updatedAt
                  }
                  ... on Team {
                    id
                    slug
                    team_name: name
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    user_name: name
                    createdAt
                    updatedAt
                  }
                }
              }
              ... on UnassignedEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
              }
              ... on UnlabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    id
                    login
                    createdAt
                    updatedAt
                  }
                  ... on EnterpriseUserAccount {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Mannequin {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                  ... on Organization {
                    id
                    login
                    name
                    archivedAt
                    createdAt
                    updatedAt
                  }
                  ... on User {
                    id
                    login
                    name
                    createdAt
                    updatedAt
                  }
                }
                createdAt
                id
                label {
                  id
                  name
                  createdAt
                  updatedAt
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "owner": owner,
            "name": name,
            "number": number,
            "cursor": cursor,
        }
        response = await self.execute(
            query=query,
            operation_name="PullRequestTimelinePage",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return PullRequestTimelinePage.model_validate(data)
