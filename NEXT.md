# Next steps

Working notes. Deliverables and their acceptance bars live in `ROADMAP.md`.

## V0

`model.py` is done: `Event`, `validate_payload`, and the `payload_to_dict` /
`payload_from_dict` pair with a hypothesis property test over every shape.

1. **Sync.** `fetch.events()` reads a whole repository through paged requests
   and normalizes it: precogly's full history is 259 pull requests and 1,889
   events, no failures. What is left between that and `steward sync`:

   - **Resumability.** A sync reads every pull request every time, which a
     backfill of precogly does in 28 seconds. Stopping early on `updated_at` is
     ruled out: `pulls.list` has no `since`, and 7 of 25 recorded pull requests
     have an event after their own `updated_at` -- all cross-references, which
     update the issue doing the referencing and not the pull request referred
     to. Webhooks (V4) are the real answer.
   - **Recording.** `tests/data/precogly_rest_timeline.json` was recorded by
     hand. `steward sync` should record its own cassettes, which is what
     ROADMAP.md's hermetic test story rests on.
   - **Writing rows,** which needs the migration runner above.

2. **`steward sync` / `steward events`,** then V0's acceptance: sync twice and
   add zero rows; truncate everything below the log, replay, diff identical.

## Known problems

- Changing what an event carries needs the log rebuilt, not re-synced. Writes
  are `ON CONFLICT DO NOTHING` on the source id, so an existing row keeps its
  old payload: adding the title to OPENED left every already-synced pull
  request without one until the events were dropped and read again. The
  append-only triggers now refuse that drop, so rebuilding means deleting the
  database file (`just clean`) and syncing again.

## Decisions still open

- Whether Steward writes to GitHub at all. Acting on its own is ruled out;
  human-initiated writes are not. It decides whether the token and `steward.toml`
  ever carry a write scope, so it is cheaper to settle
  before V1 ships a UI with buttons on it.
- Whether `steward.toml` may map a label to a state. Raised by kubernetes, which
  keeps its real state machine in bot-applied labels. Deliberately unanswered
  until V1 has run against it — see `docs/corpus.md`.

## Settled this session

PRs before issues for V1. Python backend, PostgreSQL, self-hosted via compose,
Apache-2.0. Single-tier event log, so the ingestion query must fetch wide.
Typed union for `Event.payload` over `dict[str, Any]`, because the bug it
prevents is a normalizer typo that produces a fold branch which silently never
fires.

The flat `Event` stays; one dataclass per kind was prototyped and rejected. Every
payload-touching fold branch will narrow by hand, and a kind paired with the
wrong shape type-checks. `PAYLOAD_FOR` is enforced by `validate_payload()`,
which the normalizer calls and the replay decoder does not.
