-- Roles and schemas for Steward.
--
-- Steward connects as steward_engine. Enrichment output -- anything a language
-- model produced -- lives in the `enrichment` schema, and steward_engine holds
-- no privileges on it: not SELECT, not USAGE. Engine code cannot read model
-- output because the database refuses the query. Crossing the boundary means
-- editing this file, where a reviewer will see it.
--
-- Runs once, on an empty data directory. Changing it will not affect an existing
-- volume; a privilege change needs a migration as well as an edit here.

\set engine_password `echo "${STEWARD_ENGINE_PASSWORD:-steward-dev}"`
\set enrich_password `echo "${STEWARD_ENRICH_PASSWORD:-steward-dev}"`
\set migrator_password `echo "${STEWARD_MIGRATOR_PASSWORD:-steward-dev}"`

-- Owns every object. NOLOGIN: nothing authenticates as it.
CREATE ROLE steward_owner NOLOGIN;

-- Runs migrations. Membership carries the SET option, so it can SET ROLE to
-- steward_owner without being a superuser; the admin connection string does
-- that on connect, with `options=-c role=steward_owner`.
CREATE ROLE steward_migrator LOGIN PASSWORD :'migrator_password';
GRANT steward_owner TO steward_migrator;

-- The application. Reads events, writes derived state.
CREATE ROLE steward_engine LOGIN PASSWORD :'engine_password';

-- Writes enrichment. Unused until V3, created now so the boundary predates
-- anything that might want to cross it.
CREATE ROLE steward_enrich LOGIN PASSWORD :'enrich_password';
