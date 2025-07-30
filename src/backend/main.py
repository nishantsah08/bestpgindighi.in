#!/usr/bin/env python3

import logging
from fastapi import FastAPI
from . import database
from .auth import router as auth_router
from .logging import router as logging_router
from .calls import router as calls_router
from .contacts import router as contacts_router
from .transcription import router as transcription_router

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

database.create_db_and_tables()

app = FastAPI()

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(logging_router.router, prefix="/log", tags=["log"])
app.include_router(calls_router.router, prefix="/calls", tags=["calls"])
app.include_router(contacts_router.router, prefix="/contacts", tags=["contacts"])
app.include_router(transcription_router.router, prefix="/transcription", tags=["transcription"])

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Hello from FastAPI on Cloud Run!"} # Added comment to trigger CI/CD

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
