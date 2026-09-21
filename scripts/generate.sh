#!/usr/bin/env bash
# Regenerate everything derived from the pinned schema: the timeline query, and
# the typed client built from it.
#
# The client package is removed first. ariadne-codegen writes the files an
# operation needs and leaves any others in place, so a file that stops being
# generated stays behind, still imports, and still type-checks.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

uv run python scripts/gen_timeline_query.py
rm -rf src/steward/github_api
uv run --with ariadne-codegen ariadne-codegen

printf '%s\n' "generated $(find src/steward/github_api -name '*.py' | wc -l | tr -d ' ') files, $(cat src/steward/github_api/*.py | wc -l | tr -d ' ') lines"
