"""The migration runner and the connection it runs on.

Each test gets a fresh database file under `tmp_path`, so nothing here can touch
a database a developer has synced into.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from pathlib import Path

import pytest

import steward.migrate
from steward.migrate import Migration, MigrationError, apply, connect, migrations


@pytest.fixture
def conn(tmp_path: Path) -> Iterator[sqlite3.Connection]:
    conn = connect(tmp_path / "steward.db")
    yield conn
    conn.close()


def _tables(conn: sqlite3.Connection) -> set[str]:
    return {
        row[0]
        for row in conn.execute(
            "SELECT name FROM sqlite_schema "
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
        )
    }


def test_migrations_are_numbered_and_ordered() -> None:
    found = migrations()
    assert found, "no migrations in the package"
    assert [m.version for m in found] == sorted(m.version for m in found)
    assert found[0].version == 1


def test_apply_creates_the_schema(conn: sqlite3.Connection) -> None:
    ran = apply(conn)

    assert [m.version for m in ran] == [m.version for m in migrations()]
    assert _tables(conn) == {"events", "repositories", "schema_migrations"}


def test_apply_is_idempotent(conn: sqlite3.Connection) -> None:
    apply(conn)
    assert apply(conn) == []


def test_connect_turns_on_what_sqlite_leaves_off(conn: sqlite3.Connection) -> None:
    # Both are per-connection or per-file settings that SQLite defaults the
    # other way, and both are silently skipped if set inside a transaction.
    assert conn.execute("PRAGMA foreign_keys").fetchone() == (1,)
    assert conn.execute("PRAGMA journal_mode").fetchone() == ("wal",)


def test_attach_is_refused(conn: sqlite3.Connection, tmp_path: Path) -> None:
    # The engine's side of the enrichment boundary in 0001-llm-boundary.md.
    with pytest.raises(sqlite3.DatabaseError, match="not authorized"):
        conn.execute("ATTACH ? AS enrichment", (str(tmp_path / "enrichment.db"),))


def test_a_failed_migration_leaves_nothing_behind(
    conn: sqlite3.Connection, monkeypatch: pytest.MonkeyPatch
) -> None:
    # executescript() and a transaction interact differently in each of
    # sqlite3's autocommit modes; in the wrong one, the table created before the
    # failure survives and the next run trips over it.
    broken = Migration(
        1, "broken", "CREATE TABLE half (id INTEGER); INSERT INTO missing VALUES (1);"
    )
    monkeypatch.setattr(steward.migrate, "migrations", lambda: [broken])

    with pytest.raises(sqlite3.OperationalError, match="no such table: missing"):
        apply(conn)

    assert _tables(conn) == {"schema_migrations"}
    assert conn.execute("SELECT count(*) FROM schema_migrations").fetchone() == (0,)


def test_an_edited_migration_is_refused(conn: sqlite3.Connection) -> None:
    apply(conn)
    conn.execute("UPDATE schema_migrations SET checksum = 'tampered'")
    conn.commit()
    with pytest.raises(MigrationError, match="has changed since it was applied"):
        apply(conn)


def test_a_migration_the_build_lacks_is_refused(conn: sqlite3.Connection) -> None:
    apply(conn)
    conn.execute(
        "INSERT INTO schema_migrations (version, name, checksum) "
        "VALUES (9999, 'from_the_future', 'x')"
    )
    conn.commit()
    with pytest.raises(MigrationError, match="migrations this build does not"):
        apply(conn)
