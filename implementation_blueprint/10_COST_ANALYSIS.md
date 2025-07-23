# Chapter 10: Cost Analysis & Optimization

**Version:** 1.0
**Date:** 2025-07-23

## 10.1 Guiding Principle

All cost considerations are governed by the principle of **Commercial Prudence** as defined in Article VI of the Constitution.

## 10.2 Cloud Infrastructure Costs (GCP)

- **Compute (Google Cloud Run):** Billed per request and CPU/memory consumed during processing. Cost is expected to scale linearly with user traffic.
- **Database (Google Cloud Firestore):** Billed per read, write, and delete operation. This will be a significant cost driver. Efficient queries and caching are critical.
- **Storage (Google Cloud Storage):** Billed per GB stored. Relatively low cost, but will grow over time as more documents are uploaded.

## 10.3 Third-Party API Costs

### 10.3.1 WhatsApp Business Platform
This is a primary operational cost and must be monitored closely.

- **Utility Messages:** Approx. ₹0.13 per message. Incurred for every AI Confirmation Loop, feedback survey, and initial lead response.
- **Marketing Messages:** Approx. ₹0.88 per message. Incurred for every automated lead nurturing follow-up.
- **Optimization Strategy:** The `Autonomous_Strategy_Optimization` process is the primary mechanism for managing this cost by ensuring marketing messages are only sent when there is a high probability of ROI.

## 10.4 AI & Machine Learning Costs

- **NLU/OCR Service (Google Cloud Vision API):** Billed per 1000 images processed. This cost will be directly proportional to the number of receipts and documents uploaded.
- **Model Training (AI Platform):** A recurring, predictable cost for the weekly/monthly retraining of the Lead Scoring and Vacancy Prediction models.
- **Model Inference (Cloud Run):** The cost of running the custom models to provide real-time predictions. Billed per request.

## 10.5 Monitoring & Budgeting

- **GCP Budgets:** A hard budget will be set in the GCP console for the entire project.
- **Alerting:** Automated alerts will be configured to notify the CEO and development team if spending exceeds 50%, 75%, and 90% of the monthly budget. This is a critical control to prevent unexpected cost overruns.
