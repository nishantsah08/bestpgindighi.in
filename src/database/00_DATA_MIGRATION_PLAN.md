# Data Migration & Seeding Plan

**Version:** 1.0
**Date:** 2025-07-22

## 1. Objective

To perform a one-time migration of existing business data into the new Firestore database to establish the initial "Day 0" state of the system.

## 2. Data Sources

- Existing tenant records (e.g., from spreadsheets, existing software).
- Existing vendor contact information.
- Historical financial records (if available).
- Property details as defined in `parliament_policies/bills/15_property_and_asset_management_bill.yaml`.

## 3. Migration Steps

1.  **Export Existing Data:** All current business data will be exported into a structured format (e.g., CSV, JSON).
2.  **Develop Seeding Script:** A script will be written (e.g., in Node.js or Python) to read the exported data.
3.  **Data Mapping:** The script will map the columns from the old data format to the fields in the new Firestore database schema.
4.  **Execute Script:** The script will be run once to populate the `properties`, `tenants`, `vendors`, and `financial_ledger` collections in the production Firestore database.
5.  **Verification:** The CEO will manually verify the migrated data in the Internal System Portal to ensure accuracy and completeness.