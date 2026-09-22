-- The event log, and the snapshots that are not part of it.

CREATE TABLE repositories (
    id          BIGSERIAL PRIMARY KEY,
    owner       TEXT        NOT NULL,
    name        TEXT        NOT NULL,
    node_id     TEXT        NOT NULL UNIQUE,
    first_sync  TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_sync   TIMESTAMPTZ,
    UNIQUE (owner, name)
);

-- Append-only. Rows are immutable once written: no UPDATE, no DELETE, and the
-- only writer is the ingester. Everything Steward claims about a pull request is
-- a fold over this table, so anything that mutates here invalidates history that
-- was already shown to a maintainer.
CREATE TABLE events (
    id          BIGSERIAL   PRIMARY KEY,
    repo_id     BIGINT      NOT NULL REFERENCES repositories(id),

    subject_type   TEXT     NOT NULL CHECK (subject_type IN ('pull_request', 'issue')),
    subject_number INTEGER  NOT NULL,

    kind        TEXT        NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL,

    -- Nullable because GitHub returns a null author for deleted accounts, and a
    -- deleted account is a fact about the history rather than a broken row.
    actor       TEXT,
    -- REST's `type` on a user, verbatim. Bot-ness is a judgement on top of it:
    -- dependabot is type Bot, k8s-triage-robot is a User, and steward.toml's
    -- allowlist decides. Rows here are immutable, so the judgement must not be
    -- one of them. Unconstrained on purpose: a CHECK would fail the sync the
    -- day GitHub adds a type.
    actor_type  TEXT,

    -- Whatever the event kind carries beyond the columns above: a review's
    -- state, a label's name, a requested reviewer's login. Kept as JSONB because
    -- the alternative is thirty nullable columns, twenty-eight of which are null
    -- on any given row.
    payload     JSONB       NOT NULL DEFAULT '{}'::jsonb,

    -- GitHub's node id where one exists, otherwise a synthesized stable key such
    -- as 'pr:551:opened'. This is what makes re-syncing idempotent, so it must be
    -- derivable from the event itself and never from ingestion order.
    source_id   TEXT        NOT NULL,

    ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE (repo_id, source_id)
);

CREATE INDEX events_subject_idx ON events (repo_id, subject_type, subject_number, occurred_at);
CREATE INDEX events_kind_idx    ON events (repo_id, kind, occurred_at);
