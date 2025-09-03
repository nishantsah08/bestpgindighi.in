#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/configure_frontend_env.sh https://<finance-api-url> [api_token]
# Writes .env.development.local for the Internal Portal to call the Finance API.

if [ $# -lt 1 ]; then
  echo "Usage: $0 <API_BASE_URL> [API_TOKEN]" >&2
  exit 1
fi

API_BASE="$1"
API_TOKEN="${2:-}"

ENV_FILE="src/internal_dashboard/frontend/.env.development.local"
mkdir -p "$(dirname "$ENV_FILE")"
{
  echo "REACT_APP_API_BASE=${API_BASE}"
  if [ -n "$API_TOKEN" ]; then
    echo "REACT_APP_API_TOKEN=${API_TOKEN}"
  else
    echo "# REACT_APP_API_TOKEN="
  fi
} > "$ENV_FILE"

echo "Updated $ENV_FILE"

