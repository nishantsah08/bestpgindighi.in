# Operational Parameters for Monthly Billing & Collections

### Bill Format

*   **`output_format`**: Defines the format for delivering bills to tenants.
    *   **value**: 'whatsapp_message'
*   **`include_payment_link`**: Specifies whether to include a pre-filled UPI payment link.
    *   **value**: true

### Payment Confirmation

*   **`confirmation_type`**: Defines how payments are confirmed.
    *   **value**: 'manual'
    *   **description**: 'A human operator must manually mark a bill as Paid after verifying the UPI transaction.'

### Automated Reminders

*   **`reminder_schedule`**: Defines the schedule for sending automated payment reminders.
    *   **description**: 'Parameters for when and how often to send reminders for overdue bills.'
    # Specific values to be defined.