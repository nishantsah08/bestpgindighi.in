FROM python:3.11.9-slim-bookworm

# Set the working directory
WORKDIR /app

# Set the venv path
ENV VENV_PATH="/opt/venv"
ENV PATH="$VENV_PATH/bin:$PATH"

# Create and activate the virtual environment
RUN python3 -m venv $VENV_PATH

# Copy requirements and install dependencies
COPY src/internal_dashboard/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY ./src ./src

# Set the user for the container
RUN groupadd --system appgroup && useradd --system --group appgroup appuser
USER appuser

# Expose the port
EXPOSE 8080

# Run the application
CMD ["/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "internal_dashboard.backend.main:app", "-k", "uvicorn.workers.UvicornWorker"]
