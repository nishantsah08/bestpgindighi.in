# Security Model

**Version:** 1.0
**Date:** 2025-07-22

## 1. Core Principles

- **Principle of Least Privilege:** All components (human and AI) will only have the minimum permissions necessary to perform their defined roles.
- **Defense in Depth:** Security will be applied in layers, from the frontend applications to the backend infrastructure.

## 2. Authentication

- **Method:** Google Login (OAuth 2.0) will be the sole method of authentication for all user-facing systems (Internal Portal, Mobile Apps).
- **Rationale:** This delegates user authentication to Google's robust and secure infrastructure, reducing our security surface area.

## 3. Authorization

- **Internal Portal:** Access is restricted to the CEO's specific Google account ID.
- **Mobile Apps:** User roles (CEO, Sales, Caretaker) are assigned to specific Google account IDs. The application will enforce features based on the authenticated user's role.
- **MCP Servers:** Each MCP capability will verify the role of the calling user before executing any operation.

## 4. Data Security

- **Firestore Rules:** Granular security rules will be implemented to control access to data collections. For example:
    - The `financial_ledger` can only be read by the CEO and the Financial AI Agent.
    - Tenant profiles can only be modified by authorized agents (e.g., Sales).
- **Encryption at Rest:** All data stored in Firestore and Google Cloud Storage is automatically encrypted by Google.
- **Encryption in Transit:** All data transmitted between clients and servers will use TLS (HTTPS).

## 5. Secret Management

- **API Keys & Secrets:** All third-party API keys (e.g., WhatsApp Business API token) and system secrets will be stored securely using Google Cloud Secret Manager.
- **Access:** Only specific Google Cloud Functions (MCP Servers) will be granted IAM permissions to access specific secrets at runtime. Secrets will not be stored in source code or environment variables.