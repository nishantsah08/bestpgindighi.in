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

## The Planning Commission Review

All proposed changes to the system, whether architectural, design-oriented, or significant new features, must first undergo a **Planning Commission Review**. This is a mandatory step to ensure strategic alignment and architectural soundness before any development work begins.

- **Canonical Documentation:** [`independent_bodies/planning_commission/README.md`](../../../../independent_bodies/planning_commission/README.md)



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

## Development Environment & Parallel Workflows

To ensure a stable, reproducible, and isolated development process, this project adheres to a container-based and multi-workspace strategy.

### **1. Environment Isolation**

The host development machine, which is optimized for native Android development, will not be modified. All other development environments are to be provisioned and run inside isolated containers.

*   **Backend & Frontend Environments:** Development for the Python/FastAPI backend and the React/TypeScript frontend will be conducted exclusively within **Docker containers**. The project will contain `Dockerfile` and `docker-compose.yml` files that define these environments as code. This guarantees a consistent development environment for all team members and prevents any contamination of the host machine. The production environment consists of Firebase Hosting and Google Cloud Functions.
*   **Native Android Environment:** The native Android environment on the host machine remains pristine. Its configuration will be made reproducible through:
    *   The **Gradle Wrapper (`gradlew`)** to enforce a consistent build tool version.
    *   Explicit library and SDK versions defined in the `build.gradle` files.
    *   A `src/mobile/SETUP.md` file that will document the initial machine setup steps (e.g., which core Android SDKs to install).

### **2. Parallel Development (Multi-Workspace Strategy)**

To enable multiple Gemini instances to work on different features simultaneously without conflict, a multi-workspace approach is mandated.

1.  **Primary Workspace:** The main project folder is used for project management, code review, and integration.
2.  **Feature Workspaces:** For each major, independent feature, a new, separate clone of the repository must be created in a dedicated folder (e.g., `bestpgindighi-feature-billing`).
3.  **Isolated Instance:** A dedicated Gemini CLI instance is to be launched for each feature workspace.
4.  **Feature Branching:** Within its isolated workspace, the Gemini instance will create and work on a specific feature branch (e.g., `feature/billing`).
5.  **Integration via Pull Request:** Upon completion, the feature branch will be pushed to the central GitHub repository. The work will then be reviewed and merged into the `main` branch via a formal Pull Request.

This strategy combines the physical isolation of separate directories with the logical isolation of Git branches, enabling safe and scalable parallel development.