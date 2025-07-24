# Stage 1: The builder stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Stage 2: The production stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies and application code from the builder stage
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN apt-get update && apt-get install -y dos2unix && dos2unix entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
