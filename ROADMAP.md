# Steward roadmap

Steward is a workbench for running an open-source repository. GitHub stays
canonical; Steward keeps a derived, deterministic model of contribution state and
tells a maintainer what is waiting on whom, and why.

Everything here is anchored to an audit of the five repositories in
[`docs/corpus.md`](docs/corpus.md): 1,255 pull requests and 1,190 issues with
full event timelines, measured on 2026-09-21. Where a version's acceptance bar
is a number, that number came from the audit, and the corpus is public, so it
can be re-measured.

## Settled before V0

| decision | choice | note |
|---|---|---|
| V1 surface | pull requests | Chosen over issues-first. The consequence is in *Validation* below. |
| Backend | Python | Start here; swap the engine for something faster if a profile demands it. |
| GitHub API | REST, via `githubkit` | GraphQL was built and removed. REST names the team on a review request, which GraphQL nulls; it costs `willCloseTarget` and an id on cross-references. |
| Store | PostgreSQL | Replaces the local-first SQLite shape. See *The shape this implies*. |
| Deployment | self-hosted, `docker compose up` | CLI plus a local web UI, both talking to your own Postgres. |
| LLM policy | hard architectural boundary | [`docs/design/0001-llm-boundary.md`](docs/design/0001-llm-boundary.md) |
| Look | OpenWork's surface, GitHub's density | [`docs/design/0002-visual-language.md`](docs/design/0002-visual-language.md) |

### What Postgres costs

Picking Postgres retires "local-first". What survives is the CLI, the local web
UI, single-operator ownership of the data, and GitHub as the only source of
truth. What dies is `brew install && run` — Steward now has a service
dependency, so the install story is a compose file.

The invariant that made SQLite attractive is the one thing that must not be lost
in the move:

    drop every derived table, replay the event log, get byte-identical state

Postgres keeps that invariant; it just does not hand it to you for free the way a
single deletable file did. V0 has to prove it, and V1 has to keep proving it in
CI, or it quietly stops being true.

---

## V0 — Ingestion, and nothing else

One job: get GitHub's event stream into Postgres, losslessly, and prove it can be
replayed.

- Project scaffold from the Copier template (uv, ruff, `mypy --strict`, pytest).
- `docker compose up` is the whole install: Postgres, migrations, and the Steward
  container, with the two Postgres roles from `0001` created at bootstrap so the
  engine never has the grants it is not allowed to have. `compose.override.yml`
  mounts the source for development; the committed compose file is what a
  stranger runs.
- REST backfill for one repository, from the issue timeline: commits, reviews,
  review requests and dismissals, ready-for-review and convert-to-draft events,
  label and assignment changes, force pushes, merges, closes and
  cross-references. Seventeen event kinds; anything else is either named as
  carrying no state or is an error.
- An append-only `events` table. Rows are immutable. Nothing else writes to it.
- `steward sync <owner>/<repo>` — resumable, idempotent, safe to interrupt.
- `steward events <pr>` — the raw stream for one PR, oldest first.

**Acceptance.** Sync precogly/precogly twice. The second run adds zero rows.
Truncate every non-event table, replay, and diff: identical. Event counts match
the timeline endpoint's own count per pull request.

**Explicitly not here.** No state machine, no UI, no metrics. If ingestion is
wrong everything above it is wrong, and it is much cheaper to find out now.

---

## V1 — State, policy, and the inbox

The premise, shipped. A maintainer opens Steward and sees what is waiting on
them, with the evidence that put it there.

### The fold

Events in, `(workflow_state, blocked_on)` out, as a pure function. Given the same
events and the same config it returns the same answer, forever, with no network
call and no model in the path.

    OPENED ──draft──> DRAFT ──ready──> REVIEW_WAIT ──approved──> APPROVED
                        ^                  │                        │
                        │        changes requested                  │ commit
                        │                  v                        v
                        └──── AUTHOR_WORK ────commit────> RE_REVIEW_WAIT
                                                                    │
                                        CHECKS_FAILED, CONFLICTED ──┤
                                                                    v
                                                          MERGED / CLOSED

    A PR opened as a draft emits no event saying so. The opening state is
    recovered backwards from whichever of ReadyForReview / ConvertToDraft
    comes first, and `isDraft` is never read — on a merged PR it is always
    false regardless of how the PR began.

Three things the audit says this has to handle from day one:

- **Draft intervals** reconstructed from events, not from `isDraft`. Reading the
  current field is what produced the one wrong `UNKNOWN` in the drafted design.
- **`COMMENTED` reviews create no obligation.** GitHub records neither a request
  nor an approval, so neither does Steward. Precogly PR #382 merged this way and
  any engine that infers "changes were requested" from a comment gets it wrong.
- **Bots are their own cohort.** 13 of Precogly's 15 open PRs are bots. They get
  a `BOT_PR` state, never a human reviewer obligation, and their own queue.

### The policy layer

Without it the engine says `UNKNOWN` for 87% of Precogly's open PRs. With one
rule every repository in the corpus reaches 100%.

`steward.toml`, committed to the repository, read as configuration and never
inferred:

```toml
[review]
default_reviewers = ["AlvinKuruvilla", "vikram-s-narayan"]
# With no review request on the PR, who is a non-draft open PR waiting for?
unrequested_open = "default_reviewers"   # or "nobody", to keep UNKNOWN

[bots]
logins = ["dependabot", "github-actions", "cla-assistant"]
```

Every state carries its derivation class, and the UI never blurs them:

| class | source |
|---|---|
| `EVENT` | an authoritative GitHub event, alone |
| `POLICY` | an event plus a rule the repository wrote down |
| `UNKNOWN` | neither — shown as unknown, never guessed |

### Surfaces

- `steward inbox` — unresolved items where you are the blocked-on actor, oldest
  first.
- `steward pr <n>` — state, the timeline that produced it, and the evidence for
  the current state.
- `steward why <n>` — the derivation, one line per event, each pointing at the
  GitHub object it came from.
- Web UI: repo switcher, inbox, PR detail. Every rendered claim links to the
  event behind it.

**Acceptance.** Run against all five corpus repositories through the normal
`steward sync` path:

| repo | deterministic coverage of open PRs, with policy |
|---|---|
| astral-sh/ruff | 100% |
| home-assistant/core | 100% |
| kubernetes/kubernetes | 100% |
| tokio-rs/tokio | 100% |
| precogly/precogly | 100% |

Bare coverage — no policy rule — must also be reported per repo and must not
regress below the audit's measurement. Every `UNKNOWN` is enumerated in the test
output with its PR number; a coverage number with no list of what it excluded is
not evidence.

Plus: Precogly #551 resolves to `CHANGES_REQUESTED`/author, #491 to
`RE_REVIEW_WAIT`/reviewer, #382's history never enters `CHANGES_REQUESTED`, and
#322 shows a draft interval from Aug 15 to Aug 29.

---

## V1.5 — Flow

Where the repository's time goes. Deterministic aggregation over V1's intervals;
no new data required.

- Time to first review, re-review latency, time approved-but-unmerged, time in
  checks, review cycles per PR.
- Lifetime attribution: the share of merged-PR wall-clock spent in each state,
  the table the audit produced by hand.
- The funnel: opened, reached review, changes requested, returned, merged, with
  the drop-off at each step.
- Review load by person and by area.
- The bot queue as its own view: age, grouping, what a batch would contain.

**Acceptance.** Reproduces the audit's per-repo attribution table within
rounding. Every metric names its population in the UI — "173 merged PRs,
2026-09-07 to 09-21" — because a number whose denominator is invisible ends
arguments it should not.

---

## V2 — Issues, through the reply window

The audit found deterministic ground here that the drafted plan assumed was
absent.

- Issue ingestion: comments, labels, assignment, cross-references, close reasons.
- **Reply-window calibration.** Per repository, the cumulative distribution of
  first-reply latency. In all four repositories measured, ~90% of first replies
  that ever arrive have arrived by day seven.
- **The window inbox.** Open issues with no reply from anyone but their author,
  split by whether they are still inside the repository's window. Precogly has
  103 unanswered issues; the useful surface is the handful still in the window,
  not the pile outside it.
- Deterministic duplicate *candidates*: identical stack frames, error strings,
  file paths, linked commits. Candidates are shown as evidence and joined; they
  are never merged or closed by Steward.
- Issue state stays coarse on purpose. "Needs reproduction" is not derivable from
  events and Steward will not pretend otherwise.

**Acceptance.** Reproduces the audit's survival table per repo. The window inbox
for Precogly is small enough to work to zero in one sitting; if it is not, the
window is calibrated wrong and that is the finding.

---

## V2.5 — People

The original problem: maintainers exist in the repository already and nobody has
the bandwidth to notice them.

- Contribution surface per person: areas authored, areas reviewed, areas
  discussed, over a stated window.
- Review reciprocity: who reviews whom, and where a single person is the only
  reviewer for an area.
- Emergent ownership as evidence, never as a score. `sidd190` wrote 45 of
  Precogly's 75 external PRs; the UI shows the 45 and says nothing else.
- Requires per-PR file paths, which V0's ingestion does not pull. That is the
  schema change this version carries.

**Explicitly not here.** No ranking, no readiness percentage, no promotion
suggestion. The maintainer looks at the evidence and decides.

---

## V3 — Repository memory, and the first audition

Sketched, not settled. V3 is the first version where a language model is
permitted to exist at all, so it gets designed after V0 through V2 have shipped
and there is something real to argue against. What follows is the shape, and the
audition table in `0001` is the part to argue with.

- Deterministic retrieval first: full-text and trigram search over historical
  PR and issue discussion, filtered by area, decision-bearing events, and
  outcome. This ships and is useful with no model at all.
- **Then** the audition, run as written in `docs/design/0001-llm-boundary.md`:
  summarising a 200-comment thread whose candidates deterministic retrieval
  already found. It ships only if the deterministic version demonstrably fails at
  something a maintainer needs, and the failure is recorded in the audition
  record alongside it.
- Enrichment renders in its own register, is off by default, and cannot be an
  input to any state transition.

**Acceptance.** Uninstalling every model dependency leaves Steward fully
functional, with one feature visibly absent and no state changed. This is a test,
run in CI, not a principle in a README.

---

## V4 — Live

- GitHub App with webhooks; sync stops being a poll.
- Multiple maintainers against one Steward instance, with per-person inboxes.
- Organisation view across repositories.

Deferred to here deliberately: webhooks are an ingestion optimisation, and
optimising ingestion before the thing it feeds is proven is how this project
would end up as another dashboard.

---

## Validation

Steward is tested by being used. There is no fixture loader and no hand-written
event JSON: tests drive `steward sync` and then assert on what a maintainer would
see. Five repositories are the test suite, each admitted because it fails
differently from the others — ruff presses every button, tokio presses almost
none, kubernetes keeps its state in bot labels, home-assistant runs an enormous
contributor funnel, Precogly self-merges in two minutes. Which repositories, what
each one catches, and what the corpus still has no example of are in
[`docs/corpus.md`](docs/corpus.md).

The one concession to CI: HTTP is recorded and replayed at the socket, so runs
are hermetic and offline. The normalizer's tests already work this way, through
`httpx.MockTransport`; what is missing is `steward sync` recording its own.
Everything above the socket — pagination, normalisation, the fold, the policy
layer, the queries — is the production path.
Cassettes are refreshed on a schedule, and a refresh that changes a coverage
number is a finding to read, not a number to update.

## Non-goals

- Steward never acts on its own. Nothing is merged, closed, labelled or
  commented on unless a maintainer asked for that action, and nothing runs on a
  schedule or on a rule.
- No contributor scores, health scores, or quality ratings.

Whether Steward writes to GitHub at all is open. Read-only keeps a property
worth something: the token can be read-only, so a stranger can check that
Steward cannot damage a repository before pointing it at one. Against that, a
workbench that can only watch leaves the maintainer switching tabs to act.

No longer a non-goal: replacing parts of GitHub's UI. Reviewing code is the
obvious candidate.
