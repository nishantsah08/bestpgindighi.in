# Website Deployment Guide

This document outlines the standard operating procedure for deploying the public-facing website to Firebase Hosting.

## 1. Prerequisites

- Firebase CLI must be installed and authenticated.
- The user must have appropriate permissions for the Firebase project.

## 2. Deployment Process

Deployment is a two-step process: deploying the files and implementing the necessary redirects.

### Step 2.1: Deploying Files

1.  Navigate to the project's root directory.
2.  Run the following command:
    ```bash
    firebase deploy --only hosting
    ```
3.  This command will upload the contents of the `website/` directory (or the configured public directory in `firebase.json`) to Firebase Hosting.

### Step 2.2: Implementing Redirects

To preserve SEO authority from the previous website, the following 301 redirects must be configured in the `firebase.json` file.

```json
{
  "hosting": {
    "redirects": [
      {
        "source": "/index.html",
        "destination": "/",
        "type": 301
      },
      {
        "source": "/facilities.html",
        "destination": "/rooms-and-pricing.html",
        "type": 301
      },
      {
        "source": "/contact.html",
        "destination": "/location-and-contact.html",
        "type": 301
      }
    ]
  }
}
```

## 3. Post-Deployment: Sitemap Submission

After a successful deployment, the new sitemap must be submitted to Google to ensure proper indexing of the new site structure.

1.  Log in to the Google Search Console for the `bestpgindighi.in` property.
2.  Navigate to the "Sitemaps" section.
3.  Under "Add a new sitemap," enter the full URL for the new sitemap:
    `https://www.bestpgindighi.in/sitemap.xml`
4.  Click **Submit**.

This is a one-time action required only after the initial deployment of the new site structure.