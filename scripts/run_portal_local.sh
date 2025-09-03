#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/run_portal_local.sh
# Starts the Internal Portal locally at http://localhost:3000 using CRA.

pushd src/internal_dashboard/frontend >/dev/null

if [ ! -d node_modules ]; then
  echo "Installing frontend dependencies..."
  npm ci || npm install
fi

echo "Starting portal at http://localhost:3000 ... (Ctrl+C to stop)"
npm start

popd >/dev/null

