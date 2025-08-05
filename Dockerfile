FROM python:3.11.9-slim-bookworm as builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY src/internal_dashboard/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 2: Runtime ---
FROM python:3.11.9-slim-bookworm

RUN groupadd --system appgroup && useradd --system --group appgroup appuser
USER appuser

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY ./src ./src

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8080

CMD ["/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "internal_dashboard.backend.main:app", "-k", "uvicorn.workers.UvicornWorker"]