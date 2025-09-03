#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   PROJECT_ID=grounded-pivot-467812-f4 REGION=asia-south1 SERVICE=internal-portal-frontend REPO=apps \
#   ./scripts/deploy_frontend_cloud_run.sh

PROJECT_ID=${PROJECT_ID:-grounded-pivot-467812-f4}
REGION=${REGION:-asia-south1}
SERVICE=${SERVICE:-internal-portal-frontend}
REPO=${REPO:-apps}
IMAGE="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${SERVICE}:latest"

gcloud config set project "$PROJECT_ID"
gcloud config set run/region "$REGION"
gcloud artifacts repositories create "$REPO" --repository-format=docker --location="$REGION" --description="Images" || true

pushd src/internal_dashboard/frontend >/dev/null

echo "Building and pushing image: ${IMAGE}"
gcloud builds submit --tag "$IMAGE"

echo "Deploying Cloud Run service: ${SERVICE}"
gcloud run deploy "$SERVICE" \
  --image="$IMAGE" \
  --platform=managed \
  --region="$REGION" \
  --allow-unauthenticated

echo "Service URL:"
gcloud run services describe "$SERVICE" --region "$REGION" --format='value(status.url)'

popd >/dev/null

