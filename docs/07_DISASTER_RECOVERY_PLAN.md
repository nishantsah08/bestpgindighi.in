# 07 - Disaster Recovery Plan

This document outlines the procedures for recovering from catastrophic data loss, designed with the core principles of **data integrity and cost control** over immediate, high-availability uptime. A downtime of up to 24 hours is considered acceptable in a disaster scenario.

---

## 1. Database Recovery Strategy (Firestore)

Our strategy uses two different methods to protect against the two most likely failure scenarios in the most cost-effective way.

### Scenario A: Accidental Data Loss or Corruption (Common)

This plan covers the most common type of data emergency, such as a developer error or a software bug deleting or corrupting data.

*   **Mechanism:** Firestore **Point-in-Time Recovery (PITR)**.
*   **Description:** PITR is enabled on our Firestore database. This feature automatically creates continuous backups, allowing us to restore the database to any single minute within the last 7 days.
*   **Recovery Process (Manual):**
    1.  **Declare a Data Emergency:** The CEO makes the decision to restore.
    2.  **Log into Google Cloud Console:** Navigate to the Firestore section.
    3.  **Initiate Restore:** Use the Point-in-Time Recovery feature to select a precise timestamp before the data was corrupted. The data will be restored to a new set of collections.
    4.  **Data Migration:** An authorized developer will then carefully migrate the necessary data from the restored collections back into the live collections.
*   **Expected Downtime:** 1-2 hours.
*   **Cost:** Very low. We only pay for the storage of the continuous backup data.

### Scenario B: Full Regional Failure (Rare)

This plan covers the rare but possible event that the entire Google Cloud region hosting our primary database becomes unavailable.

*   **Mechanism:** Daily Automated Backups to a separate region.
*   **Description:** Every 24 hours, an automated process exports a full snapshot of the entire Firestore database to a Google Cloud Storage bucket. This bucket is located in a different, low-cost geographical region.
*   **Recovery Process (Manual):**
    1.  **Declare a Regional Disaster:** The CEO confirms the outage and approves the manual recovery process.
    2.  **Create New Firestore Instance:** A developer will manually provision a new Firestore database in a different, healthy region.
    3.  **Import from Backup:** The developer will initiate an import process, loading the data from the most recent daily backup file from the Cloud Storage bucket into the new Firestore instance.
    4.  **Redeploy Backend:** The backend Cloud Functions will be redeployed to the new region, configured to connect to the new Firestore database.
*   **Expected Downtime:** 4-8 hours, well within the 24-hour tolerance.
*   **Cost:** Extremely low. This is the most cost-effective way to insure against a regional failure, as we only pay for the storage of the backup files.

---

## 2. Application Infrastructure Recovery

*   **Backend (Cloud Functions):** The backend is stateless. In a regional failure, it is simply redeployed to the new, healthy region alongside the database as described above.
*   **Frontend (Firebase Hosting):** No action is required. Firebase Hosting is a global service and is not tied to a single region. It will remain available.
