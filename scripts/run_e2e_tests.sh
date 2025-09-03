#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   E2E_BASE_URL=http://localhost:3000 ./scripts/run_e2e_tests.sh
# or
#   ./scripts/run_e2e_tests.sh http://localhost:3000

BASE_URL="${1:-${E2E_BASE_URL:-http://localhost:3000}}"

pushd src/internal_dashboard/frontend >/dev/null

if [ ! -d node_modules ]; then
  echo "Installing frontend dev dependencies..."
  npm ci || npm install
fi

echo "Installing Playwright browsers..."
npx playwright install --with-deps || npx playwright install

echo "Running E2E tests against ${BASE_URL}..."
E2E_BASE_URL="$BASE_URL" npm run -s test:e2e || {
  echo "E2E tests failed. See playwright-report for details." >&2
  exit 1
}

echo "E2E tests passed. To view the report: npx playwright show-report"

popd >/dev/null

