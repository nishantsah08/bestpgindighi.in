# Release Plan: Core Call Recording & Contact Management System

This document outlines the three-phase development plan to implement the foundational call recording and customer contact management system.

---

### **Phase 1: Backend API Development**

**Branch:** `feature/call-recording-and-contacts-backend`

**Goal:** To create the complete backend infrastructure for a centralized contact database and to integrate it seamlessly with the call recording system.

1.  **Update Data Model:** Define two new collections in `docs/06_DATABASE_SCHEMA.md`: `contacts` (for customer profiles) and `call_logs`.
2.  **Implement Call Upload & Contact Linking API:** Build the `POST /v1/calls/upload` endpoint. This endpoint will now perform the following logic:
    *   Receive the call recording and metadata.
    *   Search for an existing contact using the customer's phone number.
    *   If no contact exists, automatically create a new one with a status of "New Lead".
    *   Save the audio file to storage.
    *   Create a new document in the `call_logs` collection, ensuring it is linked to the correct contact profile.
3.  **Implement Contact Management APIs:** Build a full suite of CRUD (Create, Read, Update, Delete) APIs for managing contacts:
    *   `GET /v1/contacts`: To list and search all contacts.
    *   `POST /v1/contacts`: To manually create a new contact.
    *   `GET /v1/contacts/{id}`: To retrieve the full details and interaction history of a single contact.
    *   `PUT /v1/contacts/{id}`: To update a contact's information.
4.  **Implement E.164 Normalization:** Upgrade the system to handle international phone numbers by default. All incoming phone numbers will be parsed and stored in the robust E.164 standard format, as defined in the `10_customer_interaction_and_call_management_bill.yaml`.
5.  **Automated Testing:** Create and run automated tests for all new endpoints, verifying the contact creation, call linking, and data retrieval logic.

---

### **Phase 2: Internal Dashboard UI Development**

**Branch:** `feature/call-recording-and-contacts-dashboard`

**Goal:** To create the user interface within the internal dashboard for viewing and managing both call logs and the central contact database.

1.  **Create New UI Components:** Develop new React components for a "Call Logs" viewer and a full "Contact Management" page.
2.  **Connect to Backend:** The new components will fetch data from the `GET /v1/calls` and `GET /v1/contacts` API endpoints created in Phase 1.
3.  **Display Data:**
    *   The "Call Logs" page will list all recordings.
    *   The "Contact Management" page will allow users to search, view, create, and edit customer profiles, and see the list of recorded calls associated with each customer.
4.  **Add Navigation:** Integrate the new "Call Logs" and "Contacts" pages into the main navigation of the internal portal.
5.  **Build Verification:** Run `npm run build` to ensure the new frontend code compiles and integrates correctly.

---

### **Phase 3: Native Mobile Application Development**

**Branch:** `feature/call-recording-and-contacts-mobile`

**Goal:** To update the three native Android applications to record and upload calls, leveraging the new backend contact management system.

*This phase will be executed in parallel by the mobile development team.*

1.  **Implement Call Recording:** Add functionality to the apps to programmatically record the audio of outbound calls.
2.  **Integrate with Backend:** Upon call completion, the apps will send the recorded audio file and its associated metadata to the `POST /v1/calls/upload` backend endpoint. The backend will handle all contact creation and linking logic automatically.