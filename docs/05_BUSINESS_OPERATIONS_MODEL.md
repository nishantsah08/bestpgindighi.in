# 05 - Business Operations Model

This document outlines the definitive, end-to-end models for core business processes.

---

## 1. Tenant Onboarding Process

This process is designed to be highly autonomous, triggered by a financial event and driven by AI, with human oversight at critical escalation points.

**Trigger:** The process begins when the **Financial AI Agent** successfully processes a WhatsApp message indicating a "booking payment" has been received.

### Workflow:

1.  **Provisional Tenant Creation:**
    *   The **Financial AI Agent** calls the `tenants.create_provisional_tenant` MCP capability.
    *   This creates a temporary tenant record containing only the customer's name and contact number.

2.  **Automated Document Request:**
    *   The successful creation of a provisional record triggers the system to call the `notifications.send_verification_form` MCP capability.
    *   An SMS/WhatsApp is immediately sent to the tenant with a link to the secure Police Verification web form.

3.  **AI Verification Loop:**
    *   The tenant submits their documents (Aadhar, photo, etc.) via the form.
    *   This submission triggers the `documents.analyze_and_verify` MCP capability.
    *   The **Verification AI** analyzes the documents for clarity, completeness, and validity.
    *   **If documents are invalid:** The AI calls the `notifications.send_rejection_message` capability. A pre-defined message is sent to the tenant explaining the issue and providing the link to re-upload. This loop continues for a maximum of three attempts.
    *   **If documents are valid:** The AI calls the `tenants.approve_verification` capability, which updates the tenant's status to "Verified".

4.  **Caretaker Notification:**
    *   Upon successful verification, the system calls the `notifications.send_whatsapp_audio` MCP capability.
    *   A pre-recorded audio message is sent to the Caretaker's WhatsApp, authorizing them to assign a bed to the named tenant.

5.  **Failure Escalation Path:**
    *   If the AI Verification Loop fails three consecutive times, the process is halted.
    *   The system automatically calls the `judiciary.file_case` MCP capability to create a new case.

6.  **Judicial Review & CEO Approval:**
    *   The Judiciary AI reviews the case and recommends a verdict.
    *   If the case involves a financial dispute > ₹500, it enters the `PENDING_CEO_APPROVAL` state.
    *   The CEO approves, rejects, or modifies the verdict via the Internal System Portal.

7.  **Post-Verdict Execution:**
    *   Once a final verdict is determined, the system calls the appropriate MCP capability to enforce it (e.g., `financial.issue_refund`, `tenants.finalize_verification`).

### Cost Impact Statement

The Verification AI will incur computational costs for each document analysis. This process is governed by the `17_COST_OPTIMIZATION_STRATEGY.yaml` policy. The implementation must include logging for each analysis event to monitor and control these costs.
