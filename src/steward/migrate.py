"""Opening the database, and applying the schema, forward only.

Migrations are numbered SQL files inside the package, so an installed wheel
carries them. Each runs in its own transaction and is recorded in
`schema_migrations` with a checksum of what ran.

Every connection comes from `connect`, so every connection has foreign keys on,
the write-ahead log, and the authorizer that keeps enrichment out of reach.
"""

from __future__ import annotations

import hashlib
import os
import re
import sqlite3
import sys
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

FILENAME = re.compile(r"^(\d{4})_([a-z0-9_]+)\.sql$")

# Tauri's bundle identifier. It names the directory the database lives in, so
# changing it strands every existing install's data.
IDENTIFIER = "dev.steward.app"

DATABASE = "steward.db"

# How long a write waits for another writer before raising "database is
# locked". Arbitrary: long enough to outlast one pull request's batch of
# inserts, short enough that a stuck writer surfaces as an error rather than a
# hung window. Readers never wait; WAL lets them read alongside a writer.
BUSY_TIMEOUT_MS = 5_000

LEDGER = """
CREATE TABLE IF NOT EXISTS schema_migrations (
    version    INTEGER PRIMARY KEY,
    name       TEXT    NOT NULL,
    checksum   TEXT    NOT NULL,
    applied_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        CHECK (applied_at IS strftime('%Y-%m-%dT%H:%M:%SZ', applied_at))
) STRICT
"""


class MigrationError(Exception):
    """The schema on disk and the schema in the database disagree."""


@dataclass(frozen=True, slots=True)
class Migration:
    version: int
    name: str
    sql: str

    @property
    def checksum(self) -> str:
        return hashlib.sha256(self.sql.encode()).hexdigest()


def default_data_dir() -> Path:
    """Where the database lives when nobody says otherwise.

    The same directory Tauri's `app_data_dir()` resolves to, so the backend run
    by hand and the backend run by the desktop app find the same file. The app
    passes it explicitly all the same.
    """
    home = Path.home()
    if sys.platform == "darwin":
        base = home / "Library" / "Application Support"
    elif sys.platform == "win32":
        base = Path(os.environ["APPDATA"])
    else:
        base = Path(os.environ.get("XDG_DATA_HOME") or home / ".local" / "share")
    return base / IDENTIFIER


def _refuse_attach(action: int, *_: str | None) -> int:
    # Enrichment lives in its own file (docs/design/0001-llm-boundary.md), and
    # ATTACH is how a query on this connection would reach it.
    return sqlite3.SQLITE_DENY if action == sqlite3.SQLITE_ATTACH else sqlite3.SQLITE_OK


def connect(path: Path) -> sqlite3.Connection:
    """Open Steward's database, creating the file if it does not exist."""
    # sqlite3 creates the file but not its directory, which on a first launch
    # does not exist yet.
    path.parent.mkdir(parents=True, exist_ok=True)
    # The pragmas go first, with autocommit on. Once it is off, sqlite3 keeps a
    # transaction open at all times, and inside one `foreign_keys` is silently
    # ignored and `journal_mode` raises.
    conn = sqlite3.connect(path, autocommit=True)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute(f"PRAGMA busy_timeout = {BUSY_TIMEOUT_MS}")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.set_authorizer(_refuse_attach)
    # From here, commit() and rollback() mean what they say: every statement is
    # in a transaction until one of them ends it.
    conn.autocommit = False
    return conn


def migrations() -> list[Migration]:
    """Every migration in the package, in the order they must be applied."""
    found: dict[int, Migration] = {}
    for entry in resources.files("steward.migrations").iterdir():
        match = FILENAME.match(entry.name)
        if match is None:
            if entry.name.endswith(".sql"):
                raise MigrationError(f"{entry.name} is not NNNN_name.sql")
            continue
        version, name = int(match.group(1)), match.group(2)
        if version in found:
            raise MigrationError(
                f"two migrations numbered {version:04d}: "
                f"{found[version].name} and {name}"
            )
        found[version] = Migration(version, name, entry.read_text(encoding="utf-8"))
    return [found[version] for version in sorted(found)]


def apply(conn: sqlite3.Connection) -> list[Migration]:
    """Apply every migration the database has not seen. Returns what it ran."""
    # With autocommit on, rollback() does nothing, and a migration that fails
    # halfway stays half-applied.
    assert conn.autocommit is False, "apply needs a connection from connect()"

    conn.execute(LEDGER)
    conn.commit()

    applied = dict(
        conn.execute("SELECT version, checksum FROM schema_migrations").fetchall()
    )

    pending = []
    for migration in migrations():
        recorded = applied.pop(migration.version, None)
        if recorded is None:
            pending.append(migration)
        elif recorded != migration.checksum:
            raise MigrationError(
                f"{migration.version:04d}_{migration.name}.sql has changed since it "
                f"was applied. Recorded {recorded[:12]}, found "
                f"{migration.checksum[:12]}."
            )
    if applied:
        raise MigrationError(
            f"the database has migrations this build does not: "
            f"{', '.join(f'{v:04d}' for v in sorted(applied))}"
        )

    # executescript() runs inside the transaction that is already open, so the
    # migration and its ledger row commit together or not at all. The script
    # must not contain BEGIN or COMMIT of its own.
    for migration in pending:
        try:
            conn.executescript(migration.sql)
            conn.execute(
                "INSERT INTO schema_migrations (version, name, checksum) "
                "VALUES (?, ?, ?)",
                (migration.version, migration.name, migration.checksum),
            )
        except BaseException:
            conn.rollback()
            raise
        conn.commit()
    return pending
