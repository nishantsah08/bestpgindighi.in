FROM python:3.11.9-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY src/internal_dashboard/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY ./src ./src

# Create and switch to a non-root user
RUN groupadd --system appgroup && useradd --system --group appgroup appuser
USER appuser

# Set the working directory to the source code
WORKDIR /app/src

# Expose the port and run the application
EXPOSE 8080
CMD gunicorn --bind "0.0.0.0:$PORT" --workers 1 --threads 8 --timeout 0 "internal_dashboard.backend.main:app" -k uvicorn.workers.UvicornWorker