#!/bin/bash
#
# This script performs the one-time setup required in your Google Cloud project
# to enable the CI/CD pipeline.
#
# Please run this script from your Google Cloud Shell or a local terminal
# where you are authenticated as a Project Owner.

set -e

PROJECT_ID="fir-bestpg"
CI_SA_EMAIL="firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com"
COMPUTE_SA_EMAIL="1020918069137-compute@developer.gserviceaccount.com"

echo "======================================================="
echo "1. Setting project to $PROJECT_ID"
echo "======================================================="
gcloud config set project "$PROJECT_ID"

echo "
======================================================="
echo "2. Enabling required APIs..."
echo "======================================================="
gcloud services enable run.googleapis.com artifactregistry.googleapis.com

echo "
======================================================="
echo "3. Creating Artifact Registry repository (if it doesn't exist)..."
echo "======================================================="
gcloud artifacts repositories create cloud-run \
  --repository-format=docker \
  --location=asia-south1 \
  --description="Images for Cloud Run" || echo "Repository 'cloud-run' already exists. Skipping."

echo "
======================================================="
echo "4. Granting IAM permissions to the CI/CD Service Account..."
echo "======================================================="

# Grant Cloud Run Admin role
echo "--> Granting roles/run.admin..."
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:$CI_SA_EMAIL" \
  --role="roles/run.admin"

# Grant Artifact Registry Writer role
echo "--> Granting roles/artifactregistry.writer..."
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:$CI_SA_EMAIL" \
  --role="roles/artifactregistry.writer"

# Grant Service Account User role
echo "--> Granting roles/iam.serviceAccountUser..."
gcloud iam service-accounts add-iam-policy-binding "$COMPUTE_SA_EMAIL" \
  --member="serviceAccount:$CI_SA_EMAIL" \
  --role="roles/iam.serviceAccountUser"

echo "
======================================================="
echo "GCP setup completed successfully."

