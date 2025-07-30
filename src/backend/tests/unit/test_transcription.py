import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.backend.main import app
from src.backend.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_transcription.db"

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

@patch("src.backend.transcription.service._transcribe_with_deepgram", return_value="deepgram_transcript")
@patch("src.backend.transcription.service._transcribe_with_azure", return_value="azure_transcript")
@patch("src.backend.transcription.service._transcribe_with_google", return_value="google_transcript")
def test_transcription_waterfall(mock_google, mock_azure, mock_deepgram, test_db):
    # Create a call log first
    with open("test_audio.wav", "wb") as f:
        f.write(b"test audio data")

    response = client.post(
        "/calls/upload",
        data={
            "caller_role": "Sales",
            "customer_number": "1234567890",
            "duration_seconds": 60,
        },
        files={"file": ("test_audio.wav", open("test_audio.wav", "rb"), "audio/wav")},
    )
    assert response.status_code == 200
    call_log = response.json()

    # First call should go to Google
    response = client.post(f"/transcription/create/{call_log['id']}")
    assert response.status_code == 200
    mock_google.assert_called_once()

    # # Second call should go to Azure
    # with patch("src.backend.transcription.service.get_google_usage", return_value=61):
    #     response = client.post("/transcription/create/1")
    #     assert response.status_code == 200
    #     mock_azure.assert_called_once()

    # # Third call should go to Deepgram
    # with patch("src.backend.transcription.service.get_google_usage", return_value=61):
    #     with patch("src.backend.transcription.service.get_azure_usage", return_value=301):
    #         response = client.post("/transcription/create/1")
    #         assert response.status_code == 200
    #         mock_deepgram.assert_called_once()
