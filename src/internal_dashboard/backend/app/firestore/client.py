from google.cloud import firestore  # type: ignore
from ..config import get_settings


def get_client() -> firestore.Client:
    settings = get_settings()
    if settings.project_id:
        return firestore.Client(project=settings.project_id)
    return firestore.Client()

