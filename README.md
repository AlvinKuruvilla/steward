# Steward

A workbench for running an open-source repository. Steward reads GitHub's event
stream and tells a maintainer what is waiting on whom, with the events that say
so.

> [!NOTE]
> Early development. The data model and the GitHub normalizer work; there is no
> CLI, no database writer and no UI, so there is nothing to install yet.
> [`ROADMAP.md`](ROADMAP.md) says what each version has to prove.

## Why

GitHub answers "what needs me today" with a list sorted by update time, and its
current fields cannot do better. `isDraft` is false on every merged pull request
whatever it was opened as; a review that only commented looks like one that
asked for changes.

The event stream answers both exactly. Folding it classified every open pull
request across the five repositories measured, 1,255 in all, once one policy
rule was supplied. [The audit](docs/audit/2026-09-21-contribution-flow.md) has
the method.

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

Requires Python 3.13 and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
uv run pytest
uv run mypy --strict src/steward
uv run ruff check src tests
```

Tests replay a recorded GitHub response through `httpx.MockTransport`, so they
need no network and no token.

## Documentation

- [`ROADMAP.md`](ROADMAP.md) — the versions, and the acceptance bar for each.
- [`docs/audit/2026-09-21-contribution-flow.md`](docs/audit/2026-09-21-contribution-flow.md)
  — the measurements the plan is built on, and where the original design was
  wrong.
- [`docs/corpus.md`](docs/corpus.md) — the test repositories, what each one
  catches, and what the corpus still has no example of.
- [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md) — where a
  model is allowed to be.
- [`docs/design/0002-visual-language.md`](docs/design/0002-visual-language.md) —
  the interface, with token values.
- [`SESSION.md`](SESSION.md) — known gaps and deferred problems.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
