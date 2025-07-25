# Case C28: CI/CD Workflow Configuration Failure

**Date:** 2025-07-25

**Subject:** Analysis and resolution of persistent CI/CD pipeline failures related to Terraform, Docker, and Google Cloud Run deployments.

## 1. Summary of Failure

The CI/CD pipeline, as defined in `.github/workflows/main.yml`, experienced a series of cascading failures. Initial attempts to build and deploy the system resulted in race conditions, "resource already exists" errors, and deployment timeouts. The root cause was an overly complex and improperly sequenced workflow that attempted to manage application deployment and infrastructure provisioning within the same monolithic Terraform process.

## 2. Root Cause Analysis

A review of the Git history revealed a clear pattern of failure stemming from a violation of the "separation of concerns" principle.

*   **Initial Error - Race Condition:** The workflow initially tried to deploy Cloud Run services with Terraform *before* the Docker images for those services had been built and pushed to the Artifact Registry. This was a fundamental race condition.
*   **Misapplication of Terraform:** Subsequent attempts to fix this involved complex `terraform import` and multi-phase `terraform apply` steps. This was a misapplication of the tool. Terraform is designed for managing the state of long-lived infrastructure, not for the frequent, operational task of deploying new application versions. This led to state conflicts, hanging processes, and unreliable execution.
*   **Incorrect Permissions Configuration:** The final point of failure was the incorrect use of the `allow_unauthenticated` parameter within the `deploy-cloudrun` GitHub Action. The correct and most reliable method is to deploy the service first and then apply IAM permissions as a separate, explicit step.

## 3. The Resolution (The Precedent)

The successful and now-mandated workflow is defined by its simplicity and clear separation of concerns.

1.  **One-Time Setup:** Foundational infrastructure that rarely changes (like the Artifact Registry repository itself) should be created manually or via a separate, infrequently run Terraform configuration. It should not be part of the main, frequently-run CI/CD pipeline.
2.  **CI/CD Pipeline Mandate:** The primary CI/CD workflow for application deployment **must** follow this sequence:
    a.  **Authenticate:** Authenticate to the cloud provider.
    b.  **Build & Push:** Build the container image and push it to the registry.
    c.  **Deploy:** Deploy the new image to the service using the official, purpose-built deployment action (e.g., `google-github-actions/deploy-cloudrun`).
    d.  **Configure:** Apply any necessary configurations (e.g., IAM permissions) as a distinct, final step.

## 4. Binding Judgment

Any future CI/CD workflow for application deployment within this project must adhere to the simplified "Build, Push, Deploy, Configure" sequence. The use of Terraform for the direct deployment of application services within a continuous integration pipeline is hereby prohibited to prevent the recurrence of these failures. This case establishes the precedent that operational deployment logic must be separated from declarative infrastructure management.
