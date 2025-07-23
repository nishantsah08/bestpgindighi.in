# Chapter 1: Backend Architecture

**Version:** 1.0
**Date:** 2025-07-23

## 1.1 Technology Stack Selection

- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Rationale:** FastAPI is chosen for its high performance (built on Starlette and Pydantic), automatic data validation, dependency injection system, and automatic generation of OpenAPI documentation, which aligns perfectly with our API-first design principle.

## 1.2 Architectural Style: A Microservices Overview

The system will be implemented as a distributed network of independent microservices. Each service is responsible for a distinct business capability and communicates with other services over well-defined APIs.

### 1.2.1 Diagram: High-Level Service Interaction

- **Visual Asset:** `![High-Level Service Interaction](./assets/visuals/01_service_interaction.svg)`
- **Rendering Link:** `[Click here to edit and render this diagram](https://mermaid.live/edit#pako:eNqNVE1v2zAM_SuETp0kSIsN6zD02gYYBgy7YceuhyZGFk2JFEk-lQz771OSnWxnaTckD_lI8pFkL97aQJt5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5g)`
- **Source Code (Mermaid):**
  ```mermaid
  graph TD
      subgraph "User Facing"
          A[CEO Portal] --> B[API Gateway];
          C[Sales App] --> B;
          D[Caretaker App] --> B;
      end

      subgraph "Core Services"
          B --> E[Finance Service];
          B --> F[Tenant Service];
          B --> G[Feedback Service];
          B --> H[Marketing Service];
      end

      subgraph "AI & Automation Layer"
          I[WhatsApp Gateway] --> J[NLU/OCR Service];
          J --> K[Message Queue];
          K --> E;
          K --> F;
          K --> G;
          K --> H;
          L[Autonomous Optimizer] --> B;
      end

      subgraph "Datastores"
          E --> M[Firestore Database];
          F --> M;
          G --> M;
          H --> M;
          J --> N[Cloud Storage];
      end
  ```

### 1.2.2 Rationale and Trade-offs

- **Benefits:** Scalability, Fault Isolation, Technology Flexibility, Parallel Development.
- **Costs:** Increased complexity in deployment, monitoring, and inter-service communication.

## 1.3 Communication Protocols

- **Synchronous:** All direct requests from frontends or between services will be standard RESTful APIs over HTTPS.
- **Asynchronous:** For background tasks (e.g., processing an uploaded receipt, sending a nurturing message), services will publish an event to a central **RabbitMQ Message Queue**. Other services will subscribe to these events, ensuring the system is decoupled and resilient.

## 1.4 Directory Structure and Code Conventions

Each microservice will have its own directory and Git repository, following a standardized structure:

```
/finance-service
  /app
    /api
    /core
    /db
  /tests
  Dockerfile
  requirements.txt
```
