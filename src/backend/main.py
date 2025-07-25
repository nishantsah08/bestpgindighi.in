import logging
from fastapi import FastAPI
from . import database
from .auth import router as auth_router
from .logging import router as logging_router

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

database.create_db_and_tables()

app = FastAPI()

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(logging_router.router, prefix="/log", tags=["log"])

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Hello from FastAPI on Cloud Run!"} # Added comment to trigger CI/CD
