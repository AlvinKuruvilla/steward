"""JSON for the interface, and the interface's own files.

Every response carries the derivation class alongside the state. A caller that
cannot tell an EVENT from a POLICY from an UNKNOWN cannot render the difference,
and the difference is the product.
"""

from __future__ import annotations

import os
import sqlite3
from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager, closing, contextmanager
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from githubkit import GitHub
from githubkit.exception import RequestFailed
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import RedirectResponse, Response
from starlette.types import Scope

from steward import sync
from steward.migrate import DATABASE, apply, connect, default_data_dir
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
    with closing(connect(_database())) as conn:
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


def _database() -> Path:
    """The database file. `steward serve` sets the directory before starting."""
    return Path(os.environ.get("STEWARD_DATA_DIR") or default_data_dir()) / DATABASE


@contextmanager
def _connect() -> Iterator[sqlite3.Connection]:
    """A connection for one request, closed when it ends.

    Opened per request rather than shared: a sqlite3 read holds its snapshot
    until the transaction ends, and a connection kept open across requests
    would keep the write-ahead log from ever being checkpointed.
    """
    with closing(connect(_database())) as conn:
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


# Avatars, by login, because a login is all the log stores.
#
# `github.com/<login>.png` covers people and not GitHub Apps: an app's login
# carries a `[bot]` suffix that belongs to no account, and `github-actions` has
# no user page at all. `GET /users/<login>` answers for every kind of account,
# and it needs the token this process already holds. An organisation answers
# there too: a repository has no picture of its own, so its owner's stands in.
#
# A login that resolves to nothing is stored as `None`, so a deleted author
# costs one lookup and not one per render. Membership is the test for a hit;
# `.get` cannot tell a miss from a known-miss. Nothing expires, so an account
# created after Steward asked stays missing until restart.
_avatars: dict[str, str | None] = {}

# Unsized, the CDN sends the whole upload: 22KB where `s=40` is 1.6KB, for an
# image drawn into a 20-pixel circle (avatars.githubusercontent.com,
# 2026-09-22). Nothing renders above 22 CSS pixels, so 64 is crisp at 2x and
# soft at 3x; going higher is paid on every row of the inbox. One size for
# every caller: one entry per login here, one URL per login in the browser.
_AVATAR_PIXELS = 64


def _sized(url: str, pixels: int) -> str:
    """Return `url` with GitHub's `s` parameter set, preserving the rest."""
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query["s"] = str(pixels)
    return urlunsplit(parts._replace(query=urlencode(query)))


@app.get("/api/avatars/{login}")
async def get_avatar(login: str) -> RedirectResponse:
    """Redirect to an account's avatar, whatever kind of account it is."""
    if login not in _avatars:
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise HTTPException(500, "GITHUB_TOKEN is not set")
        try:
            async with GitHub(token) as gh:
                account = await gh.rest.users.async_get_by_username(username=login)
        except RequestFailed as failed:
            # Only a 404 is about the account. A 403 is the rate limit and
            # a 401 a bad token; caching either would blank that face until
            # restart over something that clears on its own.
            if failed.response.status_code == 404:
                _avatars[login] = None
            raise HTTPException(404, f"no account named {login}") from failed
        _avatars[login] = _sized(account.parsed_data.avatar_url, _AVATAR_PIXELS)

    known = _avatars[login]
    if known is None:
        raise HTTPException(404, f"no account named {login}")

    # Cached hard: an avatar moves rarely, and the browser asking once per
    # login per day is the difference between this and a rate limit.
    return RedirectResponse(
        known, status_code=307, headers={"cache-control": "public, max-age=86400"}
    )


# Label colours, by repository. The log stores a label's name and nothing else,
# and GitHub recolours a label everywhere the moment it is edited, so the colour
# a chip should carry is the repository's current one rather than whichever hex
# rode along on the event. That is a property of the repository, so it is
# fetched per repository and not folded.
_labels: dict[tuple[str, str], dict[str, str]] = {}


@app.get("/api/repositories/{owner}/{name}/labels")
async def get_labels(owner: str, name: str) -> dict[str, str]:
    """Every label the repository defines, name to six-digit hex, no `#`."""
    known = _labels.get((owner, name))
    if known is None:
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise HTTPException(500, "GITHUB_TOKEN is not set")
        try:
            async with GitHub(token) as gh:
                pages = gh.rest.paginate(
                    gh.rest.issues.async_list_labels_for_repo,
                    owner=owner,
                    repo=name,
                    per_page=100,
                )
                known = {label.name: label.color async for label in pages}
        except RequestFailed as failed:
            raise HTTPException(
                404, f"cannot read labels for {owner}/{name}"
            ) from failed
        _labels[(owner, name)] = known

    # A label that no longer exists keeps no colour here; the interface falls
    # back to a neutral chip rather than inventing one.
    return known


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
    state = sync.start(body.owner, body.name, token=token, database=_database())
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
