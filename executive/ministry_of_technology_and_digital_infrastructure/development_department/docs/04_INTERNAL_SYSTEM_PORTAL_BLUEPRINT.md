# 04 - Internal System Portal Blueprint

This document outlines the structural blueprint and feature set for the CEO's Internal System Portal.

**Authentication:** Secure login via the CEO's designated Google Account.

---

### 1. Main Dashboard (Landing Page)

- **Purpose:** To provide a single-glance overview of the business, framed around the four critical inversion risks.
- **Structure:** The dashboard will be divided into four main quadrants:
    1.  **Compliance Risk:** Displays the output of the `getComplianceStatusReport` (pending verifications, agreements, etc.).
    2.  **Financial Risk:** Displays the outputs of `getPendingRentReport`, `getTotalCashAtHand`, and `getProjectedRevenueNextMonth`.
    3.  **Reputation Risk (GBL):** Displays the outputs of `getCustomerComplaintsReport` and `getLeadFunnelReport`.
    4.  **Key Person Risk (Caretaker):** Also displays the `getCustomerComplaintsReport` as a proxy for operational stress.

---

### 2. Main Navigation Menu (Sidebar)

- Dashboard
- Cabinet Secretary (Query Interface)
- Ministry of Finance
- Ministry of Growth & Commerce (Sales)
- Ministry of Property & Tenant Welfare (Caretaker)
- Ministry of Technology & Digital Infrastructure
- Vendor Directory
- Settings

---

### 3. Section Details

#### 3.1 Cabinet Secretary (Query Interface)
- **Purpose:** A powerful, LLM-driven interface for the CEO to ask complex questions that span across internal system data and the open internet.
- **Implementation:** This is a highly complex feature that will be implemented in phases.
    - **Phase 1:** The initial version will support a limited set of structured queries (e.g., "show me all expenses in the Maintenance category for last month").
    - **Future Phases:** Will progressively add more complex, natural language capabilities and integration with external data sources, requiring a dedicated technical design document.

#### 3.2 Ministry of Finance
- **Purpose:** The deep-dive section for all financial data and control.
- **Sub-Pages:** Financial Statements (P&L, Balance Sheet, Cash Flow), General Ledger (with Transaction Correction feature), and Inventory Management.

#### 3.3 Ministry of Growth & Commerce (Sales)
- **Purpose:** To monitor the performance of the sales and marketing functions.
- **Components:** Lead Funnel Visual, Tenant Onboarding Status, Revenue Analytics, and the **GBL Review Link Generator** tool.

#### 3.4 Ministry of Property & Tenant Welfare (Caretaker)
- **Purpose:** To monitor the operational health of the physical properties.
- **Components:** Maintenance Ticket Dashboard, Tenant Satisfaction Metrics, and Property Inspection Reports.

#### 3.5 Ministry of Technology & Digital Infrastructure
- **Purpose:** To provide a high-level overview of the health and status of the digital infrastructure.
- **Components:** System Status Dashboard, Deployment Logs, and a high-level Error Monitoring summary.

#### 3.6 Vendor Directory
- **Purpose:** The web-based interface for managing all vendor information.
- **Features:** A searchable list of vendors, with profile pages containing full financial transaction history, interaction logs, and uploaded files.

#### 3.7 Settings
- **Purpose:** A section for system-level configurations.
- **Components:** User Management, Notification Preferences, and configuration for financial categories.