FROM node:26-slim AS interface

WORKDIR /web
# corepack is not in node:26 images.
RUN npm install --global pnpm@9
COPY web/package.json web/pnpm-lock.yaml ./
RUN --mount=type=cache,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile
COPY web/ ./
RUN pnpm build


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

# Served by the API at /, so one container holds both.
COPY --from=interface --chown=steward:steward /web/dist /app/.venv/lib/python3.13/site-packages/steward/web

EXPOSE 8000
ENTRYPOINT ["steward"]
CMD ["--help"]
