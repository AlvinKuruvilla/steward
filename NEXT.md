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

3. **Sync.** The normalizer is done and runs clean over the corpus: 125 pull
   requests, 1,722 events, 130 requests. What is left between it and
   `steward sync`:

   - **Pagination.** Both `pulls.list` and the timeline are read one page deep.
     githubkit has `paginate`; nothing calls it yet, so a pull request with more
     than 100 timeline items is truncated -- the bug `fetch_prs.py` had.
   - **The subjects snapshot.** `PullRequestSimple` carries title, draft state,
     base and head refs, and nothing writes them to `subjects`.
   - **Recording.** `tests/data/precogly_rest_timeline.json` was recorded by
     hand. `steward sync` should be able to record its own cassettes, which is
     what ROADMAP.md's hermetic test story rests on.
   - **Writing rows,** which needs the migration runner below.

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
