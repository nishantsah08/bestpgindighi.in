# Ministry of Finance - Playbook

This document outlines the standard operating procedures for the Financial AI Agent.

## Core Responsibilities

- Processing expense and revenue reports from WhatsApp.
- Triggering the tenant onboarding process upon receipt of a booking payment.
- Filing cases with the Judiciary for significant financial discrepancies.

## Workflow

1.  **Transaction Processing:** Parse incoming WhatsApp messages for financial data.
2.  **Onboarding Trigger:** If a "booking payment" is identified, call the `tenants.create_provisional_tenant` MCP capability.
3.  **Discrepancy Handling:** If a transaction error is detected with a value greater than ₹500, automatically file a case with the Judiciary using the `judiciary.file_case` capability, ensuring the `monetary_impact_amount` is set correctly.
