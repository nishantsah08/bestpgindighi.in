# System-Wide Test Plan

This document outlines the test cases for the new and updated system components.

## 1. Public Website

| Test Case ID | Component | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| WEB-01 | All Pages | Verify that the website is fully responsive and displays correctly on mobile, tablet, and desktop screens. | No visual bugs or layout issues on any device size. |
| WEB-02 | All Pages | Check all internal and external links to ensure there are no broken links (404 errors). | All links navigate to the correct destination. |
| WEB-03 | SEO | Verify that the 301 redirects from the old URLs (`/facilities.html`, `/contact.html`) correctly forward to the new pages. | Accessing old URLs automatically redirects to the new URLs. |
| WEB-04 | Contact Page | Test the embedded Google Map to ensure it loads and displays the correct location. | Map is interactive and centered on the correct business address. |

## 2. Internal System Portal (CEO)

| Test Case ID | Component | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| PORTAL-01 | Login | Verify that only the designated CEO Google account can successfully log in. | Successful login for CEO; access denied for all other accounts. |
| PORTAL-02 | GBL Tool | Test the "Generate GBL Review Link" button to ensure it produces a valid and correct URL. | A valid Google Business Listing review URL is generated. |
| PORTAL-03 | Vendor Directory | Verify that the CEO can view the list of vendors. | Vendor list displays correctly. |

## 3. Native Mobile Application Suite

### 3.1 CEO App

| Test Case ID | Component | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| CEO-APP-01 | Vendor Directory | Verify that the CEO can add, view, and edit a vendor profile. | All CRUD (Create, Read, Update, Delete) operations on vendor profiles function correctly. |
| CEO-APP-02 | Vendor Directory | Test the file upload feature by attaching a photo to a vendor profile. | The file is successfully uploaded and associated with the correct vendor. |

### 3.2 Sales App

| Test Case ID | Component | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| SALES-APP-01 | GBL Tool | Verify that the "Generate GBL Review Link" button is visible and functional for the Sales role. | Button is visible and generates a valid URL. |
| SALES-APP-02 | Role Access | Attempt to access features outside the Sales role's permissions (e.g., Vendor Directory). | Access is denied. |

### 3.3 Caretaker App

| Test Case ID | Component | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| CARE-APP-01 | Camera | Test the camera feature to ensure it captures photos and videos with the correct geotag and timestamp. | Media is captured and saved with the correct metadata. |
| CARE-APP-02 | Role Access | Attempt to access features outside the Caretaker role's permissions (e.g., GBL Tool, Vendor Directory). | Access is denied. |