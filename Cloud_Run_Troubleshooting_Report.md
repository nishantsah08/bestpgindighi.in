### Cloud Run Deployment Troubleshooting Report

**1. Summary**

The goal is to deploy a simple "Hello World" Nginx application to Google Cloud Run. The deployment process is consistently failing, despite several troubleshooting attempts. The core issue appears to be related to permissions when pushing the Docker image to the Google Artifact Registry.

**2. Initial Problem**

The initial deployment script (`deploy_public_website.sh`) was hanging during the "Deploying to Cloud Run" step. The Cloud Run service logs indicated that the container was not healthy because of a port mismatch. The `Dockerfile` was exposing port 80 (the Nginx default), while Cloud Run was attempting to connect to the default port of 8080.

**3. Troubleshooting Steps and Outcomes**

Here is a chronological summary of the steps taken to resolve the issue:

*   **Port Correction (Attempt 1):**
    *   **Action:** Modified the `deploy_public_website.sh` script to include the `--port=80` flag in the `gcloud run deploy` command.
    *   **Result:** The user requested to use port 8000 instead.

*   **Port Correction (Attempt 2):**
    *   **Action:**
        1.  Created a new `nginx.conf` file to configure Nginx to listen on port 8000.
        2.  Updated the `Dockerfile` to copy the new `nginx.conf` and expose port 8000.
        3.  Updated the `deploy_public_website.sh` script to use `--port=8000`.
    *   **Result:** The deployment failed with a Docker daemon permission error: `permission denied while trying to connect to the Docker daemon socket`.

*   **Docker Permissions (Attempt 1):**
    *   **Action:** Added `sudo` to the `docker build` and `docker push` commands in the deployment script.
    *   **Result:** The deployment failed with an authentication error: `denied: Unauthenticated request`. This is because `sudo` was running the commands as the `root` user, which was not authenticated with `gcloud`.

*   **Docker Permissions (Attempt 2):**
    *   **Action:**
        1.  Added the current user to the `docker` group to allow running Docker commands without `sudo`.
        2.  The user confirmed they had started a new shell session.
        3.  Removed `sudo` from the `docker` commands.
    *   **Result:** The deployment failed with the same Docker daemon permission error as before.

*   **Docker Permissions (Attempt 3):**
    *   **Action:**
        1.  Re-added `sudo` to the `docker` commands.
        2.  Added `sudo gcloud auth configure-docker` to the deployment script to authenticate the `root` user.
    *   **Result:** The deployment failed with a new permission error: `Permission "artifactregistry.repositories.uploadArtifacts" denied`.

*   **IAM Permissions:**
    *   **Action:** Granted the `roles/artifactregistry.writer` role to the user's active `gcloud` account (`nishantsah@outlook.in`).
    *   **Result:** The deployment failed with the same `Permission "artifactregistry.repositories.uploadArtifacts" denied` error.

*   **Switching `gcloud` Account:**
    *   **Action:** Attempted to switch the active `gcloud` account to the service account `development@grounded-pivot-467812-f4.iam.gserviceaccount.com`.
    *   **Result:** The user cancelled this operation.

**4. Current Status**

The deployment is blocked by the following error:

`Permission "artifactregistry.repositories.uploadArtifacts" denied on resource "projects/grounded-pivot-467812-f4/locations/asia-south1/repositories/public-website-repo"`

This error persists even after granting the `artifactregistry.writer` role to the user's account. This suggests a more complex authentication or permissions issue, possibly related to the active `gcloud` account or the way Docker is interacting with `gcloud` authentication.

**5. Relevant Files**

Here are the contents of the relevant files:

**`deploy_public_website.sh`**
```bash
#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
# Google Cloud Project ID
PROJECT_ID="grounded-pivot-467812-f4"
# Google Cloud Region for Mumbai
REGION="asia-south1"
# Name for the Artifact Registry repository
REPOSITORY="public-website-repo"
# Name for the Docker image and Cloud Run service
IMAGE_NAME="hello-world-app"
# Directory containing the source code and Dockerfile
SOURCE_DIR="src/public_website"

# --- Script ---

echo "--- Setting Google Cloud Project ---"
gcloud config set project $PROJECT_ID
gcloud config set compute/region $REGION

echo "--- Enabling Required Google Cloud Services ---"
gcloud services enable artifactregistry.googleapis.com run.googleapis.com

echo "--- Creating Artifact Registry Repository (if it doesn't exist) ---"
# The command will fail if the repository already exists. The '|| true' part ensures the script continues.
gcloud artifacts repositories create $REPOSITORY \
    --repository-format=docker \
    --location=$REGION \
    --description="Repository for public website images" || echo "Repository '$REPOSITORY' may already exist. Continuing..."

echo "--- Configuring Docker Authentication ---"
gcloud auth configure-docker $REGION-docker.pkg.dev

echo "--- Building the Docker Image ---"
sudo docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_NAME:latest $SOURCE_DIR

echo "--- Pushing the Docker Image to Artifact Registry ---"
sudo docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_NAME:latest

echo "--- Deploying the Image to Cloud Run ---"
gcloud run deploy $IMAGE_NAME \
    --image=$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_NAME:latest \
    --platform=managed \
    --region=$REGION \
    --port=8000 \
    --allow-unauthenticated

echo "--- Deployment Complete ---"
echo "The public URL for your service will be displayed above."
```

**`src/public_website/Dockerfile`**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8000
```

**`src/public_website/nginx.conf`**
```nginx
events {}
http {
    server {
        listen 8000;
        server_name localhost;

        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
    }
}
```

**`src/public_website/index.html`**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Hello World</title>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```