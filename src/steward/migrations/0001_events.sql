-- The event log, and the snapshots that are not part of it.
--
-- Timestamps are UTC text shaped `2026-09-23T14:05:00Z`. SQLite has no timestamp
-- type, so every ordering by time is an ordering by string, and that holds only
-- while every row has the same shape. Each timestamp column checks that it
-- survives a round trip through strftime unchanged, which refuses other shapes
-- and dates that do not exist. `IS` and not `=`: strftime returns NULL for
-- input it cannot parse, and a CHECK that evaluates to NULL passes.

CREATE TABLE repositories (
    id         INTEGER PRIMARY KEY,
    owner      TEXT    NOT NULL,
    name       TEXT    NOT NULL,
    node_id    TEXT    NOT NULL UNIQUE,
    first_sync TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        CHECK (first_sync IS strftime('%Y-%m-%dT%H:%M:%SZ', first_sync)),
    last_sync  TEXT
        CHECK (last_sync IS strftime('%Y-%m-%dT%H:%M:%SZ', last_sync)),
    UNIQUE (owner, name)
) STRICT;

-- Append-only. Rows are immutable once written: no UPDATE, no DELETE, and the
-- only writer is the ingester. Everything Steward claims about a pull request is
-- a fold over this table, so anything that mutates here invalidates history that
-- was already shown to a maintainer. The triggers below refuse both.
CREATE TABLE events (
    id             INTEGER PRIMARY KEY,
    repo_id        INTEGER NOT NULL REFERENCES repositories(id),

    subject_type   TEXT    NOT NULL CHECK (subject_type IN ('pull_request', 'issue')),
    subject_number INTEGER NOT NULL,

    kind           TEXT    NOT NULL,
    occurred_at    TEXT    NOT NULL
        CHECK (occurred_at IS strftime('%Y-%m-%dT%H:%M:%SZ', occurred_at)),

    -- Nullable because GitHub returns a null author for deleted accounts, and a
    -- deleted account is a fact about the history rather than a broken row.
    actor          TEXT,
    -- REST's `type` on a user, verbatim. Bot-ness is a judgement on top of it:
    -- dependabot is type Bot, k8s-triage-robot is a User, and steward.toml's
    -- allowlist decides. Rows here are immutable, so the judgement must not be
    -- one of them. Unconstrained on purpose: a CHECK would fail the sync the
    -- day GitHub adds a type.
    actor_type     TEXT,

    -- Whatever the event kind carries beyond the columns above: a review's
    -- state, a label's name, a requested reviewer's login. A JSON object because
    -- the alternative is thirty nullable columns, twenty-eight of which are null
    -- on any given row.
    payload        TEXT    NOT NULL DEFAULT '{}'
        CHECK (json_valid(payload) AND json_type(payload) = 'object'),

    -- GitHub's node id where one exists, otherwise a synthesized stable key such
    -- as 'pr:551:opened'. This is what makes re-syncing idempotent, so it must be
    -- derivable from the event itself and never from ingestion order.
    source_id      TEXT    NOT NULL,

    ingested_at    TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        CHECK (ingested_at IS strftime('%Y-%m-%dT%H:%M:%SZ', ingested_at)),

    -- A commit's id is the commit's own, and one commit can sit on two pull
    -- requests, so identity is the item together with the subject it is on.
    UNIQUE (repo_id, subject_type, subject_number, source_id)
) STRICT;

CREATE INDEX events_subject_idx ON events (repo_id, subject_type, subject_number, occurred_at);
CREATE INDEX events_kind_idx    ON events (repo_id, kind, occurred_at);

CREATE TRIGGER events_no_update BEFORE UPDATE ON events
BEGIN
    SELECT RAISE(ABORT, 'events is append-only: rows are never updated');
END;

CREATE TRIGGER events_no_delete BEFORE DELETE ON events
BEGIN
    SELECT RAISE(ABORT, 'events is append-only: rows are never deleted');
END;
