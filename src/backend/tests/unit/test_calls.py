import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.backend.main import app
from src.backend.database import Base, get_db
from src.backend.utils import normalize_phone_number

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_calls.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_upload_call_recording(test_db):
    with open("test_audio.wav", "wb") as f:
        f.write(b"test audio data")

    response = client.post(
        "/calls/upload",
        data={
            "caller_role": "Sales",
            "customer_number": "7588498834",
            "duration_seconds": 60,
        },
        files={"file": ("test_audio.wav", open("test_audio.wav", "rb"), "audio/wav")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["caller_role"] == "Sales"
    assert data["customer_number"] == "+917588498834"
    assert data["duration_seconds"] == 60
    assert "/uploads/test_audio.wav" in data["recording_url"]
    assert data["contact_id"] is not None

def test_read_call_logs(test_db):
    response = client.get("/calls/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_normalize_phone_number():
    # Indian numbers
    assert normalize_phone_number("7588498834") == "+917588498834"
    assert normalize_phone_number("+917588498834") == "+917588498834"
    assert normalize_phone_number("07588498834") == "+917588498834"
    assert normalize_phone_number(" 758 849 8834 ") == "+917588498834"

    # International numbers
    assert normalize_phone_number("+14155552671") == "+14155552671"
    assert normalize_phone_number("1 (415) 555-2671", default_region="US") == "+14155552671"

    # Invalid numbers
    assert normalize_phone_number("12345") is None
