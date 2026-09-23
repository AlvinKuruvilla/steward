"""Where the database-backed tests get their database.

A fresh file under pytest's `tmp_path` for every test, migrated and empty. No
test can reach a database a developer has synced into, and none needs anything
running first.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from pathlib import Path

import pytest

from steward.migrate import apply, connect


@pytest.fixture
def db(tmp_path: Path) -> Iterator[sqlite3.Connection]:
    """A connection to a migrated, empty database."""
    conn = connect(tmp_path / "steward.db")
    apply(conn)
    yield conn
    conn.close()
