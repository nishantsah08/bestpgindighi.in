# 03 - Development Workflow

This document outlines the standard operating procedure for making any change to the system's business logic or code.

## The Hybrid Policy Model

We use a hybrid model to manage system policies, providing both safety and flexibility.

1.  **Tier 1: Foundational Policies (Managed as Code):**
    *   **What:** Core, high-impact business rules with complex interactions.
    *   **How:** Managed as structured YAML files in the `parliament/policies/` directory.
    *   **Change Process:** Requires a formal developer workflow (Pull Request, Supreme Court Review, merge).

2.  **Tier 2: Operational Parameters (Managed via GUI):**
    *   **What:** Simple, low-risk variables.
    *   **How:** Managed via a secure Admin Portal GUI by authorized users.
    *   **Safety:** The GUI's editable fields and their validation rules are defined in the Tier 1 policy files.

## The Supreme Court Review

All proposed changes to Foundational Policies are subject to a rigorous, automated safety check to ensure system-wide consistency. This process is defined in the Judiciary's guiding document.

- **Canonical Documentation:** [`judiciary/00_JUDICIAL_REVIEW_PROCESS.md`](../judiciary/00_JUDICIAL_REVIEW_PROCESS.md)

This review includes:
- **Event-Based Impact Analysis:** Analyzing how a change affects all connected components in the system's 3D logical model.
- **Data & Policy Versioning:** Ensuring that any change that alters data structure is properly versioned and that the system can handle both old and new data formats.

## Configuration Loading Strategy

The system loads configuration in layers to prevent conflicts:

1.  **Defaults from File:** The application first loads the default values from the policy files in the code.
2.  **Overrides from Database:** It then loads the current values set by the GUI from a configuration database.
3.  **Merge:** The database values always overwrite the file defaults.

## Automated Deployment (CI/CD)

Any code or policy change that is successfully validated and merged into the `main` branch will automatically trigger a deployment pipeline.
