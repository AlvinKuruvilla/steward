"""Reading a repository from GitHub.

Every collection is paged, and githubkit follows the `Link` headers. A page that
comes back full does not mean there is nothing after it.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from githubkit import GitHub
from githubkit_schemas.latest.models import PullRequestSimple

from steward.model import Event
from steward.normalize import events_for_pull_request

# GitHub's maximum.
PAGE = 100


def pull_requests(
    gh: GitHub[Any], owner: str, repo: str
) -> Iterator[PullRequestSimple]:
    """Every pull request in the repository, newest first.

    `state="all"`: a closed pull request's history is as much of the log as an
    open one's.
    """
    yield from gh.rest.paginate(
        gh.rest.pulls.list,
        owner=owner,
        repo=repo,
        state="all",
        per_page=PAGE,
    )


def timeline(gh: GitHub[Any], owner: str, repo: str, number: int) -> Iterator[Any]:
    """Every timeline item on one pull request, oldest first."""
    yield from gh.rest.paginate(
        gh.rest.issues.list_events_for_timeline,
        owner=owner,
        repo=repo,
        issue_number=number,
        per_page=PAGE,
    )


def events(gh: GitHub[Any], owner: str, repo: str) -> Iterator[Event]:
    """Every event in the repository, a pull request at a time."""
    for pr in pull_requests(gh, owner, repo):
        yield from events_for_pull_request(pr, timeline(gh, owner, repo, pr.number))
