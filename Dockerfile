FROM python:3.13-slim AS build

COPY --from=ghcr.io/astral-sh/uv:0.9.13 /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /app

# Dependencies alone, so this layer survives changes to src/.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# README.md is here because pyproject.toml declares it; the build fails without it.
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
# --no-editable, or the venv points at /app/src and the runtime stage has none.
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-dev --no-editable


FROM python:3.13-slim

RUN useradd --create-home --uid 1000 steward
USER steward
WORKDIR /app

COPY --from=build --chown=steward:steward /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

ENTRYPOINT ["steward"]
CMD ["--help"]
