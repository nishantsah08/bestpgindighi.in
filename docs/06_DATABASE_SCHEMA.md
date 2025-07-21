# Database Schema

**Version:** 1.0
**Date:** 2025-07-22

## 1. Overview

This document defines the schema for the primary data collections stored in Firestore.

## 2. Collections

### `properties`
- **Description:** Stores the physical structure of all managed properties.
- **Fields:**
    - `property_id` (String)
    - `property_name` (String)
    - `flats` (Array of Objects)
        - `flat_number` (String)
        - `status` (String: "Operational", "Expansion Ready")
        - `sub_meter_id` (String)
        - `beds` (Array of Strings)

### `tenants`
- **Description:** Stores information about all customers.
- **Fields:**
    - `tenant_svh_id` (String)
    - `full_name` (String)
    - `phone_number` (String)
    - `property_id` (String) -> Links to `properties`
    - `flat_number` (String)
    - `bed_id` (String)
    - `status` (String: "Active", "Inactive", "Lead")
    - `snoozed_alerts` (Map)

### `vendors`
- **Description:** Stores information about all third-party vendors.
- **Fields:**
    - `vendor_id` (String)
    - `vendor_name` (String)
    - `service_category` (String)
    - `contact_person` (String)
    - `phone_number` (String)
    - `activity_log` (Array of Objects)
        - `date` (Timestamp)
        - `note` (String)
    - `files` (Array of Objects)
        - `file_name` (String)
        - `storage_url` (String)

### `financial_ledger`
- **Description:** The immutable record of all financial transactions.
- **Fields:**
    - `transaction_id` (String)
    - `date` (Timestamp)
    - `amount` (Number)
    - `type` (String: "Revenue", "Expense")
    - `category` (String) -> Links to `Chart of Accounts`
    - `description` (String)
    - `linked_entity_id` (String) -> Links to `tenants` (svh_id) or `vendors` (vendor_id)
    - `payment_method` (String: "Manual UPI", "Manual Cash")
    - `is_corrected` (Boolean)
    - `reversing_transaction_id` (String, optional)

### `complaints`
- **Description:** Stores all tenant complaints and service requests.
- **Fields:**
    - `complaint_id` (String)
    - `tenant_id` (String) -> Links to `tenants`
    - `property_id` (String) -> Links to `properties`
    - `date_filed` (Timestamp)
    - `summary` (String)
    - `status` (String: "New", "In Progress", "Resolved")
    - `snooze_until_date` (Timestamp, optional)

### `meters` & `electricity_readings`
- **Description:** As defined in the electricity billing bill.