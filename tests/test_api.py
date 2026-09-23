"""The JSON the interface reads.

Events come from the recorded
response, so what these assert is the API's shape over known events rather than
whatever a repository happens to look like today.
"""

from __future__ import annotations

import json
import re
import sqlite3
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import httpx
import pytest
from fastapi.testclient import TestClient
from githubkit import GitHub

from steward.api import _sized, app
from steward.normalize import events_for_pull_request
from steward.store import repository_id, write

FIXTURE = Path(__file__).parent / "data" / "precogly_rest_timeline.json"
TIMELINE = re.compile(r"^/repos/precogly/precogly/issues/(\d+)/timeline$")


@pytest.fixture
def client(
    db: sqlite3.Connection, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> Iterator[TestClient]:
    recorded = json.loads(FIXTURE.read_text())

    def replay(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/repos/precogly/precogly/pulls":
            return httpx.Response(200, json=recorded["pulls"])
        match = TIMELINE.match(request.url.path)
        assert match, f"no recording for {request.url.path}"
        return httpx.Response(200, json=recorded["timelines"][match.group(1)])

    gh: GitHub[Any] = GitHub("recorded", transport=httpx.MockTransport(replay))

    repo = repository_id(db, "precogly", "precogly", "R_kgDOabc")
    for pr in gh.rest.pulls.list(
        owner="precogly", repo="precogly", state="all", per_page=26
    ).parsed_data:
        write(
            db,
            repo,
            events_for_pull_request(
                pr,
                gh.rest.issues.list_events_for_timeline(
                    owner="precogly",
                    repo="precogly",
                    issue_number=pr.number,
                    per_page=100,
                ).parsed_data,
            ),
        )

    # The app opens steward.db in this directory, which is the file `db` holds.
    monkeypatch.setenv("STEWARD_DATA_DIR", str(tmp_path))
    yield TestClient(app)


def test_repositories_lists_what_was_synced(client: TestClient) -> None:
    body = client.get("/api/repositories").json()
    assert [(r["owner"], r["name"]) for r in body] == [("precogly", "precogly")]


def test_pulls_are_open_only_by_default(client: TestClient) -> None:
    open_only = client.get("/api/repositories/precogly/precogly/pulls").json()
    everything = client.get(
        "/api/repositories/precogly/precogly/pulls", params={"open_only": False}
    ).json()

    assert len(open_only) < len(everything)
    assert not {row["state"] for row in open_only} & {"MERGED", "CLOSED"}


def test_every_standing_carries_its_derivation(client: TestClient) -> None:
    for row in client.get("/api/repositories/precogly/precogly/pulls").json():
        assert row["derivation"] in {"EVENT", "POLICY", "UNKNOWN"}
        # An answer with no evidence behind it says so on both axes.
        if row["derivation"] == "UNKNOWN":
            assert row["blocked_on"] == "UNKNOWN"


def test_a_pull_request_carries_its_evidence(client: TestClient) -> None:
    body = client.get("/api/repositories/precogly/precogly/pulls/322").json()

    assert body["standing"]["state"] == "MERGED"
    assert body["episodes"][0]["state"] == "DRAFT"
    assert body["episodes"][-1]["end"] is None
    # Every episode boundary is an event the caller can see for itself.
    assert len(body["events"]) >= len(body["episodes"])
    assert body["events"] == sorted(body["events"], key=lambda e: e["occurred_at"])


def test_an_unsynced_repository_is_not_found(client: TestClient) -> None:
    assert client.get("/api/repositories/astral-sh/ruff/pulls").status_code == 404


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        # The shape `GET /users/<login>` returns today.
        (
            "https://avatars.githubusercontent.com/u/5430905?v=4",
            "https://avatars.githubusercontent.com/u/5430905?v=4&s=64",
        ),
        # Nothing promises `v` stays, and `?` written where `&` belongs is how
        # string-joining a parameter onto a URL fails without saying so.
        (
            "https://avatars.githubusercontent.com/u/5430905",
            "https://avatars.githubusercontent.com/u/5430905?s=64",
        ),
        # A size already there is replaced rather than repeated.
        (
            "https://avatars.githubusercontent.com/u/5430905?v=4&s=200",
            "https://avatars.githubusercontent.com/u/5430905?v=4&s=64",
        ),
    ],
)
def test_an_avatar_url_carries_the_size_asked_for(url: str, expected: str) -> None:
    assert _sized(url, 64) == expected
