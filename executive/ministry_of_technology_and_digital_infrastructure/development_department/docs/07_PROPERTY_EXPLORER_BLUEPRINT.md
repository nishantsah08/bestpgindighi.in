# 07 - Property Explorer Blueprint

This document outlines the detailed functionality for the "Property Explorer" feature within the Ministry of Property & Tenant Welfare.

## 1. Core Purpose

To provide a rich, visual, and interactive interface for exploring the physical hierarchy of the business's assets, from a high-level property overview down to individual beds. This tool is intended for property managers, sales staff, and executives to quickly assess occupancy and availability.

## 2. Interface Hierarchy

The Property Explorer will be a three-level, drill-down interface.

### Level 1: All Properties View ("City View")
- **Layout:** A grid of interactive cards, with one card per property.
- **Card Content:**
    - Property Photo
    - Property Name
    - Color-coded occupancy bar (percentage based)
    - Key Stats: Total Units, Total Beds, Vacant Beds.
- **Action:** Clicking a card drills down to the Single Property View.

### Level 2: Single Property View ("Building View")
- **Layout:** A 2D floor plan or stacked block diagram representing all units (rooms) in the selected property.
- **Unit Block Content:**
    - Unit Number
    - Color-coded status:
        - **Green:** Vacant
        - **Yellow:** Partially Occupied
        - **Blue:** Fully Occupied
        - **Gray:** Unavailable
- **Interactivity:**
    - Hovering over a unit shows a tooltip with details.
    - Clicking a unit drills down to the Single Unit View.

### Level 3: Single Unit View ("Room View")
- **Layout:** A simple diagram showing all beds within the selected unit.
- **Bed Content:**
    - Bed Identifier
    - Color-coded status:
        - **Green:** Vacant
        - **Blue:** Occupied
- **Interactivity:**
    - Hovering over a bed shows its identifier.
    - Clicking an occupied bed reveals a pop-up with basic tenant information.

## 3. Data Source

The Property Explorer will read data directly from the `properties`, `units`, and `beds` collections in the Firestore database, as defined in `parliament_policies/bills/21_property_data_management_bill.yaml`.
