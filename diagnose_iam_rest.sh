#!/bin/bash
#
# This script uses the Google Cloud REST APIs directly to diagnose IAM and
# Artifact Registry issues, bypassing any potential gcloud CLI issues.
#
# Please run this script in your Google Cloud Shell.

set -e

echo "======================================================="
echo "A) Preparing credentials and variables..."
echo "======================================================="

PROJECT_ID="fir-bestpg"
ACCESS_TOKEN="$(gcloud auth print-access-token)"
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"

echo "Project ID: $PROJECT_ID"
echo "Project Number: $PROJECT_NUMBER"

echo "
======================================================="
echo "B) Checking for IAM Deny Policies..."
echo "======================================================="

echo "--- Project-scoped Deny Policies ---"
curl -sS -H "Authorization: Bearer $ACCESS_TOKEN" \
"https://iam.googleapis.com/v2/policies?parent=projects/${PROJECT_NUMBER}&policyType=DenyPolicy" | jq

ORG_ID="$(gcloud organizations list --format='value(ID)' | head -n1)"
if [ -n "$ORG_ID" ]; then
  echo "
--- Organization-scoped Deny Policies (Org ID: $ORG_ID) ---"
  curl -sS -H "Authorization: Bearer $ACCESS_TOKEN" \
  "https://iam.googleapis.com/v2/policies?parent=organizations/${ORG_ID}&policyType=DenyPolicy" | jq
fi

echo "
======================================================="
echo "C) Finding Artifact Registry Repository Location..."
echo "======================================================="
curl -sS -H "Authorization: Bearer $ACCESS_TOKEN" \
"https://artifactregistry.googleapis.com/v1/projects/${PROJECT_ID}/locations/-/repositories" | jq

echo "
======================================================="
echo "Diagnostic script finished."
