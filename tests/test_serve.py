"""`steward serve` as the desktop app drives it: a real process, over a pipe.

The contract with the shell is three things -- the first stdout line is the
handshake, the token is required, and closing stdin ends the process -- and
none of them is visible to a test client that never starts a server.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path

import httpx
import pytest

TOKEN = "launch-token"


@pytest.fixture
def server(tmp_path: Path) -> Iterator[tuple[subprocess.Popen[bytes], int]]:
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "steward.main",
            "serve",
            "--data-dir",
            str(tmp_path),
            "--watch-stdin",
        ],
        env={**os.environ, "STEWARD_API_TOKEN": TOKEN},
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdout is not None
    handshake = json.loads(process.stdout.readline())
    assert handshake["steward"] == "listening"
    try:
        yield process, handshake["port"]
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()


def test_the_handshake_names_a_port_that_answers(
    server: tuple[subprocess.Popen[bytes], int],
) -> None:
    _, port = server
    response = httpx.get(
        f"http://127.0.0.1:{port}/api/repositories",
        headers={"authorization": f"Bearer {TOKEN}"},
        timeout=10,
    )
    assert response.status_code == 200
    assert response.json() == []


def test_closing_stdin_ends_the_process(
    server: tuple[subprocess.Popen[bytes], int],
) -> None:
    # What happens when the app dies without a chance to kill its child.
    process, port = server
    serving = httpx.get(
        f"http://127.0.0.1:{port}/api/repositories",
        headers={"authorization": f"Bearer {TOKEN}"},
        timeout=10,
    )
    assert serving.status_code == 200

    assert process.stdin is not None
    process.stdin.close()
    assert process.wait(timeout=10) == 0


def test_stdout_carries_nothing_but_the_handshake(
    server: tuple[subprocess.Popen[bytes], int],
) -> None:
    # Access logs and migration messages both went to stdout once; either
    # would be read as a second handshake by a shell that reads line by line.
    process, port = server
    httpx.get(
        f"http://127.0.0.1:{port}/api/repositories",
        headers={"authorization": f"Bearer {TOKEN}"},
        timeout=10,
    )
    assert process.stdin is not None
    process.stdin.close()
    stdout, _ = process.communicate(timeout=10)
    assert stdout == b""


def test_serve_refuses_to_start_without_a_token(tmp_path: Path) -> None:
    env = {k: v for k, v in os.environ.items() if k != "STEWARD_API_TOKEN"}
    finished = subprocess.run(
        [sys.executable, "-m", "steward.main", "serve", "--data-dir", str(tmp_path)],
        env=env,
        capture_output=True,
        timeout=30,
    )
    assert finished.returncode == 2
    assert b"STEWARD_API_TOKEN" in finished.stderr
