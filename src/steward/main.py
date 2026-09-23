"""The backend's entry point.

One command. Syncing and reading the log happen in the interface; this starts
the server the interface talks to. The database is `steward.db` in the data
directory, which the desktop app passes explicitly and which otherwise defaults
to the same place the app would choose.

The desktop app starts `steward serve --watch-stdin` with `STEWARD_API_TOKEN`
in the environment and reads one line from stdout:

    {"steward": "listening", "port": 49731}

Nothing else is written to stdout, so the app can take the first line as the
handshake. Logs go to stderr.
"""

from __future__ import annotations

import copy
import json
import os
import socket
import sys
import threading
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
    port: Annotated[
        int, typer.Option(help="port on 127.0.0.1; 0 picks a free one")
    ] = 0,
    watch_stdin: Annotated[
        bool,
        typer.Option(help="exit when stdin closes, as it does when the app dies"),
    ] = False,
) -> None:
    """Serve the API on loopback, for the desktop app."""
    import uvicorn
    from uvicorn.config import LOGGING_CONFIG

    if not os.environ.get("STEWARD_API_TOKEN"):
        typer.echo(
            "STEWARD_API_TOKEN is not set. Every request must carry it, so the "
            "server refuses to start without one.",
            err=True,
        )
        raise typer.Exit(2)

    # uvicorn imports the app by name, so the choice reaches it through the
    # environment rather than an argument.
    os.environ["STEWARD_DATA_DIR"] = str(data_dir or default_data_dir())

    # Bound here rather than by uvicorn, so that with port 0 the port the kernel
    # chose is known before anything is served. Picking a free port and then
    # binding it leaves a window for something else to take it.
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", port))

    # uvicorn sends access logs to stdout by default, which is the handshake
    # channel.
    logging = copy.deepcopy(LOGGING_CONFIG)
    logging["handlers"]["access"]["stream"] = "ext://sys.stderr"
    server = uvicorn.Server(
        uvicorn.Config("steward.api:app", log_config=logging, log_level="info")
    )

    if watch_stdin:
        # The app holds the write end of this pipe. When the app exits, however
        # it exits, the read returns EOF. Tauri kills its children on a clean
        # quit; this covers the unclean ones, and PyInstaller's onefile
        # bootloader, whose child inherits the same stdin.
        def exit_when_stdin_closes() -> None:
            while sys.stdin.buffer.read(4096):
                pass
            server.should_exit = True

        threading.Thread(target=exit_when_stdin_closes, daemon=True).start()

    print(
        json.dumps({"steward": "listening", "port": listener.getsockname()[1]}),
        flush=True,
    )
    server.run(sockets=[listener])


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
