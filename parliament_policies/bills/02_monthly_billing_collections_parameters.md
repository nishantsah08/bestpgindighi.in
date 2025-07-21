### Core Billing Cycle
*   **billing_generation_day**: `'last_day_of_month'`
*   **payment_due_day**: `5`
*   **grace_period_days**: `5`

### Rent & Proration Policy
*   **first_month_rent_policy**: `'full_month_advance'` (The first month's rent is always collected in full, irrespective of the joining date.)
*   **proration_handling**: `'credit_to_next_cycle'` (A credit for unused days in the first month will be applied as a discount to the second month's bill.)
*   **rent_refund_policy**: `'none'` (Rent payments are non-refundable.)

### Late Fee & Penalty Policy
*   **late_fee_type**: `'flat_fee'`
*   **late_fee_amount_inr**: `100`
*   **max_total_late_fee_inr**: `500`
*   **late_fee_start_day**: `6`
*   **late_fee_end_day**: `10`

### Escalation Timeline
*   **caretaker_follow_up_day**: `11`
*   **sales_escalation_day**: `15`
*   **ceo_escalation_day**: `20`

### Bill Composition
*   **line_items**:
    *   rent
    *   pending_rent
    *   pending_deposit
    *   fines
    *   electricity_bill
    *   maintenance_charges
    *   police_verification_charges
    *   agreement_charges
    *   adjustments
    *   **previous_outstanding**
    *   **discount_amount**

### Payment Methods
*   **accepted_methods**:
    *   "upi"

### Booking & Initial Payment Flexibility Policy

*   **1. Ideal Scenario**:
    *   **rule**: Full `rent` + full `security_deposit` paid in advance to secure booking.

*   **2. Standard Flexibility**:
    *   **rule**: If the ideal scenario is not met, the tenant can pay the full `rent` upfront.
    *   **deposit_deadline**: The full `security_deposit` must then be paid by the 5th of the following month.
    *   **deposit_installments**:
        *   **allow_installments**: `true`
        *   **schedule**: Must be negotiated with and approved by the `Sales` role.

*   **3. Short-Term Booking Hold (Advance Rent Exceptions)**:
    *   **description**: For cases where immediate full rent payment is not possible. The goal is to secure a minimum commitment while managing risk.
    *   **maximum_initial_payment_delay**: `3 days` (The first advance payment, of any amount, must be made within 3 days of verbal agreement).
    *   **tier_1_hold**:
        *   **minimum_payment**: `3000 INR`
        *   **hold_duration**: `2 days`
        *   **requirement**: The remainder of the full rent must be paid within the 2-day hold period.
    *   **tier_2_hold (Worst Case)**:
        *   **minimum_payment**: `2000 INR`
        *   **hold_duration**: `1 day`
        *   **requirement**: The remainder of the full rent must be paid within the 1-day hold period.
    *   **sales_discretion_rule**: Any advance payment amount between the `2000 INR` minimum and the full rent amount is subject to negotiation and approval by the `Sales` role.

### Communication & Notifications
*   **delivery_method**: `'whatsapp'`
*   **whatsapp_templates**:
    *   **bill_notification**: `'monthly_bill'`
    *   **payment_reminder**: `'payment_reminder'`
    *   **payment_confirmation**: `'payment_confirmation'`