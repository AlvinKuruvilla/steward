# Steward

A workbench for running an open-source repository.

GitHub stays canonical. Steward keeps a derived model of contribution state and
answers one question well: what is waiting on whom, and what is the evidence.

It is not an AI reviewer. Canonical state comes from authoritative GitHub events
and explicit repository policy, never from a language model — a boundary that is
enforced by package structure, dependency groups, database roles and types, not
by convention. See [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md).

## Where to start

- [`ROADMAP.md`](ROADMAP.md) — versions and what each one has to prove.
- [`docs/audit/2026-09-21-contribution-flow.md`](docs/audit/2026-09-21-contribution-flow.md)
  — the measurements the plan is built on: 1,255 pull requests and 1,190 issues
  across five repositories.
- [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md) — where a
  model is allowed to be, and how that is enforced.
- [`docs/design/0002-visual-language.md`](docs/design/0002-visual-language.md) —
  OpenWork's surface, GitHub's density, with the token values for both.
- [`docs/corpus.md`](docs/corpus.md) — the repositories Steward is tested against,
  what each one catches, and what the corpus still has no example of.

## Status

Design. No code yet.
