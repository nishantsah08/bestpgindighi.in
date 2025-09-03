#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   PROJECT_ID=grounded-pivot-467812-f4 REGION=asia-south1 SERVICE=finance-api \
#   ./scripts/deploy_finance_api_cloud_run.sh

PROJECT_ID=${PROJECT_ID:-grounded-pivot-467812-f4}
REGION=${REGION:-asia-south1}
SERVICE=${SERVICE:-finance-api}
IMAGE="asia-south1-docker.pkg.dev/${PROJECT_ID}/apps/${SERVICE}:latest"

pushd src/internal_dashboard/backend >/dev/null

echo "Building and pushing image: ${IMAGE}"
gcloud builds submit --tag "${IMAGE}"

echo "Deploying to Cloud Run: ${SERVICE} in ${REGION}"
gcloud run deploy "${SERVICE}" \
  --image="${IMAGE}" \
  --platform=managed \
  --region="${REGION}" \
  --allow-unauthenticated \
  --set-env-vars=ALLOWED_ORIGINS=https://internal.bestpgindighi.in

echo "Service URL:"
gcloud run services describe "${SERVICE}" --region "${REGION}" --format='value(status.url)'

popd >/dev/null

