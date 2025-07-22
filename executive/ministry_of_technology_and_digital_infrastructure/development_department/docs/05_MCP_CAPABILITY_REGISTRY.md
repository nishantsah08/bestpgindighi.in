# 05 - MCP Capability Registry

This document is the definitive, canonical registry of all capabilities exposed through the Model Context Protocol (MCP) within the SVH Enterprise ecosystem. Each entry represents a secure "socket" that authorized AI agents and applications can plug into.

## Registry Format

Each registered capability must include the following information:

- **Capability ID:** A unique, machine-readable identifier (e.g., `financial.billing.create_invoice`).
- **Description:** A human-readable explanation of what the capability does.
- **Owner:** The Executive Ministry or independent body responsible for the service that provides this capability.
- **Service Endpoint:** The network location of the MCP-compliant service.
- **Access Control List (ACL):** A list of the specific AI agents or application roles that are authorized to use this capability.
- **Schema (Input/Output):** A reference to the data schema for the capability's inputs and outputs.

---

## Registered Capabilities

### Financial Capabilities

- **Capability ID:** `financial.ledger.record_transaction`
- **Description:** Records a new transaction in the general ledger.
- **Owner:** Ministry of Finance
- **Service Endpoint:** `https://mcp.bestpgindighi.in/finance/ledger`
- **ACL:** `[Financial_AI_Agent, CEO_App]`
- **Schema:** `schemas/financial/transaction.json`

- **Capability ID:** `financial.billing.create_invoice`
- **Description:** Creates a new monthly invoice for a tenant.
- **Owner:** Ministry of Finance
- **Service Endpoint:** `https://mcp.bestpgindighi.in/finance/billing`
- **ACL:** `[Financial_AI_Agent]`
- **Schema:** `schemas/financial/invoice.json`

### Tenant Management Capabilities

### Tenant Management Capabilities

- **Capability ID:** `tenants.create_provisional_tenant`
- **Description:** Creates a temporary tenant record upon receipt of a booking payment.
- **Owner:** Property & Tenant Welfare
- **Service Endpoint:** `https://mcp.bestpgindighi.in/tenants/provisional`
- **ACL:** `[Financial_AI_Agent]`
- **Schema:** `schemas/tenants/provisional_tenant.json`

- **Capability ID:** `tenants.approve_verification`
- **Description:** Finalizes a tenant's record. For internal use by the Verification AI only.
- **Owner:** Property & Tenant Welfare
- **Service Endpoint:** `https://mcp.bestpgindighi.in/tenants/verify`
- **ACL:** `[Verification_AI]`
- **Schema:** `schemas/tenants/verification.json`

- **Capability ID:** `tenants.maintenance.create_request`
- **Description:** Creates a new maintenance request for a tenant.
- **Owner:** Property & Tenant Welfare
- **Service Endpoint:** `https://mcp.bestpgindighi.in/tenants/maintenance`
- **ACL:** `[Caretaker_AI_Agent, Caretaker_App, CEO_App]`
- **Schema:** `schemas/tenants/maintenance_request.json`

### Document & Notification Capabilities

- **Capability ID:** `documents.analyze_and_verify`
- **Description:** Triggers the Verification AI to analyze a submitted document set.
- **Owner:** Ministry of Technology & Digital Infrastructure
- **Service Endpoint:** `https://mcp.bestpgindighi.in/verification/analyze`
- **ACL:** `[System_Internal]`
- **Schema:** `schemas/documents/analysis_request.json`

- **Capability ID:** `notifications.send_verification_form`
- **Description:** Sends the initial SMS/WhatsApp with the link to the verification form.
- **Owner:** Ministry of Technology & Digital Infrastructure
- **Service Endpoint:** `https://mcp.bestpgindighi.in/notifications/send`
- **ACL:** `[System_Internal]`
- **Schema:** `schemas/notifications/form_request.json`

- **Capability ID:** `notifications.send_whatsapp_audio`
- **Description:** Sends a pre-recorded WhatsApp audio message.
- **Owner:** Ministry of Technology & Digital Infrastructure
- **Service Endpoint:** `https://mcp.bestpgindighi.in/notifications/send_audio`
- **ACL:** `[System_Internal]`
- **Schema:** `schemas/notifications/audio_request.json`
