#!/bin/bash
#
# This script implements the "Ship Today" contingency plan.
# It creates a new, clean project and Artifact Registry repository
# to bypass the complex IAM issues in the original project.
#
# Please run this script in your Google Cloud Shell.

set -e

NEW_PROJECT_ID="fir-bestpg-ci-$(date +%s)" # Add a timestamp to ensure uniqueness
CI_SA_EMAIL="firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com"
NEW_REPO_NAME="cr-images"
LOCATION="asia-south1"

echo "======================================================="
echo "1. Creating new, clean project: $NEW_PROJECT_ID"
echo "======================================================="
gcloud projects create "$NEW_PROJECT_ID"

echo "
======================================================="
echo "2. Setting active project to the new project"
echo "======================================================="
gcloud config set project "$NEW_PROJECT_ID"

echo "
======================================================="
echo "3. Enabling required services..."
echo "======================================================="
gcloud services enable artifactregistry.googleapis.com

echo "
======================================================="
echo "4. Creating new Artifact Registry repository: $NEW_REPO_NAME"
echo "======================================================="
gcloud artifacts repositories create "$NEW_REPO_NAME" \
  --repository-format=docker \
  --location="$LOCATION" \
  --description="Clean image repository for CI/CD"

echo "
======================================================="
echo "5. Granting permissions to the CI/CD service account..."
echo "======================================================="
gcloud artifacts repositories add-iam-policy-binding "$NEW_REPO_NAME" \
  --location="$LOCATION" \
  --project="$NEW_PROJECT_ID" \
  --member="serviceAccount:$CI_SA_EMAIL" \
  --role="roles/artifactregistry.admin"

echo "
======================================================="
echo "Contingency plan executed successfully."
echo "Your new project ID is: $NEW_PROJECT_ID"
echo "Please update the GCP_PROJECT_ID secret in your GitHub repository with this new ID."

