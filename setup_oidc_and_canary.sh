#!/bin/bash
#
# This script configures Workload Identity Federation to allow GitHub Actions
# to securely authenticate to Google Cloud without using long-lived service
# account keys.
#
# Please run this script from your Google Cloud Shell.

set -e

PROJECT_ID="fir-bestpg"
CI_SA_EMAIL="firebase-adminsdk-fbsvc@fir-bestpg.iam.gserviceaccount.com"
GITHUB_REPO="nishantsah08/bestpgindighi.in"

POOL_ID="github-actions-pool"
PROVIDER_ID="github-actions-provider"

echo "======================================================="
echo "1. Creating Workload Identity Pool..."
echo "======================================================="
gcloud iam workload-identity-pools create "$POOL_ID" \
  --project="$PROJECT_ID" \
  --location="global" \
  --display-name="GitHub Actions Pool" || echo "Pool '$POOL_ID' already exists. Skipping."

# Add a delay to allow the new pool to propagate
echo "
Waiting for 10 seconds for the new pool to propagate..."
sleep 10

POOL_NAME=$(gcloud iam workload-identity-pools describe "$POOL_ID" \
  --project="$PROJECT_ID" \
  --location="global" \
  --format="value(name)")

echo "
======================================================="
echo "2. Creating Workload Identity Provider..."
echo "======================================================="
gcloud iam workload-identity-pools providers create-oidc "$PROVIDER_ID" \
  --project="$PROJECT_ID" \
  --location="global" \
  --workload-identity-pool="$POOL_ID" \
  --display-name="GitHub Actions Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com" || echo "Provider '$PROVIDER_ID' already exists. Skipping."

echo "
======================================================="
echo "3. Allowing the CI/CD service account to be impersonated by GitHub Actions..."
echo "======================================================="
gcloud iam service-accounts add-iam-policy-binding "$CI_SA_EMAIL" \
  --project="$PROJECT_ID" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/$POOL_NAME/attribute.repository/$GITHUB_REPO"

echo "
======================================================="
echo "OIDC setup completed successfully."