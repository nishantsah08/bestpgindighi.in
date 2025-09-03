#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   PROJECT_ID=grounded-pivot-467812-f4 REGION=asia-south1 SERVICE=finance-api \
#   ./scripts/deploy_finance_api_cloud_run.sh

PROJECT_ID=${PROJECT_ID:-grounded-pivot-467812-f4}
REGION=${REGION:-asia-south1}
SERVICE=${SERVICE:-finance-api}
REPO=${REPO:-apps}
IMAGE="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${SERVICE}:latest"

# Required envs for service
ALLOWED_ORIGINS=${ALLOWED_ORIGINS:-*}
FIRESTORE_PROJECT_ID=${FIRESTORE_PROJECT_ID:-$PROJECT_ID}
PUBLIC_ASSETS_BUCKET=${PUBLIC_ASSETS_BUCKET:-bestpg-public-assets}
THUMB_MAX_BYTES=${THUMB_MAX_BYTES:-2097152}
IMAGE_MAX_DIM=${IMAGE_MAX_DIM:-128}

gcloud config set project "$PROJECT_ID"
gcloud config set run/region "$REGION"

# Ensure Artifact Registry repo exists
gcloud artifacts repositories create "$REPO" --repository-format=docker --location="$REGION" --description="Images" || true

pushd src/internal_dashboard/backend >/dev/null

echo "Building and pushing image: ${IMAGE}"
gcloud builds submit --tag "${IMAGE}"

echo "Deploying to Cloud Run: ${SERVICE} in ${REGION}"
gcloud run deploy "${SERVICE}" \
  --image="${IMAGE}" \
  --platform=managed \
  --region="${REGION}" \
  --allow-unauthenticated \
  --set-env-vars=ALLOWED_ORIGINS=${ALLOWED_ORIGINS},FIRESTORE_PROJECT_ID=${FIRESTORE_PROJECT_ID},PUBLIC_ASSETS_BUCKET=${PUBLIC_ASSETS_BUCKET},THUMB_MAX_BYTES=${THUMB_MAX_BYTES},IMAGE_MAX_DIM=${IMAGE_MAX_DIM}

echo "Service URL:"
gcloud run services describe "${SERVICE}" --region "${REGION}" --format='value(status.url)'

popd >/dev/null
