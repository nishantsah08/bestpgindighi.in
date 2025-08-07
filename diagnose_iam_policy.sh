#!/bin/bash
#
# This script runs a series of diagnostic commands to identify any IAM policies
# that may be overriding your Project Owner permissions.
#
# Please run this script while authenticated as the Project Owner (`nishantsah@outlook.in`)
# in your Google Cloud Shell or a configured local terminal.

set -e

PROJECT_ID="fir-bestpg"
USER_EMAIL="nishantsah@outlook.in"

echo "======================================================="
echo "A) Checking for Conditional Owner Role..."
echo "======================================================="
gcloud projects get-iam-policy "$PROJECT_ID" --format='json' > /tmp/policy.json
jq -r --arg user "user:$USER_EMAIL" \
  '.bindings[] | select(.members[]? | contains($user)) | "Role: \(.role)", "Condition: \(.condition.title // "None")"' \
  /tmp/policy.json

echo "
======================================================="
echo "B) Checking for IAM Deny Policies..."
echo "======================================================="
gcloud iam deny policies list --project="$PROJECT_ID"

echo "
# If any deny policies were listed above, describe them by replacing"
echo "# DENY_POLICY_ID with the actual ID from the output."
echo "# gcloud iam deny policies describe DENY_POLICY_ID --project=$PROJECT_ID --format=json"


echo "
======================================================="
echo "C) Checking for Organization and Organization Policies..."
echo "======================================================="
ORG_ID=$(gcloud projects get-ancestors "$PROJECT_ID" --format='json' | jq -r '.[] | select(.type == "organization") | .id')

if [ -z "$ORG_ID" ]; then
  echo "No parent Organization found for project '$PROJECT_ID'."
else
  echo "Organization ID found: $ORG_ID"
  echo "
--- Checking effective 'Domain Restricted Sharing' policy ---"
  gcloud org-policies describe constraints/iam.allowedPolicyMemberDomains \
    --project="$PROJECT_ID" --effective
fi

echo "
======================================================="
echo "Diagnostic script finished."