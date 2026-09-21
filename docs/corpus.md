# The validation corpus

Steward is tested by being run against real repositories, so the list of
repositories is part of the design rather than a detail of the test suite. This
file is the record of what is in it and why.

A repository earns a place by **failing differently** from the ones already
there. Adding a sixth repository that behaves like ruff buys nothing; adding one
that keeps its state somewhere the engine does not look buys a bug.

Measurements quoted below were taken 2026-09-21 and are the ones in
[`audit/2026-09-21-contribution-flow.md`](audit/2026-09-21-contribution-flow.md).
They are a snapshot, not a contract — a corpus refresh that moves them is a
finding to read, not a number to edit.

## In the corpus

### precogly/precogly

The repository the project exists for, and the reason the plan changed. 157
stars, Apache-2.0, TypeScript and Python, first release April 2026.

*Catches:* repositories that barely use GitHub's review machinery. 12.2% of PRs
carry a review request, 75.2% of merged PRs carry no approval, and 67% of
internal PRs merge within five minutes of opening. Bare deterministic coverage is
**13.3%** — the worst in the corpus by a wide margin, and the reason the policy
layer is V1 work rather than V2 work.

*Also catches:* bot-dominated queues. 13 of 15 open PRs are bots.

*Cannot validate:* that Steward finds review bottlenecks, because it has none.
Precogly is the ergonomics test, not the correctness test.

### astral-sh/ruff

High-volume, professionally maintained, disciplined about GitHub's affordances.

*Catches:* the happy path, and regressions in it. 67.7% review-request usage,
68.7% draft usage, bare coverage **100%**. If ruff ever drops below 100% the
engine broke, because ruff is not going to stop pressing the button.

*Also catches:* heavy draft use — 49 of 86 open PRs are drafts, so draft interval
reconstruction is exercised constantly.

### tokio-rs/tokio

The inverse of ruff. Careful review culture, almost no formal review requests.

*Catches:* the gap between social workflow and recorded workflow. 9.3%
review-request usage against **0% of merged PRs lacking an approval** — every PR
gets approved, nobody ever asks. Bare coverage **39.4%**, and 67.7% of merged-PR
lifetime lands in the no-signal bucket.

This is the repository that proves the policy layer is doing real work rather
than papering over a bug. Tokio is not disorganised; it just does not narrate.

### kubernetes/kubernetes

State lives in bot labels, not in GitHub's review objects. Prow drives
`lgtm`, `approved`, `do-not-merge/*`, `needs-rebase`, `needs-ok-to-test`.

*Catches:* repositories whose real state machine is a bot the engine knows
nothing about. Bare coverage **79.7%**, 55.6% of merged PRs with no GitHub
approval — because the approval is a label, not a review. 263 `COMMENTED` reviews
against 27 approvals.

*Also catches:* scale. Large timelines, heavy pagination, high event counts per
PR.

*Open question this repo raises:* whether `steward.toml` should be able to map a
label to a state. Deliberately unanswered until V1 has run against it.

### home-assistant/core

The largest contributor funnel available, and the strictest process.

*Catches:* review-request saturation (97.0% of PRs) and a near-zero
merge-without-approval rate (1.1%). Bare coverage **98.1%**.

*Also catches:* the issue side. 217 open issues in a 12-day window, 61% of
external ones with no reply yet — a very different shape from Precogly's 78% at a
median age of 28 days. The contrast is what makes the reply window a per-repo
calibration rather than a constant.

## Gaps, and candidates to fill them

None of these have been measured. They are named here so the corpus grows on
purpose rather than by whoever is nearest.

| gap | why it matters | candidate |
|---|---|---|
| merge queue | A queued PR is approved, mergeable, and waiting on nothing a human can act on. The engine currently has no state for it and would report `APPROVED`/blocked-on-merger, which is wrong. | `rust-lang/rust` (bors), or any repo on GitHub's native merge queue |
| required reviewers via branch protection | Approval counts and CODEOWNERS fan-out change who `blocked_on` should name. Steward reads neither today. | a repo with protected branches and a populated `CODEOWNERS` |
| the long tail | Every corpus member is busy. Most OSS repositories get a PR a month, and a state machine tuned on busy repos can be unusably noisy on quiet ones. | a <500-star repo with genuine external contribution |
| an actual maintainer-bottleneck repo | The whole premise is repositories where review latency hurts. Not one corpus member demonstrably has that problem. | to be found — see below |
| issue data for kubernetes | Pulled PRs only, so the reply-window analysis covers four repos, not five. | `kubernetes/kubernetes` issues |

The fourth row is the important one. Steward is designed for a problem that no
repository in its own test corpus currently exhibits. V1 can ship on the
correctness bar without it, but the first time someone asks "does this actually
help anyone" the answer will have to come from a repository that hurts, and
finding one is work that should start before V1 lands rather than after.

## Rules for changing this list

- A repository joins with a written reason for what it catches that the others do
  not, added above.
- A repository does not leave because it started failing. That is the finding.
- Measurements in this file are refreshed by re-running the corpus, never edited
  by hand.
