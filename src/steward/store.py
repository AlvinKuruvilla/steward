"""Writing events to the log.

Inserts are idempotent through the unique key on `events`. A second sync of the
same repository adds nothing.
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import datetime
from typing import Any

import psycopg
from psycopg.types.json import Json

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
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (repo_id, subject_type, subject_number, source_id) DO NOTHING
"""


def repository_id(
    conn: psycopg.Connection[Any], owner: str, name: str, node_id: str
) -> int:
    """The id of this repository's row, inserting it the first time."""
    with conn.transaction():
        row = conn.execute(
            "INSERT INTO repositories (owner, name, node_id) VALUES (%s, %s, %s) "
            "ON CONFLICT (owner, name) DO UPDATE SET node_id = EXCLUDED.node_id "
            "RETURNING id",
            (owner, name, node_id),
        ).fetchone()
    assert row is not None, "RETURNING id yields a row"
    return int(row[0])


def write(
    conn: psycopg.Connection[Any], repo_id: int, events: Iterable[Event]
) -> tuple[int, int]:
    """Write events, returning how many were new and how many were already there."""
    new = seen = 0
    with conn.transaction(), conn.cursor() as cur:
        for event in events:
            cur.execute(
                INSERT,
                (
                    repo_id,
                    event.subject_type.value,
                    event.subject_number,
                    event.kind.value,
                    event.occurred_at,
                    event.actor,
                    event.actor_type.value if event.actor_type else None,
                    Json(payload_to_dict(event.payload)),
                    event.source_id,
                ),
            )
            if cur.rowcount:
                new += 1
            else:
                seen += 1
    return new, seen


def record_sync(conn: psycopg.Connection[Any], repo_id: int) -> None:
    with conn.transaction():
        conn.execute(
            "UPDATE repositories SET last_sync = now() WHERE id = %s", (repo_id,)
        )


SELECT_EVENTS = """
SELECT e.subject_number, e.kind, e.occurred_at, e.source_id,
       e.actor, e.actor_type, e.payload
FROM events e
JOIN repositories r ON r.id = e.repo_id
WHERE r.owner = %s AND r.name = %s AND e.subject_type = %s
"""


def read_events(
    conn: psycopg.Connection[Any],
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
        sql += " AND e.subject_number = %s"
        params += (number,)

    grouped: dict[int, list[Event]] = {}
    for row in conn.execute(sql, params).fetchall():
        subject_number, kind, occurred_at, source_id, actor, actor_type, payload = row
        grouped.setdefault(subject_number, []).append(
            Event(
                subject_type=subject_type,
                subject_number=subject_number,
                kind=EventKind(kind),
                occurred_at=occurred_at,
                source_id=source_id,
                actor=actor,
                actor_type=ActorType(actor_type) if actor_type else None,
                payload=payload_from_dict(EventKind(kind), payload),
            )
        )
    return grouped


def repositories(
    conn: psycopg.Connection[Any],
) -> list[tuple[str, str, datetime | None]]:
    """Every synced repository, with when it was last read."""
    return [
        (owner, name, last_sync)
        for owner, name, last_sync in conn.execute(
            "SELECT owner, name, last_sync FROM repositories ORDER BY owner, name"
        ).fetchall()
    ]
