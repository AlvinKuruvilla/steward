"""Writing events to the log, and reading them back.

Inserts are idempotent through the unique key on `events`. A second sync of the
same repository adds nothing.

Timestamps cross into SQLite as UTC text in the one shape the schema accepts,
`2026-09-23T14:05:00Z`, and come back as aware datetimes. The conversion is
written out here rather than registered as a sqlite3 adapter: Python 3.12
deprecated the default adapters, and a registered one is global to the process.
"""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Iterable
from datetime import UTC, datetime

from steward.model import (
    ActorType,
    Event,
    EventKind,
    SubjectType,
    payload_from_dict,
    payload_to_dict,
)

INSERT = """
INSERT INTO events (
    repo_id, subject_type, subject_number, kind, occurred_at,
    actor, actor_type, payload, source_id
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT (repo_id, subject_type, subject_number, source_id) DO NOTHING
"""


def _timestamp(moment: datetime) -> str:
    # GitHub reports whole seconds. A fractional second or a naive datetime
    # means something upstream changed, and truncating it would reorder events
    # that share a second without anyone seeing why.
    if moment.tzinfo is None:
        raise ValueError(f"{moment} has no timezone; the log stores UTC")
    if moment.microsecond:
        raise ValueError(f"{moment} has a fractional second; the log stores seconds")
    return moment.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _moment(stored: str) -> datetime:
    return datetime.fromisoformat(stored)


def repository_id(conn: sqlite3.Connection, owner: str, name: str, node_id: str) -> int:
    """The id of this repository's row, inserting it the first time."""
    with conn:
        row = conn.execute(
            "INSERT INTO repositories (owner, name, node_id) VALUES (?, ?, ?) "
            "ON CONFLICT (owner, name) DO UPDATE SET node_id = excluded.node_id "
            "RETURNING id",
            (owner, name, node_id),
        ).fetchone()
    assert row is not None, "RETURNING id yields a row"
    return int(row[0])


def write(
    conn: sqlite3.Connection, repo_id: int, events: Iterable[Event]
) -> tuple[int, int]:
    """Write events, returning how many were new and how many were already there."""
    rows = [
        (
            repo_id,
            event.subject_type.value,
            event.subject_number,
            event.kind.value,
            _timestamp(event.occurred_at),
            event.actor,
            event.actor_type.value if event.actor_type else None,
            # Sorted and compact, so the same payload is always the same bytes.
            json.dumps(
                payload_to_dict(event.payload), sort_keys=True, separators=(",", ":")
            ),
            event.source_id,
        )
        for event in events
    ]
    with conn:
        # executemany sums rowcount across the batch, and a row the unique key
        # turned away counts zero.
        new = conn.executemany(INSERT, rows).rowcount
    return new, len(rows) - new


def record_sync(conn: sqlite3.Connection, repo_id: int) -> None:
    with conn:
        conn.execute(
            "UPDATE repositories SET last_sync = strftime('%Y-%m-%dT%H:%M:%SZ', 'now') "
            "WHERE id = ?",
            (repo_id,),
        )


SELECT_EVENTS = """
SELECT e.subject_number, e.kind, e.occurred_at, e.source_id,
       e.actor, e.actor_type, e.payload
FROM events e
JOIN repositories r ON r.id = e.repo_id
WHERE r.owner = ? AND r.name = ? AND e.subject_type = ?
"""


def read_events(
    conn: sqlite3.Connection,
    owner: str,
    name: str,
    *,
    subject_type: SubjectType = SubjectType.PULL_REQUEST,
    number: int | None = None,
) -> dict[int, list[Event]]:
    """Every stored event for a repository, grouped by subject number."""
    sql = SELECT_EVENTS
    params: tuple[object, ...] = (owner, name, subject_type.value)
    if number is not None:
        sql += " AND e.subject_number = ?"
        params += (number,)

    grouped: dict[int, list[Event]] = {}
    for row in conn.execute(sql, params).fetchall():
        subject_number, kind, occurred_at, source_id, actor, actor_type, payload = row
        grouped.setdefault(subject_number, []).append(
            Event(
                subject_type=subject_type,
                subject_number=subject_number,
                kind=EventKind(kind),
                occurred_at=_moment(occurred_at),
                source_id=source_id,
                actor=actor,
                actor_type=ActorType(actor_type) if actor_type else None,
                payload=payload_from_dict(EventKind(kind), json.loads(payload)),
            )
        )
    return grouped


def repositories(conn: sqlite3.Connection) -> list[tuple[str, str, datetime | None]]:
    """Every synced repository, with when it was last read."""
    return [
        (owner, name, _moment(last_sync) if last_sync else None)
        for owner, name, last_sync in conn.execute(
            "SELECT owner, name, last_sync FROM repositories ORDER BY owner, name"
        ).fetchall()
    ]
