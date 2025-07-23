# Chapter 4: Frontend Architecture

**Version:** 1.0
**Date:** 2025-07-23

## 4.1 Technology Stack Selection

- **Core Framework:** React 18+ with TypeScript
- **Build Tool:** Vite
- **UI Component Library:** Material-UI (MUI)
- **State Management:** Redux Toolkit
- **API Client:** Orval (for automatic generation from OpenAPI spec)

## 4.2 UI Component Library: Material-UI (MUI)

To ensure a professional, consistent, and high-quality user experience, all user interfaces will be built using the MUI component library. This provides a comprehensive set of pre-built, accessible, and themeable components (buttons, forms, charts, etc.) that align with the principles in our `10_DESIGN_SYSTEM.md`.

## 4.3 State Management Strategy: Redux Toolkit

For predictable and scalable state management, we will use Redux Toolkit. It provides a standardized, opinionated way to manage application state, which is crucial for complex dashboards and data-driven applications.

### 4.3.1 Diagram: Frontend Component Architecture

- **Visual Asset:** `![Frontend Component Architecture](./assets/visuals/04_frontend_architecture.svg)`
- **Rendering Link:** `[Click here to edit and render this diagram](https://mermaid.live/edit#pako:eNqNVE1v2zAM_SuETp0kSIsN6zD02gYYBgy7YceuhyZGFk2JFEk-lQz771OSnWxnaTckD_lI8pFkL97aQJt5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5g)`
- **Source Code (Mermaid):**
  ```mermaid
  graph TD
      subgraph "User Interaction"
          A[User] --> B[React Components];
      end

      subgraph "Application Layer"
          B --> C{Redux Actions};
          C --> D[Redux Store];
          D --> B;
          C --> E[API Client];
      end

      subgraph "Data Layer"
          E --> F(Backend API);
      end
  ```

## 4.4 API Client Generation

To ensure the frontend is always perfectly in sync with the backend API, we will use **Orval**. This tool will read the `02_API_SPECIFICATION.yaml` file and automatically generate a fully-typed TypeScript client for making API calls. This eliminates manual coding of API requests and ensures type safety.

## 4.5 Directory Structure and Code Conventions

The frontend codebase will follow a standard, feature-based directory structure:

```
/ceo-portal
  /src
    /components
    /features
      /dashboard
      /finance
    /hooks
    /services
      /api (auto-generated)
    /store
  /public
  package.json
```
