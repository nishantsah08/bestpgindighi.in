# Docker Best Practices

This document outlines the best practices for building and running Python applications in Docker within this project.

## 1. Application Structure and Relative Imports

Our Python applications are structured as packages. This means that they use relative imports to access different parts of the application (e.g., `from . import database`).

To ensure that these relative imports work correctly, the application must be run as a module, not as a script.

## 2. Dockerfile Configuration

The following `Dockerfile` configuration has been proven to work correctly with our application structure:

```Dockerfile
FROM python:3.11-slim-bookworm

WORKDIR /app

COPY src/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/backend/test_main.py .

EXPOSE 8080

CMD ["python3", "-m", "uvicorn", "test_main:app", "--host", "0.0.0.0", "--port", "8080"]
```

## 3. Running the Container

To run the container locally, use the following command:

```bash
docker run -p 8080:8080 -e PORT=8080 bestpg-backend-local
```

This command maps the container's port 8080 to the host's port 8080 and sets the `PORT` environment variable, which is used by the application.
