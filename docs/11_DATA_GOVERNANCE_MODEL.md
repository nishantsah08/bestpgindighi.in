# 11 - Data Governance Model

**Version:** 1.0
**Date:** 2025-07-22

## 1. Purpose

This document defines the specific governance and security rules for different categories of data within the system.

## 2. General Data

- **Applies to:** Tenants, Vendors, Financial Ledger, Properties, etc.
- **Access Control:** Role-based access control (RBAC) as defined in the Security Model and implemented via Firestore Rules.
- **Encryption:** Encrypted at rest and in transit by default.

## 3. Sensitive Personal Information (SPI)

- **Applies to:** The psychological profiles and sentiment analysis data generated from employee communications.
- **Heightened Governance Rules:**
    - **Access Control:** Access is restricted to the CEO's unique user ID only. This will be enforced by a specific, non-modifiable Firestore security rule.
    - **Audit Trail:** Every access event (read or view) of this data by the CEO must be logged in a separate, immutable audit log collection.
    - **Data Lifecycle:** The raw analytical data will be retained for a maximum of 180 days. The high-level summary profile will be retained for the duration of employment.
    - **Secure Deletion:** Upon cessation of employment, a formal process will be triggered to securely delete the associated analysis data and profile after a 30-day grace period.