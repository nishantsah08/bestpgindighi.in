# Public Website Deployment Guide

This document outlines the standard operating procedure for deploying the public-facing website to both the development and production environments using the provided shell scripts.

## 1. Environment Overview

The project uses two distinct Firebase Hosting sites:

-   **Development:** A staging environment for testing and review.
    -   **Site ID:** `fir-bestpg-development-public`
    -   **URL:** `https://fir-bestpg-development-public.web.app`
-   **Production:** The live, public-facing website.
    -   **Site ID:** `fir-bestpg-production-public`
    -   **URL:** `https://www.bestpgindighi.in`

## 2. Deployment Scripts

All deployments should be performed using the scripts located in the project's root directory.

### 2.1. Deploying to Development

To deploy any changes to the development environment for review, run the following command from the project root:

```bash
bash deploy-development.sh
```

This script will immediately deploy the contents of the `src/public_website` directory to the development URL.

### 2.2. Deploying to Production

Deploying to the live production website is a protected and automated action.

1.  **Prerequisite:** Ensure all changes have been tested and approved on the development environment.
2.  Run the following command from the project root:

    ```bash
    bash deploy-production.sh
    ```
3.  You will be prompted to enter the secure deployment password.
4.  If the password is correct, the script will automatically deploy the website and then ping Google to inform it that the sitemap has been updated, prompting a re-crawl. Manual submission via Google Search Console is no longer required for routine updates.
