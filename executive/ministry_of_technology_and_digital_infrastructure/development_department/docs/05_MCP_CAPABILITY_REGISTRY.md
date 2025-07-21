# MCP Capability Registry

**Version:** 1.0
**Date:** 2025-07-22

## 1. Purpose

This document is the central, technical registry for all MCP capabilities exposed by the system's backend servers. It serves as the API documentation for all client applications (Mobile Apps, Internal Portal).

## 2. Ministry of Finance Server

- **`getPendingRentReport`**: Returns a list of tenants with unpaid rent for the current cycle.
- **`getTotalCashAtHand`**: Returns the sum of all cash and bank account balances.
- **`getProjectedRevenueNextMonth`**: Returns an estimated total revenue for the next calendar month based on active tenants.
- **`recordManualRevenue`**: Records a rent payment received manually.
- **`processExpense`**: Initiates the conversational workflow to file an expense from WhatsApp.

## 3. Ministry of Growth & Commerce Server

- **`getComplianceStatusReport`**: Returns a list of tenants with pending compliance items.
- **`snoozeComplianceAlert`**: Marks a specific compliance alert for a tenant as snoozed for a given period.
- **`getLeadFunnelReport`**: Returns key lead and conversion metrics for the last 10, 30, and 60 days.
- **`generateGBLReviewLink`**: Generates the unique URL for leaving a Google Business Listing review.

## 4. Ministry of Property & Tenant Welfare Server

- **`getCustomerComplaintsReport`**: Returns a list of recent, unresolved customer complaints.
- **`snoozeComplaint`**: Marks a specific complaint as snoozed for a given period.

## 5. Vendor Management Server

- **`createVendor`**: Creates a new vendor profile.
- **`getVendor`**: Retrieves the profile and activity log for a specific vendor.
- **`updateVendor`**: Edits the details of a vendor profile.
- **`addLogToVendor`**: Adds a new text-based log entry to a vendor's profile.
- **`uploadFileToVendor`**: Uploads a file (e.g., invoice) and associates it with a vendor's profile.