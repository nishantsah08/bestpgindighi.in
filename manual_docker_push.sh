#!/bin/bash
#
# This script performs a manual Docker push to the Artifact Registry.
# It uses your currently authenticated gcloud user account.
# Running this will definitively test your user permissions.

set -e

PROJECT_ID="fir-bestpg"
LOCATION="asia-south1"
REPO_NAME="cloud-run"
HIMAGE_NAME="api-backend-manual-test"

# 1. Configure Docker to use your gcloud credentials
echo "Configuring Docker authentication..."
gcloud auth configure-docker "${LOCATION}-docker.pkg.dev" --project="$PROJECT_ID"

# 2. Build the Docker image
IMAGE_URI="${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:latest"
echo "
Building Docker image: $IMAGE_URI"
docker build -t "$IMAGE_URI" .

# 3. Push the Docker image
echo "
Pushing Docker image to Artifact Registry..."
docker push "$IMAGE_URI"

echo "

SUCCESS: Manual push completed."
