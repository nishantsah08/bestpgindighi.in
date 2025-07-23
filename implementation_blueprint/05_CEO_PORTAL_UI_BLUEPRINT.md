# Chapter 5: CEO Portal UI/UX Blueprint

**Version:** 1.0
**Date:** 2025-07-23

## 5.1 Overall Application Layout

The portal will use a standard, responsive layout with a persistent sidebar for navigation, a top header bar for user information, and a main content area.

## 5.2 Component Breakdown: The Dashboard

### 5.2.1 Diagram: Dashboard Layout

- **Visual Asset:** `![Dashboard Layout](./assets/visuals/05_dashboard_layout.svg)`
- **Source (ASCII Art Wireframe):**
  ```
  +--------------------------------------------------------------------------+
  | [Logo] Internal System Portal                                [CEO Name]  |
  +--------------------------------------------------------------------------+
  |          |                                                               |
  |          |  **Strategic Proposals Queue**                                |
  |          |  +---------------------------------------------------------+  |
  |          |  | [AI] Monthly Marketing Strategy... [Review Button]      |  |
  |          |  +---------------------------------------------------------+  |
  |          |                                                               |
  |          |  **Operational Quadrants**                                    |
  |          |  +----------------------+  +-------------------------------+  |
  |          |  | Tenant Satisfaction  |  | Financial Health              |  |
  |          |  | [Line Chart]         |  | [Key Metrics: Rent, Cash]     |  |
  |          |  +----------------------+  +-------------------------------+  |
  |          |  +----------------------+  +-------------------------------+  |
  |          |  | Sales & Growth       |  | Judicial & Compliance         |  |
  |          |  | [Funnel Chart]       |  | [Approval Queue]              |  |
  |          |  +----------------------+  +-------------------------------+  |
  |          |                                                               |
  +----------+-------------------------------------------------------------+
  ```

### 5.2.2 Component-to-API Mapping

| Component | API Endpoint Called |
| :--- | :--- |
| Strategic Proposals Queue | `GET /tasks/strategy_proposals` |
| Tenant Satisfaction Chart | `GET /feedback/trends` |
| Financial Health Metrics | `GET /finance/kpis` |
| Sales & Growth Chart | `GET /marketing/funnel` |
| Judicial & Compliance Queue | `GET /tasks/judicial_approvals` |

## 5.3 Component Breakdown: Strategic Proposal Review Modal

### 5.3.1 Diagram: Strategic Proposal Modal Flow

- **Visual Asset:** `![Strategic Proposal Flow](./assets/visuals/05_proposal_flow.svg)`
- **Rendering Link:** `[Click here to edit and render this diagram](https://mermaid.live/edit#pako:eNqNVE1v2zAM_SuETp0kSIsN6zD02gYYBgy7YceuhyZGFk2JFEk-lQz771OSnWxnaTckD_lI8pFkL97aQJt5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5Q5t5g)`
- **Source Code (Mermaid):**
  ```mermaid
  graph TD
      A[User clicks 'Review'] --> B{Load Proposal Data};
      B --> C[Display Proposal in Modal];
      C --> D{User reviews data};
      D --> E[User clicks 'Approve'];
      D --> F[User clicks 'Reject'];
      E --> G[Call POST /strategy/approve];
      F --> H[Call POST /strategy/reject];
  ```
