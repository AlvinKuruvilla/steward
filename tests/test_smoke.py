"""The command line's surface."""

from __future__ import annotations

import steward
from steward.main import main


def test_version_is_set() -> None:
    assert steward.__version__


def test_help_exits_cleanly() -> None:
    assert main(["--help"]) == 0


def test_no_arguments_prints_help() -> None:
    # click treats a missing command as a usage error, hence 2 rather than 0.
    assert main([]) == 2


def test_a_repository_must_be_owner_slash_repo() -> None:
    assert main(["sync", "precogly"]) == 2


def test_sync_without_a_token_is_an_error() -> None:
    assert main(["sync", "precogly/precogly"]) == 2
