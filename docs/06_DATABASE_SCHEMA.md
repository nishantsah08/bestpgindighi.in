# 06 - Database Schema (Firebase Firestore)

This document defines the data model for the system, implemented in Firebase Firestore.

## 1. Top-Level Collections

- `tenants`
- `vendors`
- `judicial_docket`
- `general_ledger`

## 2. `tenants` Collection

- **Document ID:** `tenant_id` (auto-generated)
- **Fields:**
    - `name` (string)
    - `contact_number` (string)
    - `status` (string: `PROVISIONAL`, `VERIFIED`, `ACTIVE`, `ARCHIVED`)
    - `verification_attempts` (number)
    - `identity_documents` (map, nullable)
    - `created_at` (timestamp)

## 3. `judicial_docket` Collection

- **Document ID:** `case_id` (auto-generated)
- **Fields:**
    - `case_type` (string)
    - `status` (string: `PENDING_REVIEW`, `PENDING_CEO_APPROVAL`, `RESOLVED`)
    - `filer_id` (string)
    - `monetary_impact_amount` (number, nullable)
    - `recommended_verdict` (string, nullable)
    - `final_verdict` (string, nullable)
    - `created_at` (timestamp)

## 4. Firestore Security Rules

- Access to collections will be governed by Firestore Security Rules.
- Rules will be written to enforce the Access Control Lists (ACLs) defined in the `05_MCP_CAPABILITY_REGISTRY.md`.
- Example: Only a service with the `Financial_AI_Agent` role can write to the `general_ledger` collection.
