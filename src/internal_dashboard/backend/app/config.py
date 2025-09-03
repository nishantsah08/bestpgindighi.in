from functools import lru_cache
from typing import List
import os


class Settings:
    def __init__(self) -> None:
        self.project_id: str | None = os.getenv("FIRESTORE_PROJECT_ID")
        self.api_token: str | None = os.getenv("API_TOKEN")
        self.allowed_origins: List[str] = [
            o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",") if o.strip()
        ]
        self.public_assets_bucket: str | None = os.getenv("PUBLIC_ASSETS_BUCKET")
        self.thumb_max_bytes: int = int(os.getenv("THUMB_MAX_BYTES", "2097152"))
        self.image_max_dim: int = int(os.getenv("IMAGE_MAX_DIM", "128"))
        self.log_correlation: bool = os.getenv("LOG_CORRELATION", "true").lower() == "true"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
