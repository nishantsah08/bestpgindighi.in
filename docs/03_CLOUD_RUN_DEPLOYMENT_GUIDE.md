# Cloud Run Deployment Guide

This document outlines the best practices and common solutions for deploying applications to Google Cloud Run within this project, specifically addressing issues encountered during the initial setup of the FastAPI backend and React internal dashboard.

## General Principles for Cloud Run Deployment

1.  **Containerization is Key:** Cloud Run deploys containerized applications. A well-structured `Dockerfile` is crucial for successful deployments.
2.  **Listen on `PORT` Environment Variable:** Cloud Run injects a `PORT` environment variable into your container. Your application *must* listen on this port (typically 8080) for Cloud Run to route traffic correctly. Do not hardcode ports.
3.  **Health Checks:** Cloud Run performs health checks to determine if your container is ready to receive traffic. Ensure your application starts and responds to requests within the allocated startup time.
4.  **Logging:** Utilize standard output (stdout) and standard error (stderr) for application logs. Cloud Run automatically collects these logs, which are invaluable for debugging.

## Python (FastAPI) Backend Deployment

### Dockerfile Structure (Multi-Stage Build)

For Python applications, a multi-stage `Dockerfile` is highly recommended. This approach separates the build environment (where dependencies are installed) from the runtime environment (which contains only the necessary components), resulting in smaller, more secure images.

```dockerfile
# Stage 1: Builder - Install dependencies
FROM python:3.11-slim-bookworm AS builder

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a directory for your application and set it as the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Create a virtual environment and install dependencies into it
# This isolates dependencies and ensures they are correctly packaged.
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"  # Add venv to PATH for this stage
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final - Copy application code and installed dependencies
FROM python:3.11-slim-bookworm AS runner

# Set environment variables for Python (repeated for clarity in this stage)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a directory for your application and set it as the working directory
WORKDIR /app

# Copy the entire virtual environment from the builder stage
COPY --from=builder /venv /venv

# Ensure the virtual environment is activated in the final image's PATH
ENV PATH="/venv/bin:$PATH"

# Copy your application code
# Ensure this path matches your project structure. For this project, it's `/src/backend`.
COPY . .

# Expose the port Cloud Run will use (default is 8080)
EXPOSE 8080

# Create a non-root user and switch to it for security best practices
RUN adduser --system --group appuser
USER appuser

# Command to run the application using uvicorn
# Cloud Run injects the PORT environment variable, which uvicorn will pick up.
# The `main:app` refers to the FastAPI application instance in `main.py`.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### `requirements.txt`

Ensure all direct and indirect Python dependencies are listed in `requirements.txt`. Use pinned versions (`==`) for reproducibility.

Example:

```
fastapi==0.111.0
uvicorn[standard]==0.30.1
sqlalchemy
passlib
python-jose
```

## React (Internal Dashboard) Deployment

For single-page applications like React, the build process generates static files that need to be served by a web server (e.g., Nginx). A multi-stage Dockerfile is also beneficial here.

### Dockerfile Structure

```dockerfile
# Stage 1: Build the React app
FROM node:20-alpine as builder

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . ./
RUN npm run build

# Stage 2: Serve the static files with a web server
FROM nginx:1.25-alpine

# Copy the built React app from the builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Copy the custom Nginx configuration
# This is crucial to make Nginx listen on the Cloud Run assigned port (8080).
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080 as required by Cloud Run
EXPOSE 8080

# Start nginx with the custom configuration
CMD ["nginx", "-g", "daemon off;"]
```

### `nginx.conf` (Custom Configuration)

Create an `nginx.conf` file in the same directory as your `Dockerfile` (e.g., `src/internal_dashboard/nginx.conf`) to configure Nginx to listen on port 8080 and serve your static files.

```nginx
events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;

    sendfile on;
    keepalive_timeout 65;

    server {
        listen 8080;  # Nginx must listen on the Cloud Run assigned port
        server_name localhost;

        location / {
            root /usr/share/nginx/html;
            index index.html index.htm;
            try_files $uri $uri/ /index.html; # Handles client-side routing
        }
    }
}
```

## Troubleshooting "Container failed to start" Errors

This is a common error on Cloud Run and usually indicates that your application inside the container is not starting correctly or not listening on the expected port.

1.  **Check Cloud Run Logs:** The most important step is to examine the logs for the failed revision. The Cloud Run console provides a direct link to the logs for failed deployments. Look for `stdout` and `stderr` messages from your application.
    *   **`ModuleNotFoundError`:** Indicates a missing Python dependency. Add it to `requirements.txt` and rebuild.
    *   **`uvicorn: not found`:** Ensure `uvicorn` is installed in the final image and its executable is in the `PATH` (handled by the virtual environment approach in the Python Dockerfile).
    *   **Port Mismatch:** Verify that your application/web server is listening on the `PORT` environment variable (8080 by default for Cloud Run). For Nginx, this means configuring `listen 8080;` in `nginx.conf`.
2.  **Local Testing:** Build and run your Docker image locally to reproduce the issue and debug interactively.
    ```bash
    docker build -t my-app:latest .
    docker run -p 8080:8080 my-app:latest
    ```
    Then try to access `http://localhost:8080`.
3.  **Health Check Timeout:** If your application takes a long time to start, you might need to increase the startup probe timeout in your Cloud Run service settings.

By following these guidelines and leveraging the provided Dockerfile examples, future deployments to Cloud Run should be much smoother.