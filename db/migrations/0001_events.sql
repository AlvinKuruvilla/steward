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
    -- GraphQL's __typename. Bot-ness is a judgement on top of it: dependabot is
    -- __typename Bot, k8s-triage-robot is a User, and steward.toml's allowlist
    -- decides. Rows here are immutable, so the judgement must not be one of them.
    -- Unconstrained on purpose: a CHECK or an enum would fail the sync the day
    -- GitHub adds a __typename.
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

-- Not the log.
--
-- A pull request's title, size, author and head branch are mutable attributes
-- that GitHub emits no event for. They cannot be folded out of `events` because
-- nothing in `events` records them changing, so they are stored as a snapshot,
-- last-writer-wins, refreshed on every sync.
--
-- The state engine reads `events` and never this table. A snapshot can go stale
-- or be overwritten; a claim about who a PR is waiting on must not depend on
-- something that can. This table exists so the UI can render "#551 rootless
-- Podman overlay, +161/-0" next to a state that was derived without it.
CREATE TABLE subjects (
    repo_id        BIGINT      NOT NULL REFERENCES repositories(id),
    subject_type   TEXT        NOT NULL CHECK (subject_type IN ('pull_request', 'issue')),
    subject_number INTEGER     NOT NULL,

    node_id        TEXT        NOT NULL,
    title          TEXT        NOT NULL,
    author         TEXT,
    author_is_bot  BOOLEAN     NOT NULL DEFAULT false,
    -- GitHub's association at sync time, not at the time the PR was opened. A
    -- contributor promoted to MEMBER reads as MEMBER across their whole history,
    -- which understates the external cohort in any repo that promotes people.
    author_association TEXT,

    state          TEXT        NOT NULL,
    is_draft       BOOLEAN     NOT NULL DEFAULT false,
    created_at     TIMESTAMPTZ NOT NULL,
    closed_at      TIMESTAMPTZ,
    merged_at      TIMESTAMPTZ,

    additions      INTEGER,
    deletions      INTEGER,
    changed_files  INTEGER,
    base_ref       TEXT,
    head_ref       TEXT,
    labels         TEXT[]      NOT NULL DEFAULT '{}',

    synced_at      TIMESTAMPTZ NOT NULL DEFAULT now(),

    PRIMARY KEY (repo_id, subject_type, subject_number)
);
