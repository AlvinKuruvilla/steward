"""Reading a repository from GitHub."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from typing import Any

from githubkit import GitHub
from githubkit_schemas.latest.models import PullRequestSimple

from steward.model import Event
from steward.normalize import events_for_pull_request

# GitHub's maximum.
PAGE = 100

# GitHub allows 900 points a minute against REST and a GET is one point, so the
# ceiling is 15 requests a second. A backfill measured 0.48s per request, and
# 15 * 0.48 is roughly seven in flight to reach that ceiling. Five leaves
# headroom, and githubkit's auto_retry backs off if the estimate is wrong.
#
# GitHub also advises making requests serially. That advice exists to keep
# clients under these limits, which the arithmetic above already does.
CONCURRENCY = 5


async def pull_requests(
    gh: GitHub[Any], owner: str, repo: str
) -> AsyncIterator[PullRequestSimple]:
    # state="all": a closed pull request's history is as much of the log as an
    # open one's.
    # The paginator's element type does not survive the overload, so the loop
    # variables below are annotated rather than inferred.
    pr: PullRequestSimple
    async for pr in gh.rest.paginate(
        gh.rest.pulls.async_list,
        owner=owner,
        repo=repo,
        state="all",
        per_page=PAGE,
    ):
        yield pr


async def timeline(gh: GitHub[Any], owner: str, repo: str, number: int) -> list[object]:
    items: list[object] = []
    item: object
    async for item in gh.rest.paginate(
        gh.rest.issues.async_list_events_for_timeline,
        owner=owner,
        repo=repo,
        issue_number=number,
        per_page=PAGE,
    ):
        items.append(item)
    return items


async def events(
    gh: GitHub[Any], owner: str, repo: str, *, concurrency: int = CONCURRENCY
) -> AsyncIterator[list[Event]]:
    """Every event in the repository, a pull request at a time."""

    async def one(pr: PullRequestSimple) -> list[Event]:
        return events_for_pull_request(pr, await timeline(gh, owner, repo, pr.number))

    # A batch at a time, so a repository's history never has to be in memory at
    # once and the caller can write as it goes.
    batch: list[PullRequestSimple] = []
    async for pr in pull_requests(gh, owner, repo):
        batch.append(pr)
        if len(batch) == concurrency:
            for found in await asyncio.gather(*map(one, batch)):
                yield found
            batch = []
    for found in await asyncio.gather(*map(one, batch)):
        yield found
