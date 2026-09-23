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


def test_serve_is_still_a_subcommand() -> None:
    # The desktop app starts the backend as `steward serve`. With one command,
    # Typer would otherwise accept only bare `steward`.
    assert main(["serve", "--help"]) == 0
