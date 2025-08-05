# Troubleshooting Report: FastAPI Deployment Failure on Google Cloud Run

**Prepared on:** Tuesday, August 5, 2025

## 1. Overall Goal

The objective is to deploy a full-stack application consisting of a Python FastAPI backend and a static HTML/JS frontend. The backend is to be containerized and deployed to **Google Cloud Run** in the `asia-south1` (Mumbai) region. The frontend is deployed to **Firebase Hosting**. The entire process is intended to be automated via a GitHub Actions CI/CD pipeline.

## 2. System Architecture

*   **Backend:**
    *   Language/Framework: Python 3.11 with FastAPI.
    *   WSGI Server: `gunicorn` with `uvicorn` workers.
    *   Source Code: `src/internal_dashboard/backend/main.py`
*   **Frontend:**
    *   Static HTML page.
    *   Source Code: `src/public_website/index.html`
*   **Deployment Platform:**
    *   Backend: Google Cloud Run (managed).
    *   Frontend: Firebase Hosting.
*   **CI/CD:**
    *   GitHub Actions.
*   **Integration:**
    *   Firebase Hosting is configured with a rewrite rule to direct all requests starting with `/api/` to the Cloud Run service.

## 3. The Core Problem

The GitHub Actions workflow consistently fails at the final step: deploying the container to Google Cloud Run. The build process (creating the Docker image and pushing it to Google Artifact Registry) succeeds, but the Cloud Run service fails to start, resulting in a timeout and rollback.

The key error message from the Cloud Run logs has been consistent across the last several attempts:

```
Container called exit(0).
```

This indicates that the `gunicorn` process inside the container starts and then immediately terminates with a success code. Because the process does not remain running, the container has no listening service, causing the Cloud Run health check to fail and the deployment to be aborted.

## 4. Current Configuration Files

Here are the exact contents of the relevant configuration files for the latest attempt.

**`.github/workflows/deploy_to_cloud_run.yml`**
```yaml
name: Deploy to Cloud Run

on:
  push:
    branches:
      - walking-skeleton

env:
  PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
  REGION: asia-south1
  SERVICE_NAME: api-backend

jobs:
  deploy:
    name: Deploy to Cloud Run
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Google Auth
        uses: 'google-github-actions/auth@v1'
        with:
          credentials_json: '${{ secrets.GCP_SA_KEY }}'

      - name: Deploy to Cloud Run
        uses: 'google-github-actions/deploy-cloudrun@v1'
        with:
          service: ${{ env.SERVICE_NAME }}
          region: ${{ env.REGION }}
          source: .
          project_id: ${{ env.PROJECT_ID }}
          allow_unauthenticated: true
```

**`Dockerfile`**
```dockerfile
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

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--workers", "1", "--threads", "8", "--timeout", "0", "internal_dashboard.backend.main:app", "-k", "uvicorn.workers.UvicornWorker"]
```

**`src/internal_dashboard/backend/main.py`**
```python
import os
import sys
import uuid
import logging
from fastapi import FastAPI
from google.cloud import firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
print("--- SCRIPT START ---")
logging.info("Application starting up...")
print(f"Python version: {sys.version}")
print(f"PYTHONPATH: {os.getenv('PYTHONPATH')}")
print(f"Current working directory: {os.getcwd()}")

app = FastAPI()
print("FastAPI app instantiated.")

# --- Database Connection ---
db = None
print("Attempting to connect to Firestore...")
logging.info("Attempting to connect to Firestore...")
try:
    if os.getenv('FIRESTORE_EMULATOR_HOST'):
        # Connect to the local emulator
        print("Connecting to Firestore emulator...")
        logging.info("Connecting to Firestore emulator...")
        db = firestore.Client(
            project="local-dev" # Use a dummy project ID for the emulator
        )
    else:
        # Connect to the real Firestore database in production
        print("Connecting to production Firestore...")
        logging.info("Connecting to production Firestore...")
        db = firestore.Client()
    print("Firestore connection successful.")
    logging.info("Firestore connection successful.")
except Exception as e:
    print(f"Error connecting to Firestore: {e}")
    logging.error(f"Error connecting to Firestore: {e}")
# --- End Database Connection ---


@app.get("/api/test_db")
async def test_db():
    """
    Performs a simple write and read to the database to confirm connection.
    """
    print("Received request for /api/test_db")
    logging.info("Received request for /api/test_db")
    try:
        doc_id = str(uuid.uuid4())
        doc_ref = db.collection(u'walking_skeleton').document(doc_id)
        
        # Write to DB
        print(f"Writing to document: {doc_id}")
        logging.info(f"Writing to document: {doc_id}")
        doc_ref.set({
            u'message': u'Hello from the backend!',
            u'timestamp': firestore.SERVER_TIMESTAMP
        })
        print("Write successful.")
        logging.info("Write successful.")

        # Read from DB
        print("Reading from document...")
        logging.info("Reading from document...")
        doc = doc_ref.get()
        if doc.exists:
            print("Read successful.")
            logging.info("Read successful.")
            return {"status": "ok", "data": doc.to_dict()}
        else:
            print("Document not found after write.")
            logging.warning("Document not found after write.")
            return {"status": "error", "message": "Document not found after write."}

    except Exception as e:
        print(f"Error in test_db: {e}")
        logging.error(f"Error in test_db: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/api/health")
def read_root():
    print("Received request for /api/health")
    logging.info("Received request for /api/health")
    return {"status": "ok"}

@app.get("/api/test")
def test_endpoint():
    print("Received request for /api/test")
    logging.info("Received request for /api/test")
    return {"status": "ok", "message": "Backend is live!"}

print("--- SCRIPT END ---")
logging.info("Application startup complete.")
```

**`src/internal_dashboard/backend/requirements.txt`**
```
fastapi
uvicorn
google-cloud-firestore
```

## 5. Summary of Failed Attempts

We have systematically tried to resolve this issue by modifying the `Dockerfile` and the `gunicorn` command. None of the following approaches have worked, all resulting in the same `Container called exit(0)` error.

1.  **`CMD` Variations:**
    *   Tried both the `exec` form (`CMD ["gunicorn", ...]`) and the `shell` form (`CMD gunicorn ...`). The `exec` form fails to substitute `$PORT`, and the `shell` form still results in an immediate exit.
2.  **Path and Environment:**
    *   Explicitly adding the venv to the `PATH` (`ENV PATH="/opt/venv/bin:$PATH"`).
    *   Using an absolute path to the executable (`CMD ["/opt/venv/bin/gunicorn", ...]`).
    *   Setting `PYTHONPATH` explicitly (`ENV PYTHONPATH=/app/src`).
3.  **Working Directory:**
    *   Setting `WORKDIR` to `/app` and calling the module as `src.internal_dashboard.backend.main:app`.
    *   Setting `WORKDIR` to `/app/src` and calling the module as `internal_dashboard.backend.main:app`.
4.  **Configuration File:**
    *   Using a `gunicorn.conf.py` file to specify the bind address, workers, etc., to simplify the `CMD` instruction.
5.  **Logging:**
    *   Added extensive `print` and `logging` statements to `main.py`. None of these statements appear in the Cloud Run logs, confirming that the script itself is not being executed by `gunicorn`.

## 6. Core Question for the Expert

Given that the `gunicorn` process is starting and then immediately exiting with a success code (0), and that no Python code from our application module seems to be executing, what is the likely cause of this behavior in the Google Cloud Run environment? Is there a subtle interaction between `gunicorn`, Docker, and the Cloud Run execution environment that we are missing?
