# Operational Parameters for Tenant Onboarding

### Financial Parameters

*   **`minimum_advance_rent`**: The absolute minimum advance rent payment required to secure a booking. Any amount above this is accepted at the discretion of the Sales person.
    *   **value**: 2000

*   **`accepted_payment_methods`**: The list of allowed payment channels.
    *   **methods**: ['UPI']

*   **`police_verification_fee`**: The fee charged for police verification.
    *   **amount**: 200

### Documentation Parameters

*   **`rule_book_document_id`**: The internal system ID for the official Rule Book document.
    *   **value**: "doc_RuleBook_v1.2" # Placeholder ID

### Business Roles

*   **`defined_roles`**: The list of human roles interacting with this policy.
    *   **roles**: ['CEO', 'Sales', 'Caretaker']