#!/bin/bash
#
# This script grants the necessary IAM permissions to the CI/CD service account
# to allow it to read from and write to the Artifact Registry repository.
#
# You must run this script while authenticated as a Google Cloud Project Owner.

set -e

SA_EMAIL="firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com"
PROJECT_ID="fir-bestpg"
LOCATION="asia-south1"
REPO_NAME="cloud-run"

echo "Granting Artifact Registry Reader role..."
gcloud artifacts repositories add-iam-policy-binding "$REPO_NAME" \
  --location="$LOCATION" \
  --project="$PROJECT_ID" \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/artifactregistry.reader"

echo "Granting Artifact Registry Writer role..."
gcloud artifacts repositories add-iam-policy-binding "$REPO_NAME" \
  --location="$LOCATION" \
  --project="$PROJECT_ID" \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/artifactregistry.writer"

echo "
Permissions granted successfully."

