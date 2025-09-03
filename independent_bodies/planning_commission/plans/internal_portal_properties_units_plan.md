# Internal Portal – Properties & Units Module (Planning Commission Plan)

## Summary
- Build the CEO Internal Portal module for managing Properties and Units.
- Property: create/edit, status toggle (Operational/Non‑Operational), delete (blocked if units exist), thumbnail avatar.
- Unit: create, status toggle (Operational/Non‑Operational), delete (no rename/edit).
- Blocking modals for all add/edit/delete, typed confirmations for deletes.
- Address entry is pincode‑first with autofill for state/city/locality using `https://api.postalpincode.in/pincode/{PIN}`.
- Thumbnails: 128x128 WebP, stored in GCS (public‑read) under a scoped path.
- Rich error messages: what happened, to whom, why, next step; developer payload includes correlation_id.
- No schema changes to existing Firestore collections beyond adding `photo_thumb_url` in property docs and creating `audit_logs` collection.

## Scope & Goals
- In scope: Properties list and detail (with Units sub‑view), CRUD per above, status lockouts, image pipeline, audit logging, address autofill.
- Out of scope: Beds/Tenants/Agreements/Finance; bulk import; CSV export; mobile apps.

## Strategic Alignment
- Aligns with docs/00_SYSTEM_OVERVIEW.md: builds the Property & Tenant Welfare operational UI.
- Supports scalability and operational integrity: clear lockouts, auditability, and small public assets.
- Follows the hybrid model: operational parameters in UI; foundational logic enforced server‑side.

## Inter‑Ministerial Coordination
- Executive: Ministry of Property & Tenant Welfare (primary UI), Technology & Digital Infrastructure (backend/API, storage), Finance (no coupling in this phase).
- Independent Bodies: Auditor AI consumes `audit_logs` later; Vigilance AI can monitor auth/access logs.

## Logical Atom Decomposition & Integration
- UI Atoms
  - Properties List view (table + search/filter + add modal)
  - Property Detail view (header with avatar/address/status + Units table + add unit modal)
  - Modals: Add/Edit Property, Add Unit, Toggle confirmations, Delete confirmations (typed)
- API Atoms (Cloud Run – Python/FastAPI)
  - Properties: list, create, edit, toggle status, delete, upload photo
  - Units: list, create, toggle status, delete
  - Shared: audit logging util; GCS upload util; validation layer
- Data Atoms (Firestore)
  - `properties` docs: { property_name, status, address{ line1, locality, city, state, pincode }, photo_thumb_url, created_at, updated_at }
  - `properties/{property_id}/units` docs: { unit_number, status, created_at, updated_at }
  - `audit_logs` docs: { action, target_type, target_id, parent_property_id?, actor_id, before, after, timestamp, ip?, user_agent?, correlation_id }
- External Atoms
  - Pincode autofill: `https://api.postalpincode.in/pincode/{PIN}` (client‑side)
  - GCS bucket for thumbnails (public‑read), region `asia-south1` (Mumbai)

## Architecture Fit & Decisions
- Frontend: Internal Portal desktop web (React SPA per blueprint) served via Firebase Hosting (no change required to host), or static via Cloud Run if desired later. This plan focuses on API + UI module; deploy scripts requested.
- Backend: Cloud Run service (FastAPI) in `asia-south1` handling CRUD, validation, auditing, and GCS uploads.
- Storage: Firestore Native; GCS public assets bucket for thumbnails; public‑read with long‑term immutable cache headers.
- Auth: Google Sign‑In for CEO; staging allowlist (email) as provided.

## Data Model & Validation
- Property
  - property_name: 3–80 chars; letters/numbers/spaces/&/-; trim/collapse; globally unique.
  - status: Operational | Non‑Operational.
  - address: { pincode (6 digits, IN), state (2–60), city (2–60), locality (2–80, optional), line1 (5–120) }.
  - photo_thumb_url: string (public URL); timestamps.
- Unit
  - unit_number: 1–12 chars; alphanumeric + hyphen; no spaces; unique per property (case‑insensitive).
  - status: Operational | Non‑Operational; timestamps.

## API Contract (High‑Level)
- Properties
  - GET /properties?search=&status=
  - POST /properties { name, address, status?, photo? }
  - PATCH /properties/{id} { name?, address?, photo? }  → 423 if Non‑Operational
  - POST /properties/{id}/status { status }
  - DELETE /properties/{id} → 409 if units exist
  - POST /properties/{id}/photo multipart(file) → { photo_thumb_url }
- Units
  - GET /properties/{id}/units
  - POST /properties/{id}/units { unit_number, status? } → 423 if property Non‑Operational
  - POST /properties/{id}/units/{unit_id}/status { status } → 423 if property Non‑Operational
  - DELETE /properties/{id}/units/{unit_id} → 423 if property Non‑Operational
- Error envelope: { code, message, target?, details?, suggested_action?, correlation_id }

## UI Behaviors & Copy (Key)
- Non‑Operational banner: “This property is Non‑Operational. Editing units is disabled. Toggle status to make changes.”
- Toggle to Non‑Operational: “No changes will be allowed or queued while ‘{property_name}’ is in Non‑Operational mode.”
- Delete Property: typed “delete {property_name}”; block with units: “Cannot delete. This property has {n} units. Delete all units first.”
- Add Unit help: “Unit number up to 12 characters, no spaces (e.g., 101, 101A, G1).”

## Storage & Caching
- GCS path: `gs://bestpg-public-assets/public/properties/{property_id}/thumb.webp`
- Headers: `Cache-Control: public, max-age=31536000, immutable`
- Public‑read bucket with uniform access; originals not stored publicly.

## Security & Access Control
- CEO‑only access for module (staging allowlist); Google Sign‑In.
- Public thumbnails only; all writes via authenticated API using service account to Firestore/GCS.
- Audit logging for all mutations.

## Blast Radius Analysis
- New files (proposed placement)
  - Backend (Cloud Run API): `src/api/properties/*.py` (routers, models, services), `src/api/units/*.py`, `src/common/audit.py`, `src/common/gcs.py`, `src/common/validation.py`
  - Frontend (Portal): `src/portal/properties/PropertiesList.tsx`, `src/portal/properties/PropertyDetail.tsx`, `src/portal/properties/modals/*.tsx`, `src/portal/common/components/StatusPill.tsx`, `src/portal/common/components/ConfirmDeleteModal.tsx`
  - Config: `.env`/secrets mapping for bucket name and limits; portal env for API base URL
  - Docs: this Planning Commission plan
- Modified files
  - Portal sidebar/navigation to add Properties entry (if not present)
  - Hosting/route config if needed for new paths (only if not already SPA‑routed)
- Data impacts
  - Adds `photo_thumb_url` to property docs (non‑breaking)
  - Adds `audit_logs` collection
- External dependencies
  - GCS client, WebP conversion library (e.g., Pillow + WebP in Python) in API container

## Resource Optimization
- WebP thumbnails (small footprint), immutable caching via CDN.
- Client‑side pincode lookup to avoid backend latency/cost; graceful fallback.
- Serverless scale‑to‑zero (Cloud Run) and Firestore native.

## Implementation Plan (Phases)
1) Backend API scaffolding (models, validation, audit logging, status lockouts, endpoints)
2) Image pipeline (size enforcement, 128x128 crop, WebP conversion, GCS upload, cache headers)
3) Frontend UI (list/detail, modals, typed confirmations, banners, pincode autofill integration)
4) Error handling (rich messages), correlation IDs end‑to‑end
5) Tests: unit → integration → Playwright E2E
6) Staging deploy (Cloud Run + GCS) and UAT

## Test Plan (Concise)
- Unit: validation, lockouts, uniqueness, image pipeline.
- Integration: CRUD paths; conflicts (409); lockouts (423); audit_logs correctness.
- E2E: pincode‑first flow; typed confirmations; toggle banners; image upload size/format.
- Security: CEO‑only routes; public thumbnails accessible.

## Deployment Plan (Staging)
- Project: `grounded-pivot-467812-f4`
- Region: `asia-south1` (Mumbai)
- Firestore: Native, location `asia-south1`
- GCS bucket: `bestpg-public-assets` (public‑read, uniform), region `asia-south1`
- Service account: `development@grounded-pivot-467812-f4.iam.gserviceaccount.com` with roles: Firestore User, Storage Object Admin (bucket‑scoped), Cloud Run Invoker, Logs Writer
- Config: `PUBLIC_ASSETS_BUCKET=bestpg-public-assets`, `THUMB_MAX_BYTES=2097152`, `IMAGE_MAX_DIM=128`, `LOG_CORRELATION=true`
- Auth: allowlist `nishantsah@outlook.in` (or enable Email/Password for staging if needed)
- Delivery: deploy via scripts (no CI/CD at this stage)

## Risks & Mitigations
- Pincode API availability: cache client‑side; manual override always allowed.
- Public assets hotlinking: acceptable for thumbnails; scoped path; option to migrate to signed URLs later.
- Concurrency on toggles/deletes: last‑write wins; UI reload with fresh state.

## Rollback
- Cloud Run revision rollback; no schema migrations; no data loss.

## Final Verification Statement
The Planning Commission has analyzed the proposed changes and confirms that they are consistent with the system's architecture and strategic objectives. No conflicts have been identified.

