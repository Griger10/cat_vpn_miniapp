FROM python:3.13.7-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app/backend

COPY backend/pyproject.toml .

RUN uv sync

FROM python:3.13.7-slim

ENV PYTHONPATH="${PYTHONPATH}:/app/backend/src/"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/app/backend/.venv
ENV PATH="/app/backend/.venv/bin:${PATH}"

WORKDIR /app

COPY --from=builder /app/backend/.venv /app/backend/.venv

COPY . .