"""The migration runner, against a real database.

What is being checked is ownership and role behaviour, which only Postgres can
answer. These skip unless `STEWARD_ADMIN_DATABASE_URL` is set; `docker compose
up -d db` and the URL from `compose.yaml` is enough.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from typing import Any

import psycopg
import pytest

from steward.migrate import MigrationError, apply, migrations

ADMIN_URL = os.environ.get("STEWARD_ADMIN_DATABASE_URL")

pytestmark = pytest.mark.skipif(
    ADMIN_URL is None, reason="needs a database: set STEWARD_ADMIN_DATABASE_URL"
)


@pytest.fixture
def db() -> Iterator[psycopg.Connection[Any]]:
    """A connection with an empty schema, so each test migrates from nothing.

    The tables go rather than the schema itself. Recreating `public` needs
    CREATE on the database, which steward_owner does not have and should not.
    """
    assert ADMIN_URL is not None
    with psycopg.connect(ADMIN_URL) as conn:
        with conn.transaction():
            conn.execute("""
                DO $$
                DECLARE t record;
                BEGIN
                    FOR t IN SELECT tablename FROM pg_tables WHERE schemaname = 'public'
                    LOOP
                        EXECUTE format('DROP TABLE public.%I CASCADE', t.tablename);
                    END LOOP;
                END $$
            """)
        yield conn


def test_migrations_are_numbered_and_ordered() -> None:
    found = migrations()
    assert found, "no migrations in the package"
    assert [m.version for m in found] == sorted(m.version for m in found)
    assert found[0].version == 1


def test_apply_creates_the_schema(db: psycopg.Connection[Any]) -> None:
    ran = apply(db)

    assert [m.version for m in ran] == [m.version for m in migrations()]
    tables = {
        row[0]
        for row in db.execute(
            "SELECT tablename FROM pg_tables WHERE schemaname = 'public'"
        ).fetchall()
    }
    assert tables == {"events", "repositories", "schema_migrations"}


def test_apply_is_idempotent(db: psycopg.Connection[Any]) -> None:
    apply(db)
    assert apply(db) == []


def test_tables_are_owned_by_the_owner_role(db: psycopg.Connection[Any]) -> None:
    # The reason the admin URL carries `role=steward_owner`. Owned by anyone
    # else, and ALTER DEFAULT PRIVILEGES never fires.
    apply(db)
    owners = {
        row[0]
        for row in db.execute(
            "SELECT DISTINCT tableowner FROM pg_tables WHERE schemaname = 'public'"
        ).fetchall()
    }
    assert owners == {"steward_owner"}


def test_the_engine_can_read_what_was_migrated(db: psycopg.Connection[Any]) -> None:
    apply(db)
    for table in ("events", "repositories"):
        assert db.execute(
            "SELECT has_table_privilege('steward_engine', %s, 'SELECT')", (table,)
        ).fetchone() == (True,)


def test_the_engine_still_cannot_reach_enrichment(
    db: psycopg.Connection[Any],
) -> None:
    apply(db)
    assert db.execute(
        "SELECT has_schema_privilege('steward_engine', 'enrichment', 'USAGE')"
    ).fetchone() == (False,)


def test_an_edited_migration_is_refused(db: psycopg.Connection[Any]) -> None:
    apply(db)
    with db.transaction():
        db.execute("UPDATE schema_migrations SET checksum = 'tampered'")
    with pytest.raises(MigrationError, match="has changed since it was applied"):
        apply(db)


def test_a_migration_the_build_lacks_is_refused(db: psycopg.Connection[Any]) -> None:
    apply(db)
    with db.transaction():
        db.execute(
            "INSERT INTO schema_migrations (version, name, checksum) "
            "VALUES (9999, 'from_the_future', 'x')"
        )
    with pytest.raises(MigrationError, match="migrations this build does not"):
        apply(db)


def test_the_wrong_role_is_refused() -> None:
    assert ADMIN_URL is not None
    # The same credential without the role switch, which is the misconfiguration
    # that would otherwise migrate successfully and grant the engine nothing.
    with (
        psycopg.connect(ADMIN_URL.split("?")[0]) as conn,
        pytest.raises(MigrationError, match="not steward_owner"),
    ):
        apply(conn)
