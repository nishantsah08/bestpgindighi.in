# Public Website Deployment Guide

This document outlines the standard operating procedure for deploying the public-facing website to both the development and production environments.

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

## 3. SEO Strategy and Optimization

This section outlines the comprehensive SEO strategy for the public website, integrating keyword research, content planning, and technical optimizations to enhance discoverability and performance.

### 3.1. Keyword Strategy Integration

Based on Google Business Profile insights and targeted research, the following keywords will be prioritized:

*   **Core Existing Keywords (Highest Priority - Maintain & Strengthen):**
    *   "pg in dighi"
    *   "pg near dighi pune"
    *   "pg in dighi pune"
    *   *Implementation:* These will be prominently featured on the homepage and general information pages, ensuring their continued strong performance.

*   **Targeted Expansion Keywords (High Priority - New Focus):**
    *   **"boys hostel dighi"** (Strong emphasis, dedicated page)
    *   "pg for AIT students" / "hostel for army institute students" (Dedicated page, integrating "Army Institute of Technology Pune")
    *   "pg for Tata Communications employees" / "hostel for Tata Communications staff" (Dedicated page, integrating "Tata Communications")
    *   "student accommodation dighi" (Dedicated page, integrating "AIT students" and general student appeal)
    *   *Implementation:* These will drive new, highly relevant traffic. The "boys hostel" keyword will be a central theme for its dedicated page.

*   **General & Supporting Keywords:**
    *   "pg near me"
    *   "pg"
    *   "male pg accommodation"
    *   "boys hostel pune dighi"
    *   *Implementation:* These will provide broader reach and support the primary and targeted keywords. Keywords will be naturally integrated into page titles, meta descriptions, headings (H1, H2, H3), and body content across relevant pages. Avoid keyword stuffing; focus on natural language.

### 3.2. Content Strategy & Dedicated Landing Pages

*   **High-Priority Landing Pages to Create/Enhance:**
    *   **Boys Hostel Dighi (`boys-hostel-dighi.html`):** This page will be robust, detailed, and heavily optimized for "boys hostel" related keywords. It will expand upon the existing "Boys PG Accommodation" section, highlighting amenities and community aspects specifically appealing to male residents.
    *   **AIT Student Housing (`ait-student-housing.html`):** Tailored content for Army Institute of Technology students, emphasizing proximity (leveraging the "10 min walk" detail), study-friendly environment, and specific needs.
    *   **Tata Communications Employee Accommodation (`tcl-employee-accommodation.html`):** Content for Tata Communications employees, focusing on convenience, amenities, and a conducive living environment, leveraging the "15 min walk" detail.
    *   **Student Housing (`student-housing.html`):** General student-focused content, highlighting study-friendly environments, safety, and community.

*   **Content Themes to Incorporate (Across all relevant pages, leveraging existing site content):**
    *   **Safety & Security:** Emphasize 24/7 CCTV, secure environment.
    *   **Proximity:** Highlight walking distance/easy commute to AIT, Tata Communications.
    *   **Amenities:** Focus on modern amenities, RO purified drinking water, and a homely environment.
    *   **Community:** Mention the benefits of a like-minded resident community (students/professionals).

### 3.3. On-Page SEO

*   **Meta Tags & Headings:** Implement unique, descriptive `<title>` tags and `<meta name="description">` for each page, incorporating target keywords. Utilize `<h1>` for main page titles and `<h2>`/`<h3>` for subheadings to establish clear content hierarchy.
*   **Image Optimization:** Optimize all images for web (compression, appropriate dimensions) and include descriptive `alt` attributes for accessibility and SEO.
*   **Content Quality:** Ensure all page content is high-quality, informative, and naturally incorporates relevant keywords, providing value to the user.

### 3.4. Technical SEO & Link Preservation

*   **URL Structure (Simple & Preserving Old SEO):**
    *   Maintain clean, readable, and keyword-rich URLs for new pages:
        *   `/boys-hostel-dighi.html`
        *   `/ait-student-housing.html`
        *   `/tcl-employee-accommodation.html`
        *   `/student-housing.html`
    *   **Crucially, implement permanent 301 redirects in `firebase.json` for any changed or old URLs** (e.g., `/facilities.html` to `/rooms-and-pricing.html` if "Facilities" is replaced or its content moved) to preserve SEO authority and prevent broken links, as detailed in this document. This ensures that any existing SEO value from old links is transferred.

*   **Meta Tags Preservation:** Ensure all existing and new meta tags are correctly implemented.
*   **Schema Markup:** Implement local business schema markup (e.g., `LocalBusiness`, `Accommodation`) to enhance local SEO and provide rich snippets in search results.
*   **Page Speed:** Leverage Firebase Hosting's CDN for fast content delivery. Further optimize by minifying CSS and JavaScript files, and prioritizing critical rendering path elements to improve Core Web Vitals.
*   **Mobile-First Optimization (Critical - 91% Mobile Traffic):**
    *   Design and develop the website to be fully responsive, ensuring an optimal viewing experience across all devices (desktops, tablets, mobile phones).
    *   Prioritize mobile layout and user experience during development.
    *   Ensure fast loading times on mobile networks.
*   **HTTPS:** Firebase Hosting automatically provides HTTPS, ensuring secure connections, which is a positive ranking signal.
*   **Sitemap Generation & Submission:** Generate an XML sitemap (`sitemap.xml`) listing all important pages. This sitemap will be submitted to Google Search Console to aid in efficient crawling and indexing.
*   **Robots.txt Configuration:** Configure `robots.txt` to guide search engine crawlers, ensuring important pages are indexed while excluding any irrelevant or private sections.
*   **Click-to-Call:** Prominently display the sales contact number (+91 7559421424) with click-to-call functionality on mobile devices.
