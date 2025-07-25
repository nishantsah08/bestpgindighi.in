# Stage 1: Builder - Install dependencies
FROM python:3.11-slim-bookworm AS builder

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a directory for your application and set it as the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final - Copy application code and installed dependencies
FROM python:3.11-slim-bookworm AS runner

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a directory for your application and set it as the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv

# Ensure the virtual environment is activated in the final image
ENV PATH="/venv/bin:$PATH"

# Copy your application code
COPY . .

# Expose the port Cloud Run will use (default is 8080)
EXPOSE 8080

# Create a non-root user and switch to it
RUN adduser --system --group appuser
USER appuser

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT:-8080}"]
