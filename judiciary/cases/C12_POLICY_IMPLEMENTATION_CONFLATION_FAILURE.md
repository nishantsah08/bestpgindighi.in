# Case File: C12 - Policy-Implementation Conflation Failure

- **Incident Date:** 2025-07-22
- **Finding:** The AI agent incorrectly included specific implementation details (a list of required MCP capabilities) within a foundational policy document (`..._bill.yaml`).

- **Root Cause Analysis:** The AI failed to maintain a strict separation between policy and implementation. Policy documents in the `parliament_policies/` directory should define *what* the system must do and the high-level rules it must follow. Implementation details, such as API specifications, function names, or specific data structures, belong in architectural blueprints and design documents within the `executive/` or `docs/` directories.

- **Precedent (The Law of Jurisdictional Clarity):** A strict separation must be maintained between legislative documents (policies) and executive documents (implementation details). Policy bills shall define the high-level goals, rules, and mandates. They must not contain specific technical implementation details like API function names, database field names, or detailed algorithms. Such details must be placed in the appropriate architectural blueprints or design documents.