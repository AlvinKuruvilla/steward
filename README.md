# Steward

A workbench for running an open-source repository. Steward reads GitHub's event
stream and tells a maintainer what is waiting on whom, with the events that say
so.

> [!NOTE]
> Early development. The data model and the GitHub normalizer work; there is no
> CLI, no database writer and no UI, so there is nothing to install yet.
> [`ROADMAP.md`](ROADMAP.md) says what each version has to prove.

## Why

A maintainer's question is "what needs me today". GitHub answers with a list
sorted by update time.

The answer lives in the event stream, and GitHub's current fields do not carry
it. `isDraft` is false on every merged pull request, whatever it was opened as.
A review that only left a comment looks like one that asked for changes.

Folding the events answers both. Measured across 1,255 pull requests and 1,190
issues in five repositories: every open pull request gets classified once one
policy rule is supplied, and 87% of Precogly's come back `UNKNOWN` without it.
[The audit](docs/audit/2026-09-21-contribution-flow.md) has the numbers and the
method.

## How it works

GitHub stays canonical. Steward keeps an append-only log of the events it
reported and derives everything else at read time.

```text
  GitHub REST timeline
        │
        │  normalize      one row per event, immutable
        ▼
  ┌───────────┐
  │  events   │           opened, review, force_pushed, labeled, …
  └───────────┘
        │
        │  fold           pure: same events, same answer
        ▼
  (workflow_state, blocked_on)
        │
        └── every claim links to the event that produced it
```

Conclusions stay out of the log: `STALE` and `NEEDS_ATTENTION` are judgements,
and a judgement in an append-only log can never be revised. Drop every derived
table, replay the log, and the state comes back identical. V0 has to prove that.

Where events alone cannot answer, repository policy does, and the answer says
which applied. `EVENT` for a state that came from an event, `POLICY` for one
that needed a rule from `steward.toml`, `UNKNOWN` for the rest.

## Non-goals

- No writes to GitHub. No merging, closing, labelling or commenting.
- No replacement for GitHub's UI. Reviewing, replying and merging happen there.
- No contributor scores, rankings or promotion suggestions.
- No language model anywhere near canonical state. Models live in their own
  package, dependency group and database role, none of which the engine can
  reach. See [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md).

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
