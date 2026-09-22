"""Applying the schema, forward only.

Migrations are numbered SQL files inside the package, so an installed wheel
carries them. Each runs in its own transaction and is recorded in
`schema_migrations` with a checksum of what ran.

The connection must be acting as `steward_owner`. `10-roles.sql` grants
`steward_engine` its privileges through `ALTER DEFAULT PRIVILEGES FOR ROLE
steward_owner`, which covers tables that role creates and no others.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from importlib import resources
from typing import Any

import psycopg

# Arbitrary. Fixed forever, so two runners against one database take the same
# lock.
LOCK_KEY = 0x53544557  # "STEW"

OWNER = "steward_owner"

FILENAME = re.compile(r"^(\d{4})_([a-z0-9_]+)\.sql$")

LEDGER = """
CREATE TABLE IF NOT EXISTS schema_migrations (
    version    INTEGER     PRIMARY KEY,
    name       TEXT        NOT NULL,
    checksum   TEXT        NOT NULL,
    applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
)
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


def apply(conn: psycopg.Connection[Any]) -> list[Migration]:
    """Apply every migration the database has not seen. Returns what it ran."""
    acting_as = conn.execute("SELECT current_user").fetchone()
    if acting_as is None or acting_as[0] != OWNER:
        raise MigrationError(
            f"connected as {acting_as[0] if acting_as else 'nobody'}, not {OWNER}. "
            f"The admin connection string needs options=-c role={OWNER}."
        )

    # Session-level: it outlives the per-migration transactions below.
    conn.execute("SELECT pg_advisory_lock(%s)", (LOCK_KEY,))
    with conn.transaction():
        conn.execute(LEDGER)

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

    for migration in pending:
        with conn.transaction():
            conn.execute(migration.sql)
            conn.execute(
                "INSERT INTO schema_migrations (version, name, checksum) "
                "VALUES (%s, %s, %s)",
                (migration.version, migration.name, migration.checksum),
            )
    return pending
