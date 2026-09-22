"""JSON for the interface, and the interface's own files.

Every response carries the derivation class alongside the state. A caller that
cannot tell an EVENT from a POLICY from an UNKNOWN cannot render the difference,
and the difference is the product.
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any

import psycopg
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import Response
from starlette.types import Scope

from steward import sync
from steward.migrate import apply
from steward.model import Event, payload_to_dict
from steward.state import (
    BlockedOn,
    Derivation,
    WorkflowState,
    current,
    fold,
    summarise,
)
from steward.store import read_events, repositories


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Bring the schema up to date, so starting the app is the whole install."""
    admin = os.environ.get("STEWARD_ADMIN_DATABASE_URL")
    if admin:
        with psycopg.connect(admin) as conn:
            for migration in apply(conn):
                print(f"applied {migration.version:04d}_{migration.name}")
    yield


app = FastAPI(
    title="Steward",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)


class Repository(BaseModel):
    """A repository the log holds events for."""

    owner: str
    name: str
    last_sync: datetime | None
    syncing: bool = False
    pull_requests_read: int = 0
    sync_error: str | None = None


class AddRepository(BaseModel):
    owner: str
    name: str


class Standing(BaseModel):
    """Where a pull request is, what put it there, and what it is about."""

    number: int
    title: str | None
    state: WorkflowState
    blocked_on: BlockedOn
    derivation: Derivation
    since: datetime
    author: str | None
    author_is_bot: bool
    labels: list[str]
    comments: int
    last_kind: str | None
    last_actor: str | None
    last_at: datetime | None


class Moment(BaseModel):
    """One event, as evidence."""

    kind: str
    occurred_at: datetime
    actor: str | None
    payload: dict[str, str | int | bool]


class Episode(BaseModel):
    """One stretch of a pull request's life, in one state.

    The last episode of a pull request has no end, whether it is still running
    or was merged or closed.
    """

    start: datetime
    end: datetime | None
    state: WorkflowState
    blocked_on: BlockedOn
    derivation: Derivation


class PullRequest(BaseModel):
    """Where a pull request stands, how it got there, and the evidence."""

    standing: Standing
    episodes: list[Episode]
    events: list[Moment]


@contextmanager
def _connect() -> Iterator[psycopg.Connection[Any]]:
    """The engine's connection, which can read the log and not create tables."""
    url = os.environ.get("STEWARD_DATABASE_URL")
    if not url:
        raise HTTPException(500, "STEWARD_DATABASE_URL is not set")
    with psycopg.connect(url) as conn:
        yield conn


def _standing(number: int, events: list[Event]) -> Standing | None:
    """One row of the queue, every field of it folded from the log."""
    now = current(events)
    if now is None:
        return None
    about = summarise(events)
    return Standing(
        number=number,
        title=about.title,
        state=now.state,
        blocked_on=now.blocked_on,
        derivation=now.derivation,
        since=now.start,
        author=about.author,
        author_is_bot=about.author_is_bot,
        labels=list(about.labels),
        comments=about.comments,
        last_kind=about.last_kind.value if about.last_kind else None,
        last_actor=about.last_actor,
        last_at=about.last_at,
    )


@app.get("/api/repositories")
def get_repositories() -> list[Repository]:
    """Every repository that has been synced, and any sync now running."""
    with _connect() as conn:
        known = repositories(conn)

    rows = {
        (owner, name): Repository(owner=owner, name=name, last_sync=last_sync)
        for owner, name, last_sync in known
    }
    # A repository being read for the first time has no row yet, so the
    # in-flight syncs are folded in rather than looked up.
    for state in sync.everything():
        row = rows.setdefault(
            (state.owner, state.name),
            Repository(owner=state.owner, name=state.name, last_sync=None),
        )
        row.syncing = state.running
        row.pull_requests_read = state.pull_requests
        row.sync_error = state.error
    return sorted(rows.values(), key=lambda r: (r.owner, r.name))


# async, because starting the sync needs the running event loop that FastAPI
# gives an async endpoint and not the threadpool it gives a sync one.
@app.post("/api/repositories", status_code=202)
async def add_repository(body: AddRepository) -> Repository:
    """Start reading a repository's history. Returns before it finishes."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise HTTPException(500, "GITHUB_TOKEN is not set")
    database_url = os.environ.get("STEWARD_DATABASE_URL")
    if not database_url:
        raise HTTPException(500, "STEWARD_DATABASE_URL is not set")

    state = sync.start(body.owner, body.name, token=token, database_url=database_url)
    return Repository(
        owner=state.owner,
        name=state.name,
        last_sync=None,
        syncing=state.running,
        pull_requests_read=state.pull_requests,
        sync_error=state.error,
    )


@app.get("/api/repositories/{owner}/{name}/pulls")
def get_pulls(owner: str, name: str, open_only: bool = True) -> list[Standing]:
    """Every pull request's standing, most recently moved first."""
    with _connect() as conn:
        grouped = read_events(conn, owner, name)
    if not grouped:
        raise HTTPException(404, f"{owner}/{name} has no events; sync it first")

    standings = []
    for number, events in grouped.items():
        standing = _standing(number, events)
        if standing is None:
            continue
        if open_only and standing.state in (
            WorkflowState.MERGED,
            WorkflowState.CLOSED,
        ):
            continue
        standings.append(standing)
    # Stalest first. A queue is read from the top, and the thing that has been
    # waiting longest is the thing most likely to have been forgotten.
    return sorted(standings, key=lambda s: s.since)


@app.get("/api/repositories/{owner}/{name}/pulls/{number}")
def get_pull(owner: str, name: str, number: int) -> PullRequest:
    """One pull request: its standing, every episode, and every event."""
    with _connect() as conn:
        grouped = read_events(conn, owner, name, number=number)
    events = grouped.get(number)
    if not events:
        raise HTTPException(404, f"no events for {owner}/{name}#{number}")

    standing = _standing(number, events)
    assert standing is not None, "events exist, so an interval does"
    return PullRequest(
        standing=standing,
        episodes=[
            Episode(
                start=i.start,
                end=i.end,
                state=i.state,
                blocked_on=i.blocked_on,
                derivation=i.derivation,
            )
            for i in fold(events)
        ],
        events=[
            Moment(
                kind=e.kind.value,
                occurred_at=e.occurred_at,
                actor=e.actor,
                payload=payload_to_dict(e.payload),
            )
            for e in sorted(events, key=lambda e: e.occurred_at)
        ],
    )


class Interface(StaticFiles):
    """The built interface, with client-side routes falling back to index.html.

    Routing lives in the browser, so /bots is not a file and never will be.
    """

    async def get_response(self, path: str, scope: Scope) -> Response:
        try:
            return await super().get_response(path, scope)
        except StarletteHTTPException as missing:
            if missing.status_code != 404:
                raise
            return await super().get_response("index.html", scope)


# Mounted last, so every /api route is matched first.
_built = Path(__file__).parent / "web"
if _built.is_dir():
    app.mount("/", Interface(directory=_built, html=True), name="web")
