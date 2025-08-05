FROM python:3.11.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY src/internal_dashboard/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

WORKDIR /app/src

# Use shell form so $PORT expands; keep uvicorn worker
CMD gunicorn -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 \
    internal_dashboard.backend.main:app