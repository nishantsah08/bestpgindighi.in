# Properties & Units Management – Consolidated Plan

## Scope
- Property management: add, switch Operational/Non‑Operational, delete (type “delete”).
- Units under a property: add, switch Operational/Non‑Operational, delete (type “delete”).
- No bed management in this phase.
- Add a “Properties” section in the Internal Portal.

## Deliverables
- Properties module in the Internal Portal with a Units sub‑view.
- Safe delete (typed confirmation) and clear status rules in the UI.
- Reuse existing backend endpoints (no schema changes).
- Short runbook and a test report template.

## Implementation Steps
1. Build Properties list: create, status toggle, delete with typed confirmation.
2. Build Property detail panel: list units, create, status toggle, delete with typed confirmation.
3. Enforce UI lockouts when Non‑Operational (no edits allowed).
4. Configure API base URL and token via environment; add simple error toasts.

## Testing (from this machine against Google Cloud)
- Use a real browser to navigate like a user: add/toggle/delete properties; open a property; add/toggle/delete units.
- Verify: Non‑Operational blocks edits; deletes fully remove; lists refresh promptly.
- Evidence: screenshots/video and a brief pass/fail note after each change and before merge.
- Frequency: after each feature and on final review.

## Deployment
- Project: `grounded-pivot-467812-f4` (Google Cloud).
- Service account: `development@grounded-pivot-467812-f4.iam.gserviceaccount.com`.
- The Internal Portal uses an API token when calling the backend.
- Rollback by reverting the branch deployment if a critical test fails.

## Access & Prerequisites
- Confirm the live Internal Portal URL, API token, backend Cloud Run URL, and CORS settings.
- Ensure the service account has roles for Cloud Run and Firestore.

## Timeline
- Day 1: Properties list (create/toggle/delete) + tests.
- Day 2: Property detail Units (create/toggle/delete) + tests.
- Day 3: Polish, docs, consolidated test run and sign‑off.

## Risks & Mitigation
- CORS/auth mismatch: validate early with a smoke test.
- Data side effects: run against test data and cleanup after runs.
- UI regressions: keep typed confirmation for all destructive actions.

## Final Verification Statement
The Planning Commission has analyzed the proposed changes and confirms that they are consistent with the system's architecture and strategic objectives. No conflicts have been identified.

