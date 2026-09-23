# Steward's commands. `just` with no argument lists them.

set dotenv-load := true
set quiet := true

github_token := env("GITHUB_TOKEN", `gh auth token 2>/dev/null || echo ""`)

# Development keeps its own database. Without --data-dir the backend uses the
# installed app's directory, and `just clean` would delete that app's data.
data_dir := "tmp/data"

default:
    @just --list

# The API, migrating on start. Add and sync repositories from the interface.
serve:
    GITHUB_TOKEN={{github_token}} uv run steward serve --data-dir {{data_dir}}

# Vite with hot reload, proxying /api to `just serve`.
web:
    cd web && pnpm dev

# A SQLite shell on the development database, for reading the log directly.
db:
    sqlite3 {{data_dir}}/steward.db

# Throw the development database away. Everything in it can be synced again.
clean:
    rm -rf {{data_dir}}

# Each test makes its own database file, so this never touches tmp/data.
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
