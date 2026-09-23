"""The backend's entry point.

One command. Syncing and reading the log happen in the interface; this starts
the server the interface talks to. The database is `steward.db` in the data
directory, which the desktop app passes explicitly and which otherwise defaults
to the same place the app would choose.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Annotated

import typer

from steward.migrate import default_data_dir

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="A workbench for running an open-source repository.",
)


# A callback, so a single command stays `steward serve` instead of Typer
# collapsing it into bare `steward`.
@app.callback()
def _root() -> None:
    pass


@app.command()
def serve(
    data_dir: Annotated[
        Path | None,
        typer.Option(help="directory holding steward.db [default: the app's own]"),
    ] = None,
    host: Annotated[str, typer.Option(help="interface to bind")] = "127.0.0.1",
    port: Annotated[int, typer.Option(help="port to bind")] = 8000,
) -> None:
    """Serve the API, and the interface if it has been built."""
    import uvicorn

    # uvicorn imports the app by name, so the choice reaches it through the
    # environment rather than an argument.
    os.environ["STEWARD_DATA_DIR"] = str(data_dir or default_data_dir())
    if host not in ("127.0.0.1", "localhost", "::1"):
        # Nothing authenticates a request, so anywhere but loopback this puts
        # the log on the network.
        typer.echo(
            f"warning: binding {host}, and Steward has no authentication",
            err=True,
        )
    uvicorn.run("steward.api:app", host=host, port=port, log_level="info")


def main(argv: list[str] | None = None) -> int:
    """Run the application and return a process exit code."""
    args = sys.argv[1:] if argv is None else argv
    try:
        app(args=args)
    except SystemExit as exit_:
        return int(exit_.code or 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
