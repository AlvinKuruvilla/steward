# Steward

A workbench for running an open-source repository. Steward keeps a derived model
of contribution state and answers one question well: what is waiting on whom, and
what is the evidence.

> **Status: early development.** The data model and the GitHub normalizer work
> and are tested against five real repositories. There is no CLI, no database
> writer and no UI yet, so there is nothing to install. See
> [Status](#status).

## Why

A maintainer's real question is "what needs me today". GitHub answers it with a
list sorted by update time. What would answer it properly is already there, in
the event stream rather than in the current fields.

Reading current fields gets it wrong in ways that look right. `isDraft` is false
on every merged pull request, whatever it was opened as. A review that only left
a comment reads like a review that asked for changes.

Folding the events instead was measured against 1,255 pull requests and 1,190
issues across five repositories. It classifies every open pull request in all
five once one policy rule is supplied; without that rule, 87% of Precogly's come
back `UNKNOWN`. The numbers and the method are in
[the audit](docs/audit/2026-09-21-contribution-flow.md).

## How it works

GitHub stays canonical. Steward stores an append-only log of the events GitHub
reported, and derives everything else from it at read time.

```text
  GitHub REST timeline
        │
        │  normalize      one row per event, immutable, no interpretation
        ▼
  ┌───────────┐
  │  events   │           opened, review, force_pushed, labeled, …
  └───────────┘
        │
        │  fold           a pure function: same events, same answer, forever
        ▼
  (workflow_state, blocked_on)
        │
        └── every claim links to the event that produced it
```

Conclusions are never written to the log. `STALE` and `NEEDS_ATTENTION` are
judgements; a judgement in an append-only log can never be revised, so the log
holds facts and the fold computes the rest. Drop every derived table, replay the
log, and the state comes back identical — a property V0 has to prove.

Where events alone are not enough, repository policy fills the gap. The result
says which it was: a state derived from an event is labelled `EVENT`; one
that needed a rule from `steward.toml` is labelled `POLICY`; anything else is
shown as `UNKNOWN` rather than guessed.

## Non-goals

- Write to GitHub. No merging, closing, labelling or commenting.
- Replace GitHub's UI. Reviewing, replying and merging happen there.
- Score contributors, rank them, or suggest promotions.
- Let a language model touch canonical state. Models are confined to a separate
  package, dependency group and database role, none of which the engine can
  reach — [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md).

## Status

Working:

- `src/steward/model.py` — the event model and its JSONB round trip.
- `src/steward/normalize.py` — GitHub's REST timeline to events, 17 kinds.
- `db/migrations/0001_events.sql` — the log, the roles, the snapshot tables.

Not yet: the migration runner, `steward sync`, the fold, the CLI and the web UI.
`compose.yaml` names a Dockerfile that does not exist, so `docker compose up`
will not work today.

Checked against `precogly/precogly`, `astral-sh/ruff`, `kubernetes/kubernetes`,
`tokio-rs/tokio` and `home-assistant/core`: 125 pull requests, 1,722 events, no
failures. [`ROADMAP.md`](ROADMAP.md) has what each version must prove before it
counts as done.

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
