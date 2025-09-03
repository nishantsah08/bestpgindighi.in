from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .api.v1.properties import router as properties_router


settings = get_settings()

app = FastAPI(title="Finance API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins or ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)


@app.get("/v1/health")
def health():
    return {"ok": True}


app.include_router(properties_router)

