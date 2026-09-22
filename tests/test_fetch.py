"""Paging, against a recorded response served across two pages.

The items are real; only the split is synthetic. A test whose fixture fits in
one page cannot tell a paged reader from an unpaged one, which is the bug being
guarded against.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import pytest
from githubkit import GitHub

from steward.fetch import pull_requests, timeline

FIXTURE = Path(__file__).parent / "data" / "precogly_rest_timeline.json"
NEXT = '<https://api.github.com{path}?page=2>; rel="next"'


@pytest.fixture(scope="module")
def recorded() -> dict[str, Any]:
    loaded: dict[str, Any] = json.loads(FIXTURE.read_text())
    return loaded


def _split_serving(items: list[Any], path: str) -> httpx.MockTransport:
    """Serve `items` as two pages, the first announcing the second."""
    half = len(items) // 2

    def replay(request: httpx.Request) -> httpx.Response:
        assert request.url.path == path, f"no recording for {request.url.path}"
        if request.url.params.get("page") == "2":
            return httpx.Response(200, json=items[half:])
        return httpx.Response(
            200, json=items[:half], headers={"Link": NEXT.format(path=path)}
        )

    return httpx.MockTransport(replay)


async def test_timeline_reads_past_the_first_page(recorded: dict[str, Any]) -> None:
    number, items = max(recorded["timelines"].items(), key=lambda kv: len(kv[1]))
    path = f"/repos/precogly/precogly/issues/{number}/timeline"
    gh: GitHub[Any] = GitHub("recorded", async_transport=_split_serving(items, path))

    read = await timeline(gh, "precogly", "precogly", int(number))

    assert len(read) == len(items)
    assert [item.node_id for item in read if hasattr(item, "node_id")] == [
        item["node_id"] for item in items if "node_id" in item
    ]


async def test_pull_requests_read_past_the_first_page(recorded: dict[str, Any]) -> None:
    path = "/repos/precogly/precogly/pulls"
    gh: GitHub[Any] = GitHub(
        "recorded",
        async_transport=_split_serving(recorded["pulls"], path),
    )

    read = [pr async for pr in pull_requests(gh, "precogly", "precogly")]

    assert [pr.number for pr in read] == [pr["number"] for pr in recorded["pulls"]]


async def test_a_single_page_is_not_requested_twice(recorded: dict[str, Any]) -> None:
    # A reader that keeps going without a `Link` header would loop on the last
    # page, which a split fixture cannot catch.
    calls = 0

    def replay(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(200, json=recorded["pulls"])

    gh: GitHub[Any] = GitHub("recorded", async_transport=httpx.MockTransport(replay))
    read = [pr async for pr in pull_requests(gh, "precogly", "precogly")]
    assert len(read) == len(recorded["pulls"])
    assert calls == 1
