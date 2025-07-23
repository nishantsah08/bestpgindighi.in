# Chapter 3: Database Implementation Guide

**Version:** 1.0
**Date:** 2025-07-23

## 3.1 Database Choice

The system will use **Google Cloud Firestore** in Native mode, chosen for its scalability, real-time capabilities, and robust security model.

## 3.2 Detailed Collection Schemas

This document cross-references the canonical schemas defined in `docs/06_DATABASE_SCHEMA.md`.

### 3.2.1 Diagram: Entity-Relationship Diagram (ERD)

- **Visual Asset:** `![Entity-Relationship Diagram](./assets/visuals/03_erd.svg)`
- **Rendering Link:** `[Click here to edit and render this diagram](https://mermaid.live/edit#pako:eNqNVE1v2zAM_SuETp0kSIsN6zD02gYYBgy7YceuhyZGFk2JFEk-lQz771OSnWxnaTckD_lI8pFkL97aQJt5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5g)`
- **Source Code (Mermaid):**
  ```mermaid
  erDiagram
      TENANTS ||--o{ FEEDBACK : "submits"
      TENANTS {
          string tenant_id PK
          string name
          string status
      }
      FEEDBACK {
          string feedback_id PK
          string tenant_id FK
          timestamp timestamp
          float calculated_overall_satisfaction_score
      }
  ```

## 3.3 High-Performance Indexing Strategy

To ensure fast and cost-effective queries, the following composite indexes must be created in Firestore:

- **`tenant_feedback` Collection:**
  - `tenant_id` (ASC), `timestamp` (DESC) - To quickly retrieve all feedback for a specific tenant, sorted by most recent.
- **`general_ledger` Collection:**
  - `category` (ASC), `date` (DESC) - To efficiently query for expenses by category for a given time range.

## 3.4 Data Access Patterns & Best Practices

- **Minimize Reads:** Always query for the specific fields needed. Avoid fetching entire documents if only a few fields are required.
- **Use Caching:** For frequently accessed, non-volatile data (e.g., system settings), implement a caching layer to reduce database reads.

## 3.5 Firestore Security Rule Implementation

Firestore security rules are the primary mechanism for enforcing data access policies.

### 3.5.1 Translating MCP ACLs to Firestore Rules

The ACLs defined in the MCP Registry will be directly translated into Firestore security rules. The user's JWT token, passed from the application, will contain their role (e.g., `CEO_App`, `Financial_AI_Agent`).

### 3.5.2 Sample Rule Implementations

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Only authenticated users with the CEO_App role can read feedback trends
    match /feedback_trends/{trendId} {
      allow read: if request.auth.token.role == 'CEO_App';
    }

    // Only the system can write to the feedback collection
    match /tenant_feedback/{feedbackId} {
      allow write: if request.auth.token.role == 'System_Internal';
    }
  }
}
```
