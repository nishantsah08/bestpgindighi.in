FROM python:3.11.9-slim-bookworm

WORKDIR /app

COPY src/internal_dashboard/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

RUN groupadd --system appgroup && useradd --system --group appgroup appuser
USER appuser

WORKDIR /app/src

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--workers", "1", "--threads", "8", "--timeout", "0", "internal_dashboard.backend.main:app", "-k", "uvicorn.workers.UvicornWorker"]
