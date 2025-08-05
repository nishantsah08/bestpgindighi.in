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

# Expose the port
EXPOSE 8080

# Run the application
CMD ["gunicorn", "-c", "gunicorn.conf.py", "internal_dashboard.backend.main:app"]
