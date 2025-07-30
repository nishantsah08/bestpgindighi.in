# 06 - Database Schema (Firebase Firestore)

This document defines the data model for the system, implemented in Firebase Firestore.

## 1. Top-Level Collections

- `properties`
- `tenants`
- `rent_agreements`
- `vendors`
- `judicial_docket`
- `general_ledger`
- `tenant_feedback`
- `inventory`
- `sales_tasks`
- `call_logs`
- `contacts`

## 2. `properties` Collection (NEW)

- **Document ID:** `property_id` (auto-generated)
- **Description:** Stores high-level information about each managed property.
- **Sub-collections:** `units`
- **Fields:**
    - `property_name` (string)
    - `address` (map)
    - `status` (string: `Operational`, `Expansion Ready`)
    - `created_at` (timestamp)

## 3. `units` Collection (NEW)

- **Document ID:** `unit_id` (auto-generated)
- **Description:** Stores information about individual flats or units within a property.
- **Sub-collections:** `beds`
- **Fields:**
    - `unit_number` (string)
    - `unit_type` (string: `2BHK`, `Studio`)
    - `status` (string: `Occupied`, `Vacant`)
    - `property_id` (reference to `properties` collection)

## 4. `beds` Collection (NEW)

- **Document ID:** `bed_id` (auto-generated)
- **Description:** Stores details about each individual bed within a unit.
- **Fields:**
    - `bed_identifier` (string)
    - `status` (string: `Occupied`, `Vacant`, `Reserved`)
    - `unit_id` (reference to `units` collection)
    - `tenant_id` (reference to `tenants` collection, nullable)

## 5. `tenants` Collection

- **Document ID:** `tenant_id` (auto-generated)
- **Fields:**
    - `name` (string)
    - `contact_number` (string)
    - `status` (string: `PROVISIONAL`, `VERIFIED`, `ACTIVE`, `ARCHIVED`)
    - `verification_attempts` (number)
    - `identity_documents` (map, nullable)
    - `created_at` (timestamp)

## 6. `rent_agreements` Collection (NEW)

- **Document ID:** `agreement_id` (auto-generated)
- **Description:** Stores all data related to tenant rent agreements.
- **Fields:**
    - `tenant_id` (reference to `tenants` collection)
    - `start_date` (timestamp)
    - `end_date` (timestamp)
    - `status` (string: `ACTIVE`, `EXPIRED`, `RENEWED`, `CANCELLED`)
    - `document_url` (string, URL to the signed e-agreement)
    - `created_at` (timestamp)

## 7. `tenant_feedback` Collection

- **Document ID:** `feedback_id` (auto-generated)
- **Fields:**
    - `tenant_id` (string, reference to `tenants` collection)
    - `timestamp` (timestamp)
    - `bathroom_cleanliness_score` (number, 1-5)
    - `kitchen_cleanliness_score` (number, 1-5)
    - `parking_area_cleanliness_score` (number, 1-5)
    - `garbage_collection_timeliness_score` (number, 1-5)
    - `room_cleaning_service_score` (number, 1-5, nullable)
    - `maintenance_quality_score` (number, 1-5, nullable)
    - `comments` (string, nullable)
    - `calculated_overall_satisfaction_score` (float)

## 8. `judicial_docket` Collection

- **Document ID:** `case_id` (auto-generated)
- **Fields:**
    - `case_type` (string)
    - `status` (string: `PENDING_REVIEW`, `PENDING_CEO_APPROVAL`, `RESOLVED`)
    - `filer_id` (string)
    - `monetary_impact_amount` (number, nullable)
    - `recommended_verdict` (string, nullable)
    - `final_verdict` (string, nullable)
    - `created_at` (timestamp)

## 9. `inventory` Collection

- **Document ID:** `asset_id` (auto-generated)
- **Fields:**
    - `asset_name` (string)
    - `quantity` (number)
    - `status` (string: `IN_STORAGE`, `IN_USE`, `DISPOSED`)
    - `purchase_transaction_id` (string, reference to `general_ledger` collection)
    - `added_at` (timestamp)

## 10. Firestore Security Rules

- Access to collections will be governed by Firestore Security Rules.
- Rules will be written to enforce the Access Control Lists (ACLs) defined in the `05_MCP_CAPABILITY_REGISTRY.md`.
- Example: Only a service with the `Financial_AI_Agent` role can write to the `general_ledger` collection.

## 11. `call_logs` Collection (NEW)

- **Document ID:** `call_id` (auto-generated)
- **Description:** Stores metadata for all recorded calls made from the mobile application suite.
- **Fields:**
    - `caller_role` (string: `CEO`, `Sales`, `Caretaker`)
    - `customer_number` (string)
    - `call_timestamp` (timestamp)
    - `duration_seconds` (number)
    - `recording_url` (string, URL to the audio file in storage)
    - `status` (string: `UPLOADED`, `TRANSCRIBING`, `COMPLETED`, `FAILED`)
    - `created_at` (timestamp)

## 12. `contacts` Collection (NEW)

- **Document ID:** `contact_id` (auto-generated)
- **Description:** Stores information about all business contacts, including leads, tenants, and vendors.
- **Fields:**
    - `name` (string, nullable)
    - `phone_number` (string, unique, canonical format: E.164)
    - `svh_id` (string, unique, format: `SVH-XX`)
    - `status` (string: `New Lead`, `Active Tenant`, `Past Tenant`, `Vendor`)
    - `created_at` (timestamp)

## 14. `api_usage_logs` Collection (NEW)

- **Document ID:** `provider_year_month` (e.g., `google_2025_07`)
- **Description:** Tracks monthly usage of third-party APIs with free tiers.
- **Fields:**
    - `provider_name` (string: `google`, `azure`)
    - `year_month` (string, format: `YYYY_MM`)
    - `minutes_used` (number)

## 13. `system_counters` Collection (NEW)

- **Document ID:** `counter_name` (e.g., `contact_svh_id`)
- **Description:** Manages unique, incremental counters for the system.
- **Fields:**
    - `current_value` (number)

