<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/steward-dark.svg">
  <img src="assets/steward.svg" alt="" width="40" height="40">
</picture>

# Steward

[![CI](https://github.com/AlvinKuruvilla/steward/actions/workflows/ci.yml/badge.svg)](https://github.com/AlvinKuruvilla/steward/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/AlvinKuruvilla/steward?color=blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)](pyproject.toml)
[![Checked with mypy](https://img.shields.io/badge/mypy-strict-2a6db2)](pyproject.toml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A workbench for running an open-source repository. Steward reads GitHub's event
stream and tells a maintainer what is waiting on whom, with the events that say
so.

> [!NOTE]
> Early development, and becoming a desktop app; [`ROADMAP.md`](ROADMAP.md)
> says why. The backend is on SQLite and the desktop shell is not built yet, so
> for now the interface runs in a browser against `127.0.0.1:8000` (see
> *Development*). Nothing authenticates a request, so keep it on loopback.

## Why

GitHub answers "what needs me today" with a list sorted by update time, and its
current fields cannot do better. `isDraft` is false on every merged pull request
whatever it was opened as; a review that only commented looks like one that
asked for changes.

The event stream answers both exactly. Folding it classified every open pull
request across the five repositories in [`docs/corpus.md`](docs/corpus.md),
1,255 in all, once one policy rule was supplied.

## How it works

GitHub stays canonical. Steward keeps an append-only log of the events GitHub
reported and folds it into `(workflow_state, blocked_on)` at read time, so the
same events always give the same answer and every claim links to the event
behind it.

Each answer says where it came from: `EVENT` when the events alone decide it,
`POLICY` when a rule from `steward.toml` was needed, `UNKNOWN` when neither.

## Non-goals

- No autonomous action. Nothing is merged, closed, labelled or commented on
  unless a maintainer asked for it. Nothing runs on a schedule or on a rule.
- No contributor scores, rankings or promotion suggestions.
- No language model anywhere near canonical state. See
  [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md).

## Development

Requires Python 3.13, [uv](https://docs.astral.sh/uv/), pnpm and
[just](https://just.systems). The desktop shell is not built yet; until it is,
the interface runs in a browser against the API.

```sh
just serve          # the API on 127.0.0.1:8000, with its database in tmp/data
just web            # the interface, with hot reload; add a repository from it
just check          # format, lint, types, tests
just db             # a SQLite shell on the development database
```

Tests replay a recorded GitHub response through `httpx.MockTransport`, so they
need no network and no token. Each one gets its own database file, so
`just test` never touches the one you have synced into.

## Documentation

- [`ROADMAP.md`](ROADMAP.md) — the versions, and the acceptance bar for each.
- [`docs/corpus.md`](docs/corpus.md) — the test repositories, what each one
  catches, and what the corpus still has no example of.
- [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md) — where a
  model is allowed to be.
- [`docs/design/0002-visual-language.md`](docs/design/0002-visual-language.md) —
  the interface, with token values.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
