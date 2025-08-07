#!/bin/bash
#
# This script creates a new, clean Artifact Registry repository and grants the
# necessary permissions to the CI/CD service account. It then updates the
# CI/CD workflow to use this new repository.
#
# Please run this script in your Google Cloud Shell.

set -e

PROJECT_ID="fir-bestpg"
CI_SA_EMAIL="firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com"
NEW_REPO_NAME="cr-images"
LOCATION="asia-south1"

echo "======================================================="
echo "1. Creating new, clean Artifact Registry repository: $NEW_REPO_NAME"
echo "======================================================="
gcloud artifacts repositories create "$NEW_REPO_NAME" \
  --repository-format=docker \
  --location="$LOCATION" \
  --project="$PROJECT_ID" \
  --description="Clean image repository for CI/CD"

echo "
======================================================="
echo "2. Granting permissions to the CI/CD service account..."
echo "======================================================="
gcloud artifacts repositories add-iam-policy-binding "$NEW_REPO_NAME" \
  --location="$LOCATION" \
  --project="$PROJECT_ID" \
  --member="serviceAccount:$CI_SA_EMAIL" \
  --role="roles/artifactregistry.admin"

echo "
======================================================="
echo "3. Updating CI/CD workflow to use new repository..."
echo "======================================================="

# This uses a temporary file to avoid issues with sed in-place editing
WORKFLOW_FILE=".github/workflows/deploy_to_cloud_run.yml"
TMP_FILE=$(mktemp)

sed 's/REPO: cloud-run/REPO: cr-images/' "$WORKFLOW_FILE" > "$TMP_FILE" && mv "$TMP_FILE" "$WORKFLOW_FILE"

echo "Workflow updated successfully."

echo "
======================================================="
echo "Fix applied. Please commit and push the updated workflow file."

