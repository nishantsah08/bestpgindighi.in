FROM python:3.11.9-slim-bookworm

WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Set the shell to run subsequent commands inside the venv
SHELL ["/bin/bash", "-c", "source /opt/venv/bin/activate && exec \"$@\""]

# Install dependencies inside the venv
COPY src/internal_dashboard/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY ./src ./src

# Create and switch to a non-root user
RUN groupadd --system appgroup && useradd --system --group appgroup appuser
USER appuser

WORKDIR /app/src

# Expose the port and run the application
EXPOSE 8080
CMD gunicorn --bind "0.0.0.0:$PORT" --workers 1 --threads 8 --timeout 0 "internal_dashboard.backend.main:app" -k uvicorn.workers.UvicornWorker