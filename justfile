# Steward's commands. `just` with no argument lists them.

set dotenv-load := true
set quiet := true

github_token := env("GITHUB_TOKEN", `gh auth token 2>/dev/null || echo ""`)
admin_url := "postgresql://steward_migrator:steward-dev@127.0.0.1:5432/steward?options=-c%20role%3Dsteward_owner"
engine_url := "postgresql://steward_engine:steward-dev@127.0.0.1:5432/steward"

default:
    @just --list

# Build and start Postgres and the server, on loopback.
up:
    GITHUB_TOKEN={{github_token}} docker compose up -d --build --wait
    @echo "http://127.0.0.1:8000"

down:
    GITHUB_TOKEN={{github_token}} docker compose down

# Stop, and throw the data away with it.
clean:
    GITHUB_TOKEN={{github_token}} docker compose down -v

# Read a repository's history into the log. `just sync astral-sh/ruff`
sync repository:
    GITHUB_TOKEN={{github_token}} docker compose run --rm steward sync {{repository}}

# One pull request's event stream. `just events precogly/precogly 322`
events repository number:
    STEWARD_DATABASE_URL="{{engine_url}}" uv run steward events {{repository}} {{number}}

# The API and interface outside Docker, against the compose database.
serve:
    STEWARD_DATABASE_URL="{{engine_url}}" uv run steward serve

# Vite with hot reload, proxying /api to `just serve`.
web:
    cd web && pnpm dev

migrate:
    STEWARD_ADMIN_DATABASE_URL="{{admin_url}}" uv run steward migrate

# Tests use `steward_test` and skip when no database is up, so this is safe to
# run against a database you have synced into.
test *args:
    uv run pytest {{args}}

check:
    uv run ruff format --check src tests
    uv run ruff check src tests
    uv run mypy --strict src/steward
    uv run mypy tests
    uv run pytest -q
    cd web && pnpm exec tsc --noEmit -p tsconfig.app.json

fix:
    uv run ruff format src tests
    uv run ruff check --fix src tests

# From nothing to a populated interface. A shortcut, not a dependency: the app
# adds and syncs a repository from its own interface.
fresh repository="precogly/precogly": clean up
    just sync {{repository}}
    @echo "http://127.0.0.1:8000"
