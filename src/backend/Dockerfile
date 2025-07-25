# Dockerfile

# Stage 1: Builder
FROM python:3.11-slim-bookworm AS builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runner
FROM python:3.11-slim-bookworm AS runner

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN adduser --system --group appuser
USER appuser

COPY --from=builder /opt/venv /opt/venv
COPY . /app/backend

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8080

CMD uvicorn backend.main:app --host 0.0.0.0 --port ${PORT}