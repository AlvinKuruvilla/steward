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
                    timelineItems(first: 100) {
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
              ... on AddedToMergeQueueEvent {
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
                enqueuer {
                  login
                  name
                }
                id
              }
              ... on AddedToProjectEvent {
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
              ... on AddedToProjectV2Event {
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
                project {
                  number
                }
                wasAutomated
              }
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
              ... on AutoMergeDisabledEvent {
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
                disabler {
                  login
                  name
                }
                id
                reason
                reasonCode
              }
              ... on AutoMergeEnabledEvent {
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
                enabler {
                  login
                  name
                }
                id
              }
              ... on AutoRebaseEnabledEvent {
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
                enabler {
                  login
                  name
                }
                id
              }
              ... on AutoSquashEnabledEvent {
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
                enabler {
                  login
                  name
                }
                id
              }
              ... on AutomaticBaseChangeFailedEvent {
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
                newBase
                oldBase
              }
              ... on AutomaticBaseChangeSucceededEvent {
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
                newBase
                oldBase
              }
              ... on BaseRefChangedEvent {
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
                currentRefName
                id
                previousRefName
              }
              ... on BaseRefDeletedEvent {
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
                baseRefName
                createdAt
                id
              }
              ... on BaseRefForcePushedEvent {
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
              ... on BlockedByAddedEvent {
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
                blockingIssue {
                  number
                }
                createdAt
                id
              }
              ... on BlockedByRemovedEvent {
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
                blockingIssue {
                  number
                }
                createdAt
                id
              }
              ... on BlockingAddedEvent {
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
                blockedIssue {
                  number
                }
                createdAt
                id
              }
              ... on BlockingRemovedEvent {
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
                blockedIssue {
                  number
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
              ... on CommentDeletedEvent {
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
                deletedCommentAuthor {
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
                id
              }
              ... on ConnectedEvent {
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
                source {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
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
              ... on ConvertedFromDraftEvent {
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
                project {
                  number
                }
                wasAutomated
              }
              ... on ConvertedNoteToIssueEvent {
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
                projectColumnName
              }
              ... on ConvertedToDiscussionEvent {
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
                discussion {
                  number
                }
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
              ... on DemilestonedEvent {
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
                milestoneTitle
              }
              ... on DeployedEvent {
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
                ref {
                  name
                }
              }
              ... on DeploymentEnvironmentChangedEvent {
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
              ... on DisconnectedEvent {
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
                source {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
              }
              ... on HeadRefDeletedEvent {
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
                headRef {
                  name
                }
                headRefName
                id
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
              ... on HeadRefRestoredEvent {
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
              ... on IssueCommentPinnedEvent {
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
              ... on IssueCommentUnpinnedEvent {
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
              ... on IssueFieldAddedEvent {
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
                color
                createdAt
                id
                issueField {
                  __typename
                  ... on IssueFieldDate {
                    name
                  }
                  ... on IssueFieldMultiSelect {
                    name
                  }
                  ... on IssueFieldNumber {
                    name
                  }
                  ... on IssueFieldSingleSelect {
                    name
                  }
                  ... on IssueFieldText {
                    name
                  }
                }
                options {
                  name
                }
                value
              }
              ... on IssueFieldChangedEvent {
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
                issueField {
                  __typename
                  ... on IssueFieldDate {
                    name
                  }
                  ... on IssueFieldMultiSelect {
                    name
                  }
                  ... on IssueFieldNumber {
                    name
                  }
                  ... on IssueFieldSingleSelect {
                    name
                  }
                  ... on IssueFieldText {
                    name
                  }
                }
                newColor
                newOptions {
                  name
                }
                newValue
                previousColor
                previousOptions {
                  name
                }
                previousValue
              }
              ... on IssueFieldRemovedEvent {
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
                issueField {
                  __typename
                  ... on IssueFieldDate {
                    name
                  }
                  ... on IssueFieldMultiSelect {
                    name
                  }
                  ... on IssueFieldNumber {
                    name
                  }
                  ... on IssueFieldSingleSelect {
                    name
                  }
                  ... on IssueFieldText {
                    name
                  }
                }
                options {
                  name
                }
              }
              ... on IssueTypeAddedEvent {
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
                issueType {
                  name
                }
              }
              ... on IssueTypeChangedEvent {
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
                issueType {
                  name
                }
                prevIssueType {
                  name
                }
              }
              ... on IssueTypeRemovedEvent {
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
                issueType {
                  name
                }
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
              ... on LockedEvent {
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
                lockReason
              }
              ... on MarkedAsDuplicateEvent {
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
                canonical {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                createdAt
                duplicate {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                id
                isCrossRepository
              }
              ... on MentionedEvent {
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
              ... on MilestonedEvent {
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
                milestoneTitle
              }
              ... on MovedColumnsInProjectEvent {
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
              ... on ParentIssueAddedEvent {
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
                parent {
                  number
                }
              }
              ... on ParentIssueRemovedEvent {
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
                parent {
                  number
                }
              }
              ... on PinnedEvent {
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
              ... on ProjectV2ItemStatusChangedEvent {
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
                previousStatus
                project {
                  number
                }
                status
                wasAutomated
              }
              ... on PullRequestCommit {
                pullRequestCommit_commit: commit {
                  oid
                  abbreviatedOid
                }
                id
              }
              ... on PullRequestCommitCommentThread {
                pullRequestCommitCommentThread_commit: commit {
                  oid
                  abbreviatedOid
                }
                id
                pullRequestCommitCommentThread_path: path
                position
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
              ... on PullRequestReviewThread {
                diffSide
                id
                isCollapsed
                isOutdated
                isResolved
                line
                originalLine
                originalStartLine
                pullRequestReviewThread_path: path
                resolvedBy {
                  login
                  name
                }
                startDiffSide
                startLine
                subjectType
                viewerCanReply
                viewerCanResolve
                viewerCanUnresolve
              }
              ... on PullRequestRevisionMarker {
                createdAt
                lastSeenCommit {
                  oid
                  abbreviatedOid
                }
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
              ... on ReferencedEvent {
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
                referencedEvent_commit: commit {
                  oid
                  abbreviatedOid
                }
                commitRepository {
                  name
                }
                createdAt
                id
                isCrossRepository
                isDirectReference
              }
              ... on RemovedFromMergeQueueEvent {
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
                beforeCommit {
                  oid
                  abbreviatedOid
                }
                createdAt
                enqueuer {
                  login
                  name
                }
                id
                reason
              }
              ... on RemovedFromProjectEvent {
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
              ... on RemovedFromProjectV2Event {
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
                project {
                  number
                }
                wasAutomated
              }
              ... on RenamedTitleEvent {
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
                currentTitle
                id
                previousTitle
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
              ... on SubIssueAddedEvent {
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
                subIssue {
                  number
                }
              }
              ... on SubIssueRemovedEvent {
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
                subIssue {
                  number
                }
              }
              ... on SubscribedEvent {
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
              ... on TransferredEvent {
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
                fromRepository {
                  name
                }
                id
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
              ... on UnlockedEvent {
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
              ... on UnmarkedAsDuplicateEvent {
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
                canonical {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                createdAt
                duplicate {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                id
                isCrossRepository
              }
              ... on UnpinnedEvent {
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
              ... on UnsubscribedEvent {
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
              ... on UserBlockedEvent {
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
                blockDuration
                createdAt
                id
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
                  timelineItems(first: 100, after: $cursor) {
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
              ... on AddedToMergeQueueEvent {
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
                enqueuer {
                  login
                  name
                }
                id
              }
              ... on AddedToProjectEvent {
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
              ... on AddedToProjectV2Event {
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
                project {
                  number
                }
                wasAutomated
              }
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
              ... on AutoMergeDisabledEvent {
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
                disabler {
                  login
                  name
                }
                id
                reason
                reasonCode
              }
              ... on AutoMergeEnabledEvent {
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
                enabler {
                  login
                  name
                }
                id
              }
              ... on AutoRebaseEnabledEvent {
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
                enabler {
                  login
                  name
                }
                id
              }
              ... on AutoSquashEnabledEvent {
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
                enabler {
                  login
                  name
                }
                id
              }
              ... on AutomaticBaseChangeFailedEvent {
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
                newBase
                oldBase
              }
              ... on AutomaticBaseChangeSucceededEvent {
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
                newBase
                oldBase
              }
              ... on BaseRefChangedEvent {
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
                currentRefName
                id
                previousRefName
              }
              ... on BaseRefDeletedEvent {
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
                baseRefName
                createdAt
                id
              }
              ... on BaseRefForcePushedEvent {
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
              ... on BlockedByAddedEvent {
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
                blockingIssue {
                  number
                }
                createdAt
                id
              }
              ... on BlockedByRemovedEvent {
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
                blockingIssue {
                  number
                }
                createdAt
                id
              }
              ... on BlockingAddedEvent {
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
                blockedIssue {
                  number
                }
                createdAt
                id
              }
              ... on BlockingRemovedEvent {
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
                blockedIssue {
                  number
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
              ... on CommentDeletedEvent {
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
                deletedCommentAuthor {
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
                id
              }
              ... on ConnectedEvent {
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
                source {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
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
              ... on ConvertedFromDraftEvent {
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
                project {
                  number
                }
                wasAutomated
              }
              ... on ConvertedNoteToIssueEvent {
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
                projectColumnName
              }
              ... on ConvertedToDiscussionEvent {
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
                discussion {
                  number
                }
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
              ... on DemilestonedEvent {
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
                milestoneTitle
              }
              ... on DeployedEvent {
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
                ref {
                  name
                }
              }
              ... on DeploymentEnvironmentChangedEvent {
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
              ... on DisconnectedEvent {
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
                source {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
              }
              ... on HeadRefDeletedEvent {
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
                headRef {
                  name
                }
                headRefName
                id
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
              ... on HeadRefRestoredEvent {
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
              ... on IssueCommentPinnedEvent {
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
              ... on IssueCommentUnpinnedEvent {
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
              ... on IssueFieldAddedEvent {
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
                color
                createdAt
                id
                issueField {
                  __typename
                  ... on IssueFieldDate {
                    name
                  }
                  ... on IssueFieldMultiSelect {
                    name
                  }
                  ... on IssueFieldNumber {
                    name
                  }
                  ... on IssueFieldSingleSelect {
                    name
                  }
                  ... on IssueFieldText {
                    name
                  }
                }
                options {
                  name
                }
                value
              }
              ... on IssueFieldChangedEvent {
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
                issueField {
                  __typename
                  ... on IssueFieldDate {
                    name
                  }
                  ... on IssueFieldMultiSelect {
                    name
                  }
                  ... on IssueFieldNumber {
                    name
                  }
                  ... on IssueFieldSingleSelect {
                    name
                  }
                  ... on IssueFieldText {
                    name
                  }
                }
                newColor
                newOptions {
                  name
                }
                newValue
                previousColor
                previousOptions {
                  name
                }
                previousValue
              }
              ... on IssueFieldRemovedEvent {
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
                issueField {
                  __typename
                  ... on IssueFieldDate {
                    name
                  }
                  ... on IssueFieldMultiSelect {
                    name
                  }
                  ... on IssueFieldNumber {
                    name
                  }
                  ... on IssueFieldSingleSelect {
                    name
                  }
                  ... on IssueFieldText {
                    name
                  }
                }
                options {
                  name
                }
              }
              ... on IssueTypeAddedEvent {
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
                issueType {
                  name
                }
              }
              ... on IssueTypeChangedEvent {
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
                issueType {
                  name
                }
                prevIssueType {
                  name
                }
              }
              ... on IssueTypeRemovedEvent {
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
                issueType {
                  name
                }
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
              ... on LockedEvent {
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
                lockReason
              }
              ... on MarkedAsDuplicateEvent {
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
                canonical {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                createdAt
                duplicate {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                id
                isCrossRepository
              }
              ... on MentionedEvent {
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
              ... on MilestonedEvent {
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
                milestoneTitle
              }
              ... on MovedColumnsInProjectEvent {
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
              ... on ParentIssueAddedEvent {
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
                parent {
                  number
                }
              }
              ... on ParentIssueRemovedEvent {
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
                parent {
                  number
                }
              }
              ... on PinnedEvent {
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
              ... on ProjectV2ItemStatusChangedEvent {
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
                previousStatus
                project {
                  number
                }
                status
                wasAutomated
              }
              ... on PullRequestCommit {
                pullRequestCommit_commit: commit {
                  oid
                  abbreviatedOid
                }
                id
              }
              ... on PullRequestCommitCommentThread {
                pullRequestCommitCommentThread_commit: commit {
                  oid
                  abbreviatedOid
                }
                id
                pullRequestCommitCommentThread_path: path
                position
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
              ... on PullRequestReviewThread {
                diffSide
                id
                isCollapsed
                isOutdated
                isResolved
                line
                originalLine
                originalStartLine
                pullRequestReviewThread_path: path
                resolvedBy {
                  login
                  name
                }
                startDiffSide
                startLine
                subjectType
                viewerCanReply
                viewerCanResolve
                viewerCanUnresolve
              }
              ... on PullRequestRevisionMarker {
                createdAt
                lastSeenCommit {
                  oid
                  abbreviatedOid
                }
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
              ... on ReferencedEvent {
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
                referencedEvent_commit: commit {
                  oid
                  abbreviatedOid
                }
                commitRepository {
                  name
                }
                createdAt
                id
                isCrossRepository
                isDirectReference
              }
              ... on RemovedFromMergeQueueEvent {
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
                beforeCommit {
                  oid
                  abbreviatedOid
                }
                createdAt
                enqueuer {
                  login
                  name
                }
                id
                reason
              }
              ... on RemovedFromProjectEvent {
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
              ... on RemovedFromProjectV2Event {
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
                project {
                  number
                }
                wasAutomated
              }
              ... on RenamedTitleEvent {
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
                currentTitle
                id
                previousTitle
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
              ... on SubIssueAddedEvent {
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
                subIssue {
                  number
                }
              }
              ... on SubIssueRemovedEvent {
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
                subIssue {
                  number
                }
              }
              ... on SubscribedEvent {
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
              ... on TransferredEvent {
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
                fromRepository {
                  name
                }
                id
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
              ... on UnlockedEvent {
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
              ... on UnmarkedAsDuplicateEvent {
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
                canonical {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                createdAt
                duplicate {
                  __typename
                  ... on Issue {
                    number
                  }
                  ... on PullRequest {
                    number
                  }
                }
                id
                isCrossRepository
              }
              ... on UnpinnedEvent {
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
              ... on UnsubscribedEvent {
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
              ... on UserBlockedEvent {
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
                blockDuration
                createdAt
                id
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
