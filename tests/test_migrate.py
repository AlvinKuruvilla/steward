"""The migration runner, against a real database.

What is being checked is ownership and role behaviour, which only Postgres can
answer. The database comes from `conftest.py`, which skips when none is up.
"""

from __future__ import annotations

from typing import Any

import psycopg
import pytest

from steward.migrate import MigrationError, apply, migrations


def test_migrations_are_numbered_and_ordered() -> None:
    found = migrations()
    assert found, "no migrations in the package"
    assert [m.version for m in found] == sorted(m.version for m in found)
    assert found[0].version == 1


def test_apply_creates_the_schema(admin: psycopg.Connection[Any]) -> None:
    ran = apply(admin)

    assert [m.version for m in ran] == [m.version for m in migrations()]
    tables = {
        row[0]
        for row in admin.execute(
            "SELECT tablename FROM pg_tables WHERE schemaname = 'public'"
        ).fetchall()
    }
    assert tables == {"events", "repositories", "schema_migrations"}


def test_apply_is_idempotent(admin: psycopg.Connection[Any]) -> None:
    apply(admin)
    assert apply(admin) == []


def test_tables_are_owned_by_the_owner_role(admin: psycopg.Connection[Any]) -> None:
    # The reason the admin URL carries `role=steward_owner`. Owned by anyone
    # else, and ALTER DEFAULT PRIVILEGES never fires.
    apply(admin)
    owners = {
        row[0]
        for row in admin.execute(
            "SELECT DISTINCT tableowner FROM pg_tables WHERE schemaname = 'public'"
        ).fetchall()
    }
    assert owners == {"steward_owner"}


def test_the_engine_can_read_what_was_migrated(admin: psycopg.Connection[Any]) -> None:
    apply(admin)
    for table in ("events", "repositories"):
        assert admin.execute(
            "SELECT has_table_privilege('steward_engine', %s, 'SELECT')", (table,)
        ).fetchone() == (True,)


def test_the_engine_still_cannot_reach_enrichment(
    admin: psycopg.Connection[Any],
) -> None:
    apply(admin)
    assert admin.execute(
        "SELECT has_schema_privilege('steward_engine', 'enrichment', 'USAGE')"
    ).fetchone() == (False,)


def test_an_edited_migration_is_refused(admin: psycopg.Connection[Any]) -> None:
    apply(admin)
    with admin.transaction():
        admin.execute("UPDATE schema_migrations SET checksum = 'tampered'")
    with pytest.raises(MigrationError, match="has changed since it was applied"):
        apply(admin)


def test_a_migration_the_build_lacks_is_refused(admin: psycopg.Connection[Any]) -> None:
    apply(admin)
    with admin.transaction():
        admin.execute(
            "INSERT INTO schema_migrations (version, name, checksum) "
            "VALUES (9999, 'from_the_future', 'x')"
        )
    with pytest.raises(MigrationError, match="migrations this build does not"):
        apply(admin)


def test_the_wrong_role_is_refused(database: str) -> None:
    # The same credential without the role switch, which is the misconfiguration
    # that would otherwise migrate successfully and grant the engine nothing.
    with (
        psycopg.connect(database.split("?")[0]) as conn,
        pytest.raises(MigrationError, match="not steward_owner"),
    ):
        apply(conn)
