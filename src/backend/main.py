from fastapi import FastAPI
from .auth import router as auth_router, models as auth_models
from database import engine

auth_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Best PG in Dighi API"}
