# 11 - Data Governance Model

This document outlines the policies for managing the system's data, with a focus on the NoSQL structure of Firebase Firestore.

## 1. Schema Management

- **Canonical Schema:** The `docs/06_DATABASE_SCHEMA.md` document is the single source of truth for the data model.
- **Schema Evolution:** Any changes to the data model must be backward-compatible. Destructive changes (e.g., deleting a field) are prohibited. Instead, new fields should be added, and old fields should be marked as deprecated.
- **Validation:** All data written to the database must be validated against the canonical schema by the respective MCP service.

## 2. Data Lifecycle Management

- **Data Retention:** Data retention policies are defined in the `01_DATA_PRIVACY_POLICY.md`.
- **Archiving:** Tenant data will be moved to an archived state upon off-boarding.
- **Deletion:** Personally Identifiable Information (PII) will be securely deleted after the legally mandated retention period.

## 3. Data Quality

- **Data Owners:** Each data collection (e.g., `tenants`, `vendors`) has a designated owner (the relevant ministry) responsible for its quality and integrity.
- **Auditing:** The Auditor AI will periodically run data quality checks to identify and report anomalies.

## 4. AI Model Data Governance

### AI-Powered Lead Scoring Model
- **Purpose:** To prioritize sales efforts by predicting the likelihood of a lead converting.
- **Data Sources:** The model will be trained on anonymized historical lead data, including inquiry content, time of inquiry, lead source, and final outcome (converted/not converted).
- **Data Minimization:** Only the data fields explicitly required for the model will be used. No unnecessary PII will be included in the training set.
- **Bias Prevention:** The model and its training data will be regularly audited to ensure it does not exhibit any demographic or other prohibited biases. The goal is to score based on demonstrated interest and intent, not personal characteristics.
- **Data Retention:** The training data for the lead scoring model will be refreshed and retrained periodically. Old training sets will be securely deleted.

### Tenant Feedback Data
- **Purpose:** To measure tenant satisfaction and identify specific areas for operational improvement.
- **Anonymization:** While individual feedback is linked to a `tenant_id` for immediate follow-up, all data used for the CEO's trend analysis dashboard will be anonymized and aggregated. The CEO will see the overall trend, not how a specific individual voted.
- **Data Retention:** Individual feedback records will be retained for the duration of the tenancy and archived for 1 year post-tenancy. Aggregated trend data may be retained indefinitely for long-term analysis.
