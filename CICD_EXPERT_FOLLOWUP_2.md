# Second Follow-up Request for CI/CD Expert Review

**Date:** Wednesday, August 6, 2025

## 1. Summary

This is a second follow-up to the ongoing CI/CD issue. The workflow is still failing with the `NOT_FOUND` error when trying to describe the Artifact Registry repository, despite implementing the expert's latest recommendations and confirming that the `gcloud` CLI is now authenticated.

## 2. Implemented Changes

Based on the expert's advice, the following changes were made to the `.github/workflows/deploy_to_cloud_run.yml` file:

1.  **`export_default_credentials: true`:** This was added to the `google-github-actions/auth` step to ensure that Application Default Credentials (ADC) were exported to the shell.
2.  **Separated GAR and Cloud Run Regions:** The workflow was updated to use separate environment variables for the GAR and Cloud Run locations (`GAR_LOCATION` and `RUN_REGION`).

## 3. The Contradictory Results

The latest workflow run has produced a deeply contradictory set of results:

1.  **Authentication Success:** The "Who am I?" step now correctly shows that the service account is active and that ADC is working:
    ```
    Credentialed Accounts
    ACTIVE  ACCOUNT
    *       firebase-adminsdk-fbsvc@***.iam.gserviceaccount.com
    ```
2.  **`gcloud` Failure:** The very next step, `Describe GAR repo`, still fails with the `NOT_FOUND` error.

This is the core of the problem. The runner is authenticated, but `gcloud` is behaving as if it is not.

## 4. The Unanswered Question

Why is the `gcloud artifacts repositories describe` command failing with a `NOT_FOUND` error when it is being run in a confirmed authenticated environment?

## 5. Request to the Expert

Could you please review the latest logs and workflow file to help diagnose this contradictory behavior? Is there a known issue or a subtle interaction between the GitHub Actions runner, the `google-github-actions/auth` action, and the `gcloud` CLI that could be causing this?

**Latest Workflow File:**

```yaml
name: Deploy to Cloud Run

on:
  push:
    branches: [walking-skeleton]

env:
  PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}   # fir-bestpg
  GAR_LOCATION: asia            # or asia-south1 — must match the repo
  RUN_REGION: asia-south1       # Cloud Run region
  SERVICE_NAME: api-backend
  REPO: cloud-run

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Google Auth
        uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}
          project_id: ${{ env.PROJECT_ID }}
          export_default_credentials: true  # <-- critical

      - name: Set up gcloud
        uses: google-github-actions/setup-gcloud@v2
        with:
          project_id: ${{ env.PROJECT_ID }}

      - name: Who am I?
        run: |
          gcloud auth list --filter=status:ACTIVE
          gcloud config get-value project
          # Also verify ADC is usable:
          gcloud auth application-default print-access-token | head -c 20; echo

      - name: Describe GAR repo
        run: |
          gcloud artifacts repositories describe ${{ env.REPO }} \
            --location=${{ env.GAR_LOCATION }} \
            --project=${{ env.PROJECT_ID }}

      - name: Configure Docker auth for Artifact Registry
        run: gcloud auth configure-docker ${{ env.GAR_LOCATION }}-docker.pkg.dev --quiet

      - name: Docker login (defensive)
        run: |
          gcloud auth print-access-token | \
            docker login -u oauth2accesstoken --password-stdin \
            https://${{ env.GAR_LOCATION }}-docker.pkg.dev

      - id: vars
        name: Compute image URI
        run: |
          echo "image_uri=${{ env.GAR_LOCATION }}-docker.pkg.dev/${{ env.PROJECT_ID }}/${{ env.REPO }}/${{ env.SERVICE_NAME }}:${{ github.sha }}" >> $GITHUB_OUTPUT

      - name: Build
        run: docker build -t ${{ steps.vars.outputs.image_uri }} .

      - name: Push
        run: docker push ${{ steps.vars.outputs.image_uri }}

      - name: Deploy to Cloud Run
        uses: google-github-actions/deploy-cloudrun@v2
        with:
          service: ${{ env.SERVICE_NAME }}
          region: ${{ env.RUN_REGION }}        # <-- NOT "asia"
          image: ${{ steps.vars.outputs.image_uri }}
          allow_unauthenticated: true
```