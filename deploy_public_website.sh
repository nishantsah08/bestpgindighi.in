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
gcloud run deploy $IMAGE_NAME     --image=$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE_NAME:latest     --platform=managed     --region=$REGION     --port=8000     --allow-unauthenticated

echo "--- Deployment Complete ---"
echo "The public URL for your service will be displayed above."
