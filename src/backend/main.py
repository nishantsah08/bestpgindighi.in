from fastapi import FastAPI
from . import database
from .auth import router as auth_router

database.create_db_and_tables()

app = FastAPI()

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI on Cloud Run!"}
