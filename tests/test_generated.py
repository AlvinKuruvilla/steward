"""The committed query must be what the pinned schema generates.

Both are checked in, which is what makes a schema refresh a diff someone reads
rather than a surprise at sync time. That only holds while they agree, so this
regenerates into a temp file and compares.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_timeline_query_matches_the_pinned_schema(tmp_path: Path) -> None:
    regenerated = tmp_path / "timeline.graphql"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "gen_timeline_query.py"),
            str(regenerated),
        ],
        check=True,
        capture_output=True,
    )
    committed = (ROOT / "queries" / "timeline.graphql").read_text(encoding="utf-8")
    assert regenerated.read_text(encoding="utf-8") == committed, (
        "queries/timeline.graphql is out of date with schema/github.graphql. "
        "Run scripts/generate.sh."
    )


def test_schema_matches_its_checksum() -> None:
    # The checksum is what a refresh compares against to tell an upstream change
    # from a local edit; a hand-edited schema would otherwise generate happily.
    recorded = (ROOT / "schema" / "github.graphql.sha256").read_text().split()[0]
    actual = subprocess.run(
        ["shasum", "-a", "256", "github.graphql"],
        cwd=ROOT / "schema",
        check=True,
        capture_output=True,
        text=True,
    ).stdout.split()[0]
    assert actual == recorded
