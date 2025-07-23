# Chapter 8: Infrastructure as Code

**Version:** 1.0
**Date:** 2025-07-23

## 8.1 IaC Tool

All cloud infrastructure will be managed declaratively using **Terraform**. This ensures our infrastructure is reproducible, version-controlled, and can be audited.

## 8.2 Cloud Provider

The system will be deployed exclusively on the **Google Cloud Platform (GCP)**.

## 8.3 High-Level Infrastructure Diagram

- **Visual Asset:** `![GCP Cloud Infrastructure](./assets/visuals/08_gcp_infrastructure.svg)`
- **Source Code (Mermaid):**
  ```mermaid
  graph TD
      subgraph "External World"
          A[Internet] --> B[Cloud Load Balancer];
      end

      subgraph "GCP Project"
          B --> C{API Gateway};
          C --> D[Finance Service (Cloud Run)];
          C --> E[Tenant Service (Cloud Run)];
          C --> F[...other services...];
          D --> G[Firestore Database];
          E --> G;
          F --> G;
          D --> H[RabbitMQ (Message Broker)];
          E --> H;
          I[Cloud Storage] --> D;
      end
  ```

## 8.4 Managed Resources

The following GCP services will be provisioned and managed via Terraform:

- **Compute:** Google Cloud Run for stateless microservices.
- **Database:** Google Cloud Firestore for the primary NoSQL database.
- **Storage:** Google Cloud Storage for documents and images.
- **Messaging:** RabbitMQ deployed on a GKE cluster for asynchronous tasks.
- **Networking:** VPC, Subnets, Firewall Rules, Cloud DNS.
- **Security:** IAM Roles, Service Accounts, Secret Manager.
- **CI/CD:** Artifact Registry for Docker images.

## 8.5 Environment Management

Terraform workspaces will be used to manage three distinct, identical environments:

- `development`
- `staging`
- `production`
