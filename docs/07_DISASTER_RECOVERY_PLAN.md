# 07 - Disaster Recovery Plan

This document outlines the procedures for recovering from two primary types of catastrophic failure: a database failure and a full infrastructure failure.

---

## 1. Database Disaster Recovery

This plan is to be executed in the event of significant data corruption or loss within the primary Supabase database.

### Phase 1: Manual Restore (CEO)

The decision to restore the database is a CEO-level action that must be performed manually to prevent accidental data loss. The system is intentionally designed so that this action **cannot** be triggered from within the Internal System Portal.

1.  **Declare a Data Emergency:** The CEO makes the decision to restore from a backup.
2.  **Log into Supabase:** Navigate to `https://supabase.com/` and log into the project.
3.  **Initiate Restore:** Navigate to the **Database -> Backups** section. Select the most recent stable backup and click the **Restore** button. Follow the on-screen prompts to complete the restore process.

### Phase 2: Automated Re-Sync (CEO, via Internal Portal)

After Supabase confirms the restore is complete, the CEO must trigger the automated re-synchronization playbook from within our own portal.

1.  **Navigate to Recovery Page:** Log into the Internal System Portal and navigate to `⚙️ Ministry of Technology -> Disaster Recovery`.
2.  **Initiate Re-Sync:** Click the prominent **[Re-Sync System with Restored Database]** button.
3.  **First Confirmation:** A warning dialog will appear explaining the action. The CEO must type the word `PROCEED` into a text box to enable the final confirmation button.
4.  **Second Confirmation:** After typing `PROCEED`, a second, final confirmation button **[Yes, I am sure - Re-Sync Now]** will become active. The CEO must click this button.
5.  **Monitor Progress:** The portal will then trigger the underlying GitHub Actions workflow and display its real-time progress. The workflow will automatically restart all application services and run a suite of data integrity checks.

---

## 2. Full Infrastructure Disaster Recovery

This plan is to be executed in the rare event of a total Google Cloud Platform regional failure.

### Phase 1: Manual Failover Decision (CEO)

1.  **Declare a Regional Disaster:** The CEO makes the decision to failover to a secondary region.
2.  **Edit Configuration:** The CEO will edit a single line in the `terraform/gcp.tf` file in the GitHub repository, changing the `region` variable from the failed region to the new, healthy region.

### Phase 2: Automated Redeployment (System)

1.  **Commit & Push:** The CEO commits and pushes the one-line change to the `main` branch.
2.  **CI/CD Trigger:** This push automatically triggers the main CI/CD pipeline.
3.  **Automated Redeployment:** The pipeline will detect the region change and automatically execute `terraform apply`. This will build the entire application infrastructure (Firebase Hosting, Cloud Run services) from scratch in the new region, deploy the latest application code, and automatically update all DNS records to point to the new infrastructure.