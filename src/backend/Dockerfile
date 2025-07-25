# Dockerfile

# Stage 1: Builder
FROM python:3.11-slim-bookworm AS builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Runner
FROM python:3.11-slim-bookworm AS runner

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN adduser --system --group appuser
USER appuser

COPY --from=builder /opt/venv/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . /app/backend

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8080

CMD uvicorn backend.main:app --host 0.0.0.0 --port ${PORT}