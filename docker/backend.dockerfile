FROM ghcr.io/astral-sh/uv:debian-slim AS builder

COPY docker/entrypoint.sh /

WORKDIR /app

COPY backend/pyproject.toml .
COPY backend/uv.lock .

RUN uv venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
RUN uv sync
