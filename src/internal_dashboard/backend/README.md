# Finance/Properties API (FastAPI + Firestore)

## Run locally
```
cd src/internal_dashboard/backend
pip install -r requirements.txt
export ALLOWED_ORIGINS=*
# Optional if using GCP ADC locally:
# export FIRESTORE_PROJECT_ID=grounded-pivot-467812-f4
uvicorn app.main:app --port 8080
```

## Deploy to Cloud Run
```
PROJECT_ID=grounded-pivot-467812-f4
REGION=asia-south1
SERVICE=finance-api

cd src/internal_dashboard/backend
gcloud builds submit --tag asia-south1-docker.pkg.dev/$PROJECT_ID/apps/$SERVICE:latest

gcloud run deploy $SERVICE \
  --image=asia-south1-docker.pkg.dev/$PROJECT_ID/apps/$SERVICE:latest \
  --platform=managed \
  --region=$REGION \
  --allow-unauthenticated \
  --set-env-vars=ALLOWED_ORIGINS=https://internal.bestpgindighi.in

# Get URL
gcloud run services describe $SERVICE --region=$REGION --format='value(status.url)'
```

## Endpoints
- GET `/v1/health`
- Properties: `POST /v1/properties`, `GET /v1/properties`, `GET /v1/properties/{id}`, `PATCH /v1/properties/{id}`, `DELETE /v1/properties/{id}`
- Units: `POST /v1/properties/{pid}/units`, `GET /v1/properties/{pid}/units`, `PATCH /v1/properties/{pid}/units/{uid}`, `DELETE /v1/properties/{pid}/units/{uid}`

Auth: If `API_TOKEN` is set, requests must send `Authorization: Bearer <token>`.

