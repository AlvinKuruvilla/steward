# 0001 — Where a language model is allowed to be

Status: accepted, 2026-09-21.

Steward's canonical state is derived only from authoritative GitHub events and
explicit repository policy. A language model may never produce, alter, or feed
that state. This document says what that means precisely enough to fail a build.

## Why a rule and not a preference

The rule exists because the alternative has a known shape. A project adds a
summary, which is harmless. The summary is good, so it gets a confidence score. A
state is hard to derive, so the score fills it in "temporarily". Two years later
nobody can say which of the repository's answers were computed and which were
generated, and the answer to "why is this waiting on me?" is a paraphrase.

**The engine does not need one.** Folding the event stream into
`(workflow_state, blocked_on)` classified 100% of open pull requests across five
repositories once the policy rule was applied, and 13% to 100% without it. The
gap was never inference; it was repositories that do not press the review-request
button, closed by configuration. Where the audit expected to need a model it
found a field it had not read.

**Generated state cannot be audited.** The product's claim is "this is waiting on
you, and here is the evidence". Evidence means the maintainer can follow the
derivation to a GitHub object and disagree with it. A generated state has no
derivation, only a plausible one. A wrong answer that looks reasonable is worse
than no answer, because it ends the question.

**Issue and PR text is attacker-controlled.** This is the argument that makes the
boundary structural rather than stylistic. Anyone on the internet can open an
issue on a public repository, and its body, its title, and its comments are
untrusted input. Give a model that text and let its output reach state, and
"waiting on maintainer" becomes a field a stranger can write into by asking
nicely inside an issue body. Every prompt-injection defence is probabilistic.
The boundary is not: if model output cannot reach state, the injection has
nowhere to land. Steward is built by people who threat-model for a living and
this is a trust boundary like any other.

## The boundary

```text
 authoritative                 derived                    advisory
 ─────────────                 ───────                    ────────

 GitHub events  ──────────>  event log  ──────────>  state + obligations
 repo policy    ──────────>  (append-only,               (pure fold)
                              immutable)                      │
                                   │                          │
                                   │  read-only               │  read-only
                                   v                          v
                            ┌─────────────────────────────────────┐
                            │           enrichment                │
                            │  summaries, retrieval, clustering   │
                            └─────────────────────────────────────┘
                                             │
                                             v
                                    UI, distinct register,
                                    off by default

 Every arrow points right. There is no arrow back into the derived column,
 and the enrichment box cannot write anywhere. Deleting that box removes
 features and changes no answer.
```

## Enforcement

A principle nobody can fail is a preference. Each of these breaks the build.

**Package boundary.** `steward.engine` is a package with no dependency — direct
or transitive — on an HTTP client or a model SDK. `steward.enrich` is where those
live. An `import-linter` contract forbids `steward.engine` from importing
`steward.enrich`, `httpx`, `requests`, or any provider SDK, and CI runs it.

**Dependency groups.** Model SDKs are an optional group in `pyproject.toml`.
`uv sync --no-group enrich` installs a Steward with no model code on disk at all,
and the full engine test suite passes against it. This is the V3 acceptance test:
uninstalling enrichment leaves Steward working, with one feature visibly absent
and no state changed.

**Separate files, separate processes.** Enrichment rows live in their own SQLite
file, written by an enrichment process and never opened by the engine's. The
engine's connection installs an authorizer that denies `ATTACH`, so a query that
reaches for the enrichment file fails at the statement rather than succeeding
quietly. How the interface shows enrichment beside engine state without the
engine reading it depends on how the window talks to the backend, which is not
settled yet.

SQLite has no roles, so none of this is the database refusing. The engine process
could open the file if someone wrote the code to; the authorizer is installed by
the code it restricts. What stops that code is the import contract above and a
reviewer reading a diff that names the enrichment file. Until 2026-09-23 this was
a Postgres schema the engine's role held no grant on, which the database
enforced; the move to a desktop app gave that up, for the reasons in
[`ROADMAP.md`](../../ROADMAP.md).

**Types.** Enrichment output is `Unverified[T]`, and nothing in the engine's
signatures accepts one. `mypy --strict` rejects the call at the point someone
tries to unwrap it into a state transition.

**Runtime.** The fold runs in a context with no network access. A model call
inside it raises rather than succeeding slowly.

## The audition

Every proposed enrichment answers all four in writing, in an audition record
committed beside the feature. Any "no" is a rejection.

1. **What does the model have that the engine does not?** Not "it is easier" —
   what information exists only in prose? If the answer is a GitHub field, read
   the field. The drafted design proposed a model for exactly one state that
   `ReadyForReviewEvent` already encoded.
2. **Was the deterministic version built and found wanting?** Built, not
   imagined. A record of the deterministic attempt and the specific way it failed
   ships with the feature. Retrieval before summarisation, always.
3. **What is the cost of it being wrong?** Only features that are *annoying* when
   wrong pass. A misleading summary wastes five minutes. A wrong state sends a
   maintainer to the wrong PR and, worse, teaches them to trust the next one.
4. **Does it survive deletion?** Turn it off: does Steward still answer every
   question it claims to answer? If no, it was load-bearing and the boundary has
   already been crossed.

### Applying it

| proposal | verdict | why |
|---|---|---|
| Summarise a 200-comment thread | **pass**, at V3 | The information is only in prose, and a wrong summary is annoying rather than misleading. Ships only after deterministic retrieval finds the thread. |
| Find prior decisions about an architectural choice | **pass**, after deterministic retrieval | Full-text and trigram search over discussion ships first and is useful alone. A model may rank what search already found. |
| Decide whether two issues describe the same bug | **candidates only** | Deterministic signals — identical stack frames, error strings, file paths — produce the candidate set. A model may explain a pairing. It may never merge or close. |
| Determine whether CI passed | **reject** | There is an API. |
| Determine who a PR is waiting on | **reject** | This is the product. It is a fold over events and a config file. |
| Explain why a PR has been waiting | **reject** | The event list is the explanation. Prose describing the event list is strictly worse than the event list. |
| Classify an issue as bug, duplicate, or support | **reject at state level** | Not derivable from events. Steward says so rather than generating a category. May be offered as advisory enrichment. |
| Judge whether a PR is good | **reject, permanently** | The trust boundary. Not a capability question. |

## Determinism, where a model is used at all

- Temperature zero, pinned model version, prompt hashed and stored with the
  output. An enrichment row records which model and which prompt produced it.
- Output is cached against `(model, prompt_hash, input_hash)` and only recomputed
  when an input changes. Re-rendering a page never re-runs a model.
- Enrichment is always resumable and always skippable. A provider outage degrades
  Steward to fully functional with fewer features, never to broken.
- No model call is ever on the path to rendering an inbox.

## Presentation

Enrichment is a different kind of claim than state and the UI never lets them
share a register. The specifics are in
[`0002-visual-language.md`](0002-visual-language.md); the requirement here is that
enrichment is visually distinct, labelled with its model, individually
dismissible, and globally disableable — and that with it disabled, no number,
state, or queue position changes.

## Trade-offs

**We will ship less.** Whole categories of plausible feature — automatic triage,
suggested reviewers, backlog classification — are unavailable at state level.
Other projects will ship them and demo better.

**Some questions stay unanswered.** "Does this issue need reproduction?" is not
derivable from events, so Steward will show `UNKNOWN` where a competitor shows a
confident label. The competitor's label will be wrong some fraction of the time
and nobody will know which fraction.

**The boundary costs real engineering.** A separate process and database file, a
separate package, an import contract, a dependency group, a type wrapper. Every
one is a thing to maintain; a cheaper project would write the rule in a README and
trust code review.

**Nothing outside the code enforces it.** The Postgres role was the one layer the
engine's own code could not switch off, and SQLite has nothing to replace it
with. Every remaining layer is checked by CI or by review, so a determined
change can cross the boundary in one diff. It will at least be a diff that says
so.

It is paid because the boundary is the product. An AI reviewer that is right 95%
of the time is a supply-chain incident with a 5% rate. A deterministic engine that
answers 87% of questions and says `UNKNOWN` to the rest is a tool a maintainer can
build a habit on. The second is worth less in a demo and more on a Tuesday.
