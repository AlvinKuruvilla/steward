-- The application's database, and the tests'.
--
-- The tests drop every table in `public` between cases, so they need a
-- database that is not the one a developer syncs into.

CREATE DATABASE steward_test;

\connect steward
\ir per-database.psql

\connect steward_test
\ir per-database.psql
