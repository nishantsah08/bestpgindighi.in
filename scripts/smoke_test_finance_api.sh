#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/smoke_test_finance_api.sh https://<finance-api-url>
# Verifies /v1/health endpoint. Optional write tests can be added later.

if [ $# -lt 1 ]; then
  echo "Usage: $0 <API_BASE_URL>" >&2
  exit 1
fi

API_BASE="$1"

echo "Checking health at ${API_BASE}/v1/health ..."
HTTP=$(curl -sS -w "%{http_code}" -o /tmp/health.json "${API_BASE}/v1/health" || true)
BODY=$(cat /tmp/health.json || true)
echo "HTTP ${HTTP}"
echo "Body: ${BODY}"

if [[ "${HTTP}" != "200" || "${BODY}" != *"ok"* ]]; then
  echo "Health check failed." >&2
  exit 1
fi

echo "Health OK."

