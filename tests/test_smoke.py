"""Smoke tests for steward."""

from __future__ import annotations

import steward


def test_version_is_set() -> None:
    assert steward.__version__


def test_main_runs() -> None:
    from steward.main import main

    assert main([]) == 0
