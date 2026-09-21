#!/usr/bin/env bash
# Refresh the pinned copy of GitHub's public GraphQL schema.
#
# The schema is an input to code generation, so it is pinned rather than
# fetched at build time: a type GitHub adds arrives as a diff someone reads,
# and a build run today produces what a build run last month produced.
set -euo pipefail

url="https://docs.github.com/public/fpt/schema.docs.graphql"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out="$root/schema/github.graphql"

# Kept byte-identical to what GitHub serves, so the checksum can be compared
# against a fresh download without accounting for a header we added.
curl --fail --silent --show-error --location --max-time 120 "$url" -o "$out.new"
mv "$out.new" "$out"

( cd "$root/schema" && shasum -a 256 github.graphql > github.graphql.sha256 )

printf 'fetched %s\n  from %s\n  %s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$url" "$(cat "$root/schema/github.graphql.sha256")"
