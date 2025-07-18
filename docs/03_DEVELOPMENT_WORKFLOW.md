# 03 - Development Workflow

This document outlines the standard operating procedure for making any change to the system's business logic or code.

## The Hybrid Policy Model

We use a hybrid model to manage system policies, providing both safety and flexibility.

1.  **Tier 1: Foundational Policies (Managed as Code):**
    *   **What:** Core, high-impact business rules with complex interactions (e.g., rent calculation logic).
    *   **How:** Managed as structured YAML files in the `parliament/policies/` directory.
    *   **Change Process:** Requires a formal developer workflow (Pull Request, validation, merge).

2.  **Tier 2: Operational Parameters (Managed via GUI):**
    *   **What:** Simple, low-risk variables (e.g., the value of a late fee, a feature flag).
    *   **How:** Managed via a secure Admin Portal GUI by authorized users.
    *   **Safety:** The GUI's editable fields and their validation rules are defined in the Tier 1 policy files.

## The `bludeprint validation tool`

This is an automated safety net that runs on every proposed change to a Foundational Policy.

1.  **Decomposition:** It first breaks down all business policies into their smallest atomic logical rules.
2.  **Simulation:** It runs a suite of logical scenarios (happy paths, conflicts, edge cases) against the full set of rules.
3.  **Validation:** It checks for any contradictions, dead ends, or inconsistencies. A change is only approved if all checks pass.

## Configuration Loading Strategy

To prevent conflicts between the two policy tiers, the system loads configuration in layers:

1.  **Defaults from File:** The application first loads the default values from the policy files in the code.
2.  **Overrides from Database:** It then loads the current values set by the GUI from a configuration database.
3.  **Merge:** The database values always overwrite the file defaults, ensuring GUI changes are preserved across deployments.

## Automated Deployment (CI/CD)

Any code or policy change that is successfully validated and merged into the `main` branch of a component will automatically trigger a deployment pipeline, ensuring that the production environment is always up-to-date with the latest stable version.