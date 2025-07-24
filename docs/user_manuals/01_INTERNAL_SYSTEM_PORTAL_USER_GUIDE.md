# Internal System Portal - User Guide

**For:** CEO, Power Users

### Philosophy: Total Information, Total Control

This web-based portal is the central nervous system of the entire operation. It is the comprehensive dashboard for deep analysis, configuration, and management, designed for use on a desktop computer.

---

### Window 1: The Main Dashboard

The landing page provides a detailed operational overview of the business.

**Functionality:**
*   **Live Occupancy Map:** A visual representation of all properties with color-coded statuses.
*   **Key Operational Metrics:** View real-time data on rent collection progress and open maintenance tickets.
*   **System-Wide Activity Feed:** A detailed, real-time log of all significant events from all applications.
*   **Quick Actions:** Buttons for common administrative tasks like `[+ Add New Tenant]` or `[+ Add Expense]`.

---

### Window 2: Tenant Management

The master database and Customer Relationship Management (CRM) for all tenants.

**Functionality:**
*   A powerful, searchable, and filterable table of all tenants (past, present, and prospective).
*   Clicking a tenant opens their **360-Degree Tenant Profile**, which contains:
    *   All personal and contact details.
    *   A complete, itemized payment history.
    *   A full log of all maintenance requests and other issues.
    *   A record of all communications.
    *   A link to their signed rent agreement PDF.

---

### Window 3: Property & Availability Management

The administrative view for managing all physical assets.

**Functionality:**
*   A hierarchical view of `Properties > Floors > Rooms > Beds`.
*   **Set Rent Prices:** This is the interface used to define the rent for each specific bed.
*   **Manage Status:** Change the status of a bed (e.g., `Available`, `Occupied`, `Under Maintenance`).
*   Upload photos and manage amenity lists for each room.

---

### Window 4: The Parliament

This is the most powerful screen in the portal. It is the Graphical User Interface (GUI) for configuring the live business logic of the system.

**Functionality:**
*   The portal reads all `.yaml` policy files from the `parliament_policies/` directory in the project.
*   It dynamically generates a user-friendly web form for each policy, allowing you to edit its parameters.
*   **Example:** To change the late fee, you would select the "Late Fee Policy." The form would show an input field for "Late Fee Amount (in INR)".
*   When you save a change, the new value is stored in the database and immediately used by the live application, overriding the default value from the code.
