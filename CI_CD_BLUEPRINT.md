# CI/CD Pipeline Blueprint for FastAPI Deployment

**Date:** Wednesday, August 6, 2025

## 1. Objective

To establish an automated CI/CD pipeline using GitHub Actions. The pipeline must build a Docker image from the project's source code, push it to Google Artifact Registry (GAR), and subsequently deploy it as a service on Google Cloud Run.

---

## 2. Core Project & Service Identifiers

*   **Google Cloud Project ID:** `fir-bestpg`
*   **Google Cloud Project Number:** `1020918069137`
*   **CI/CD Service Account Email:** `firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com`
*   **GitHub Repository:** `nishantsah08/bestpgindighi.in`

---

## 3. Asset & Code Locations

*   **Source Code Directory:** The primary application source code is located in `/src/internal_dashboard/backend/`.
*   **Dockerfile Location:** The `Dockerfile` is located at the root of the repository.
*   **Target Artifact Registry (GAR) Repository:**
    *   **Name:** `cloud-run`
    *   **Location:** `asia-south1` (Mumbai)
    *   **Format:** Docker
*   **Target Cloud Run Service:**
    *   **Service Name:** `api-backend`
    *   **Deployment Region:** `asia-south1` (Mumbai)

---

## 4. Pipeline Requirements

*   **Trigger:** The workflow must automatically execute upon any `push` to the `walking-skeleton` branch.
*   **Authentication:** The pipeline must authenticate to Google Cloud using the specified CI/CD Service Account. The necessary credentials will be provided via a GitHub secret named `GCP_SA_KEY`.
*   **Build Process:** The pipeline must successfully build a Docker image using the provided `Dockerfile`.
*   **Push Process:** The resulting Docker image must be tagged with the Git commit SHA and pushed to the `cloud-run` repository in Google Artifact Registry.
*   **Deploy Process:** The newly pushed image must be deployed to the `api-backend` service in Cloud Run. The service should be configured to allow unauthenticated invocations.

---

## 5. Dockerfile Content

```dockerfile
# 1. Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# 2. Set environment variables.
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files.
# PYTHONUNBUFFERED: Sends logs straight to the terminal.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory.
WORKDIR /app

# 4. Install system dependencies.
# We install git to be able to install packages from git repositories.
# We install curl to be able to check the health of the application.
RUN apt-get update && apt-get install -y --no-install-recommends git curl

# 5. Install Python dependencies.
# We use a virtual environment to isolate our dependencies.
COPY src/internal_dashboard/backend/requirements.txt .
RUN python -m venv /venv
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# 6. Copy the application code.
COPY . .

# 7. Expose the port the app runs on.
EXPOSE 8080

# 8. Set the entrypoint.
# We use gunicorn to run the application.
CMD ["/venv/bin/gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.internal_dashboard.backend.main:app", "--bind", "0.0.0.0:8080"]
```
