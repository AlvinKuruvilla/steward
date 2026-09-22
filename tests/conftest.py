"""Where the database-backed tests get their database.

`steward_test`, never `steward`. These tests drop every table in `public`
between cases, so pointing them at the database a developer syncs into would
empty it. `db/init/20-databases.sql` creates both.

They skip when nothing is listening, so `pytest` works with no Postgres running.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from typing import Any

import psycopg
import pytest

ADMIN_URL = os.environ.get(
    "STEWARD_TEST_ADMIN_DATABASE_URL",
    "postgresql://steward_migrator:steward-dev@127.0.0.1:5432/steward_test"
    "?options=-c%20role%3Dsteward_owner",
)
ENGINE_URL = os.environ.get(
    "STEWARD_TEST_DATABASE_URL",
    "postgresql://steward_engine:steward-dev@127.0.0.1:5432/steward_test",
)

EMPTY_THE_SCHEMA = """
DO $$
DECLARE t record;
BEGIN
    FOR t IN SELECT tablename FROM pg_tables WHERE schemaname = 'public'
    LOOP
        EXECUTE format('DROP TABLE public.%I CASCADE', t.tablename);
    END LOOP;
END $$
"""


def _reachable() -> bool:
    try:
        with psycopg.connect(ADMIN_URL, connect_timeout=2):
            return True
    except psycopg.OperationalError:
        return False


@pytest.fixture(scope="session")
def database() -> str:
    """The admin URL, or a skip when no database is listening."""
    if not _reachable():
        pytest.skip(f"no database at {ADMIN_URL.split('@')[-1].split('?')[0]}")
    return ADMIN_URL


@pytest.fixture
def admin(database: str) -> Iterator[psycopg.Connection[Any]]:
    """A connection acting as steward_owner, against an empty schema."""
    with psycopg.connect(database) as conn:
        with conn.transaction():
            conn.execute(EMPTY_THE_SCHEMA)
        yield conn


@pytest.fixture
def engine(admin: psycopg.Connection[Any]) -> Iterator[psycopg.Connection[Any]]:
    """The application's connection, on a schema the migrations have built."""
    from steward.migrate import apply

    apply(admin)
    # A second connection cannot see any of that until it is committed:
    # psycopg's transaction() nests as a savepoint inside the connection's
    # own open transaction, which ends when the `admin` fixture does.
    admin.commit()
    with psycopg.connect(ENGINE_URL) as conn:
        yield conn
