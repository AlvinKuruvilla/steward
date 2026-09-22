"""The command line.

Three commands, and two connection strings. `migrate` uses
`STEWARD_ADMIN_DATABASE_URL`, which carries `role=steward_owner`; everything
else uses `STEWARD_DATABASE_URL`, which is the engine and cannot create tables.
"""

from __future__ import annotations

import os
import sys
from typing import Annotated, Any

import psycopg
import typer
from githubkit import GitHub

from steward import fetch, store
from steward.migrate import apply
from steward.model import EventKind

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="A workbench for running an open-source repository.",
)


def _require(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise typer.BadParameter(f"{name} is not set", param_hint=name)
    return value


def _split(repository: str) -> tuple[str, str]:
    owner, _, name = repository.partition("/")
    if not owner or not name:
        raise typer.BadParameter(f"expected owner/repo, got {repository!r}")
    return owner, name


def _connect(url: str) -> psycopg.Connection[Any]:
    try:
        return psycopg.connect(url)
    except psycopg.OperationalError as err:
        raise typer.Exit(2) from err


@app.command()
def migrate() -> None:
    """Apply any migrations the database has not seen."""
    with _connect(_require("STEWARD_ADMIN_DATABASE_URL")) as conn:
        applied = apply(conn)
    for migration in applied:
        typer.echo(f"applied {migration.version:04d}_{migration.name}")
    if not applied:
        typer.echo("up to date")


@app.command()
def sync(repository: Annotated[str, typer.Argument(help="owner/repo")]) -> None:
    """Read a repository's pull request history into the log."""
    owner, name = _split(repository)
    gh: GitHub[Any] = GitHub(_require("GITHUB_TOKEN"))
    node_id = gh.rest.repos.get(owner=owner, repo=name).parsed_data.node_id

    with _connect(_require("STEWARD_DATABASE_URL")) as conn:
        repo_id = store.repository_id(conn, owner, name, node_id)
        new, seen = store.write(conn, repo_id, fetch.events(gh, owner, name))
        store.record_sync(conn, repo_id)
    typer.echo(f"{repository}: {new} new, {seen} already recorded")


@app.command()
def events(
    repository: Annotated[str, typer.Argument(help="owner/repo")],
    number: Annotated[int, typer.Argument(help="pull request number")],
) -> None:
    """Print one pull request's event stream, oldest first."""
    owner, name = _split(repository)
    with _connect(_require("STEWARD_DATABASE_URL")) as conn:
        rows = conn.execute(
            "SELECT e.occurred_at, e.kind, e.actor, e.payload "
            "FROM events e JOIN repositories r ON r.id = e.repo_id "
            "WHERE r.owner = %s AND r.name = %s "
            "AND e.subject_type = 'pull_request' AND e.subject_number = %s "
            "ORDER BY e.occurred_at, e.kind <> %s",
            (owner, name, number, EventKind.OPENED.value),
        ).fetchall()

    if not rows:
        typer.echo(f"no events for {repository}#{number}", err=True)
        raise typer.Exit(1)
    for occurred_at, kind, actor, payload in rows:
        detail = " ".join(f"{k}={v}" for k, v in sorted(payload.items()))
        typer.echo(
            f"{occurred_at:%Y-%m-%d %H:%M}  {kind:<22} {actor or '-':<20} {detail}"
        )


def main(argv: list[str] | None = None) -> int:
    """Run the application and return a process exit code."""
    args = sys.argv[1:] if argv is None else argv
    try:
        app(args=args)
    except SystemExit as exit_:
        return int(exit_.code or 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
