# Next steps

Working notes. Deliverables and their acceptance bars live in `ROADMAP.md`;
deferred problems live in `SESSION.md`.

## V0

`model.py` is done: `Event`, `validate_payload`, and the `payload_to_dict` /
`payload_from_dict` pair with a hypothesis property test over every shape.

1. **Migration runner.** Walked through but not written. Settled: numbered SQL
   with a `schema_migrations` ledger, SHA-256 checksums to catch an edited
   migration, one transaction per file, `pg_advisory_lock` around the run,
   forward-only. Two things still open:

   - **Where migrations live.** They are in `db/migrations/`, which breaks the
     moment Steward is installed as a wheel. Moving them to
     `src/steward/migrations/` needs a hatchling force-include so `.sql` ships.
   - **Which role runs them.** Must be `steward_owner`, or
     `ALTER DEFAULT PRIVILEGES` never fires and `steward_engine` silently gets no
     grants. `steward_owner` is NOLOGIN, so the runner connects as superuser and
     issues `SET ROLE`. That is a second connection string, which `compose.yaml`
     does not yet provide.

2. **Dockerfile.** `compose.yaml` declares `build: .` and there is no Dockerfile.

3. **The normalizer.** The query and the client are generated from the pinned
   schema (`scripts/generate.sh`), so fetching wide is settled: all 78 timeline
   types, 1 rate-limit point per page of 25 PRs. What is left is mapping the
   generated models onto `Event`, through `validate_payload`.

   Blocked on one decision: single-tier or two-tier. A typed client makes the
   raw tier cheap — store the response model, derive `events` from it — and
   until that is settled the normalizer has no target to write to.

4. **`steward sync` / `steward events`,** then V0's acceptance: sync twice and
   add zero rows; truncate everything below the log, replay, diff identical.

## Decisions still open

- Migration file location (1 above).
- Whether `steward.toml` may map a label to a state. Raised by kubernetes, which
  keeps its real state machine in bot-applied labels. Deliberately unanswered
  until V1 has run against it — see `docs/corpus.md`.

## Settled this session

PRs before issues for V1. Python backend, PostgreSQL, self-hosted via compose,
Apache-2.0. Single-tier event log, so the ingestion query must fetch wide.
Typed union for `Event.payload` over `dict[str, Any]`, because the bug it
prevents is a normalizer typo that produces a fold branch which silently never
fires.

The flat `Event` stays; one dataclass per kind was prototyped and rejected — see
`SESSION.md` for the costs that buys. `PAYLOAD_FOR` is enforced by
`validate_payload()`, which the normalizer calls and the replay decoder does not.
