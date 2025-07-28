# --- Stage 1: Builder ---
FROM python:3.11-slim as builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY src/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 2: Runtime ---
FROM python:3.11-slim

RUN groupadd --system nonroot && useradd --system --group nonroot nonroot
USER nonroot

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY . .

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8080

CMD ["exec", "gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "src.backend.main:app", "-k", "uvicorn.workers.UvicornWorker"]
