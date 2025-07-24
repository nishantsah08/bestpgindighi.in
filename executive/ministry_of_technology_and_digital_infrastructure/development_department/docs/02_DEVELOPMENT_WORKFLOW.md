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
- **Judicial Process Integration:** Ensuring that any new process includes appropriate triggers for filing judicial cases and handling their verdicts.
- **Event-Based Impact Analysis:** Analyzing how a change affects all connected components in the system's 3D logical model.
- **Data & Policy Versioning:** Ensuring that any change that alters data structure is properly versioned and that the system can handle both old and new data formats.

## Configuration Loading Strategy

The system loads configuration in layers to prevent conflicts:

1.  **Defaults from File:** The application first loads the default values from the policy files in the code.
2.  **Overrides from Database:** It then loads the current values set by the GUI from a configuration database.
3.  **Merge:** The database values always overwrite the file defaults.

## Policy Enforcement Engine

The system will use a standardized, open-source YAML-based rules engine (e.g., Arta, py-rules-engine) to enforce the policies defined in the `parliament_policies/acts/` directory.

### Rule Development Lifecycle

1.  **Rule Creation:** Business logic rules are defined in human-readable `.yaml` files.
2.  **Rule Testing:** Each rule must be accompanied by a set of unit tests that validate its logic against a predefined set of inputs and expected outputs.
3.  **Promotion:** Once tested, the rule is submitted for Supreme Court Review as part of a formal Pull Request.

## Implementation-Level Design Documents

For any new, non-trivial component (e.g., a new MCP server, a complex mobile app feature), a dedicated implementation-level design document must be created. This document will detail the specific code structure, algorithms, and data flows, serving as a guide for development and a reference for future maintenance.

## Cost Impact Analysis

All new architectural proposals must include a "Cost Impact Statement" that demonstrates adherence to the `17_COST_OPTIMIZATION_STRATEGY.yaml` policy.

## Automated Deployment (CI/CD)

Any code or policy change that is successfully validated and merged into the `main` branch will automatically trigger a deployment pipeline.

## Mobile Application Update Strategy

For internally distributed mobile applications, a mandatory, blocking update flow is required to ensure all devices run the latest version.

1.  **Private Distribution:** The CI/CD pipeline will build and sign the Android application package (`.apk`) and upload it to a private, secure storage location (e.g., Supabase Storage). The pipeline will also update a version manifest file on the server.
2.  **Forced Update Check:** Upon application launch, the app must immediately and silently check the server's version manifest before loading any other part of the application.
3.  **Blocking UI:** If the application's version is older than the server's version, the application must immediately present a full-screen, non-dismissible overlay that blocks all other UI elements.
4.  **Mandatory Download & Install:** This blocking screen will display the download progress of the new `.apk` file. Once the download is complete, the user will be presented with a single option: "INSTALL UPDATE". Tapping this button will launch the Android system's package installer.
5.  **Security Permission:** This flow requires the user to grant the "Install unknown apps" permission for the application on their device. The app should guide the user through this process if the permission is not already granted.