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
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on ClosedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                closer {
                  __typename
                  ... on Commit {
                    oid
                    abbreviatedOid
                  }
                  ... on ProjectV2 {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                createdAt
                duplicateOf {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                id
                stateReason
              }
              ... on ConvertToDraftEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on CrossReferencedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                isCrossRepository
                referencedAt
                source {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                target {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                willCloseTarget
              }
              ... on HeadRefForcePushedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                afterCommit {
                  oid
                  abbreviatedOid
                }
                beforeCommit {
                  oid
                  abbreviatedOid
                }
                createdAt
                id
                ref {
                  name
                }
              }
              ... on IssueComment {
                author {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                authorAssociation
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
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
                  login
                  name
                }
                publishedAt
                updatedAt
                viewerCanDelete
                viewerCanMinimize
                viewerCanPin
                viewerCanReact
                viewerCanUnminimize
                viewerCanUnpin
                viewerCanUpdate
                viewerCannotUpdateReasons
                viewerDidAuthor
              }
              ... on LabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                label {
                  name
                }
              }
              ... on MergedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                mergedEvent_commit: commit {
                  oid
                  abbreviatedOid
                }
                createdAt
                id
                mergeRef {
                  name
                }
                mergeRefName
              }
              ... on PullRequestCommit {
                pullRequestCommit_commit: commit {
                  oid
                  abbreviatedOid
                }
                id
              }
              ... on PullRequestReview {
                author {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                authorAssociation
                authorCanPushToRepository
                pullRequestReview_commit: commit {
                  oid
                  abbreviatedOid
                }
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                fullDatabaseId
                id
                includesCreatedEdit
                isMinimized
                lastEditedAt
                minimizedReason
                publishedAt
                state
                submittedAt
                updatedAt
                viewerCanDelete
                viewerCanMinimize
                viewerCanReact
                viewerCanUnminimize
                viewerCanUpdate
                viewerCannotUpdateReasons
                viewerDidAuthor
              }
              ... on ReadyForReviewEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on ReopenedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
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
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                dismissalMessage
                id
                previousReviewState
              }
              ... on ReviewRequestRemovedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseTeam {
                    slug
                    enterpriseTeam_name: name
                  }
                  ... on Mannequin {
                    login
                    mannequin_name: name
                  }
                  ... on Team {
                    slug
                    team_name: name
                  }
                  ... on User {
                    login
                    user_name: name
                  }
                }
              }
              ... on ReviewRequestedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseTeam {
                    slug
                    enterpriseTeam_name: name
                  }
                  ... on Mannequin {
                    login
                    mannequin_name: name
                  }
                  ... on Team {
                    slug
                    team_name: name
                  }
                  ... on User {
                    login
                    user_name: name
                  }
                }
              }
              ... on UnassignedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on UnlabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                label {
                  name
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
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on ClosedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                closer {
                  __typename
                  ... on Commit {
                    oid
                    abbreviatedOid
                  }
                  ... on ProjectV2 {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                createdAt
                duplicateOf {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                id
                stateReason
              }
              ... on ConvertToDraftEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on CrossReferencedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                isCrossRepository
                referencedAt
                source {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                target {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                willCloseTarget
              }
              ... on HeadRefForcePushedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                afterCommit {
                  oid
                  abbreviatedOid
                }
                beforeCommit {
                  oid
                  abbreviatedOid
                }
                createdAt
                id
                ref {
                  name
                }
              }
              ... on IssueComment {
                author {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                authorAssociation
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
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
                  login
                  name
                }
                publishedAt
                updatedAt
                viewerCanDelete
                viewerCanMinimize
                viewerCanPin
                viewerCanReact
                viewerCanUnminimize
                viewerCanUnpin
                viewerCanUpdate
                viewerCannotUpdateReasons
                viewerDidAuthor
              }
              ... on LabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                label {
                  name
                }
              }
              ... on MergedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                mergedEvent_commit: commit {
                  oid
                  abbreviatedOid
                }
                createdAt
                id
                mergeRef {
                  name
                }
                mergeRefName
              }
              ... on PullRequestCommit {
                pullRequestCommit_commit: commit {
                  oid
                  abbreviatedOid
                }
                id
              }
              ... on PullRequestReview {
                author {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                authorAssociation
                authorCanPushToRepository
                pullRequestReview_commit: commit {
                  oid
                  abbreviatedOid
                }
                createdAt
                createdViaEmail
                editor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                fullDatabaseId
                id
                includesCreatedEdit
                isMinimized
                lastEditedAt
                minimizedReason
                publishedAt
                state
                submittedAt
                updatedAt
                viewerCanDelete
                viewerCanMinimize
                viewerCanReact
                viewerCanUnminimize
                viewerCanUpdate
                viewerCannotUpdateReasons
                viewerDidAuthor
              }
              ... on ReadyForReviewEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on ReopenedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
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
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                dismissalMessage
                id
                previousReviewState
              }
              ... on ReviewRequestRemovedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseTeam {
                    slug
                    enterpriseTeam_name: name
                  }
                  ... on Mannequin {
                    login
                    mannequin_name: name
                  }
                  ... on Team {
                    slug
                    team_name: name
                  }
                  ... on User {
                    login
                    user_name: name
                  }
                }
              }
              ... on ReviewRequestedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                requestedReviewer {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseTeam {
                    slug
                    enterpriseTeam_name: name
                  }
                  ... on Mannequin {
                    login
                    mannequin_name: name
                  }
                  ... on Team {
                    slug
                    team_name: name
                  }
                  ... on User {
                    login
                    user_name: name
                  }
                }
              }
              ... on UnassignedEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                assignee {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
              }
              ... on UnlabeledEvent {
                actor {
                  __typename
                  ... on Bot {
                    login
                  }
                  ... on EnterpriseUserAccount {
                    login
                    name
                  }
                  ... on Mannequin {
                    login
                    name
                  }
                  ... on Organization {
                    login
                    name
                  }
                  ... on User {
                    login
                    name
                  }
                }
                createdAt
                id
                label {
                  name
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
