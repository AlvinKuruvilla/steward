"""Reading a repository into the log, and saying how far it got.

Both the CLI and the API call `run`. The API also has to answer "is it still
going", so progress is kept here rather than in either caller.
"""

from __future__ import annotations

import asyncio
from contextlib import closing
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from githubkit import GitHub
from githubkit.throttling import LocalThrottler

from steward import fetch, store
from steward.migrate import connect


@dataclass
class Progress:
    """How a sync is going, for a caller that cannot watch it."""

    owner: str
    name: str
    started_at: datetime
    pull_requests: int = 0
    new: int = 0
    seen: int = 0
    finished_at: datetime | None = None
    error: str | None = None

    @property
    def running(self) -> bool:
        return self.finished_at is None


# Keyed by repository, so a second request for one already syncing joins the
# first rather than starting a competing read of the same history.
_progress: dict[tuple[str, str], Progress] = {}
_tasks: dict[tuple[str, str], asyncio.Task[Progress]] = {}


def progress(owner: str, name: str) -> Progress | None:
    return _progress.get((owner, name))


def everything() -> list[Progress]:
    return list(_progress.values())


async def run(owner: str, name: str, *, token: str, database: Path) -> Progress:
    """Read a repository's history into the log, start to finish."""
    state = _progress.setdefault(
        (owner, name), Progress(owner=owner, name=name, started_at=datetime.now(UTC))
    )
    try:
        async with GitHub(token, throttler=LocalThrottler(fetch.CONCURRENCY)) as gh:
            repository = await gh.rest.repos.async_get(owner=owner, repo=name)
            # closing(), not the connection's own `with`: on sqlite3 that
            # commits and leaves the connection open.
            with closing(connect(database)) as conn:
                repo_id = store.repository_id(
                    conn, owner, name, repository.parsed_data.node_id
                )
                async for events in fetch.events(gh, owner, name):
                    added, already = store.write(conn, repo_id, events)
                    state.pull_requests += 1
                    state.new += added
                    state.seen += already
                store.record_sync(conn, repo_id)
    # Recorded on the progress rather than raised: the caller is a background
    # task, and a traceback nobody sees is worse than a message in the UI.
    except Exception as err:
        state.error = f"{type(err).__name__}: {err}"
    finally:
        state.finished_at = datetime.now(UTC)
    return state


def start(owner: str, name: str, *, token: str, database: Path) -> Progress:
    """Begin a sync in the background, or return the one already running."""
    key = (owner, name)
    existing = _progress.get(key)
    if existing is not None and existing.running:
        return existing

    state = Progress(owner=owner, name=name, started_at=datetime.now(UTC))
    _progress[key] = state
    _tasks[key] = asyncio.create_task(run(owner, name, token=token, database=database))
    return state
