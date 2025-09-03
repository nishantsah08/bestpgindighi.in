#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   PROJECT_ID=grounded-pivot-467812-f4 REGION=asia-south1 BUCKET=bestpg-public-assets \
#   ./scripts/create_public_assets_bucket.sh

PROJECT_ID=${PROJECT_ID:-grounded-pivot-467812-f4}
REGION=${REGION:-asia-south1}
BUCKET=${BUCKET:-bestpg-public-assets}

gcloud config set project "$PROJECT_ID"

echo "Creating bucket gs://${BUCKET} in ${REGION} (if not exists)"
gcloud storage buckets create "gs://${BUCKET}" --location="${REGION}" --uniform-bucket-level-access || true

echo "Setting public read access for objects"
gsutil iam ch allUsers:objectViewer gs://${BUCKET}

echo "Bucket ready: gs://${BUCKET}"

