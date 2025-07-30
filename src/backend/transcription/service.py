from sqlalchemy.orm import Session
from ..calls import models
from datetime import datetime

# Placeholder functions for actual transcription services
def _transcribe_with_google(audio_url: str) -> str:
    return "This is a transcript from Google."

def _transcribe_with_azure(audio_url: str) -> str:
    return "This is a transcript from Azure."

def _transcribe_with_deepgram(audio_url: str) -> str:
    return "This is a transcript from Deepgram."

def get_google_usage(db: Session) -> int:
    # In a real application, you would query the api_usage_logs table here.
    return 0

def get_azure_usage(db: Session) -> int:
    # In a real application, you would query the api_usage_logs table here.
    return 0

def transcribe_audio(db: Session, call_log: models.CallLog) -> str:
    # 1. Check Google Free Tier
    if get_google_usage(db) < 60:
        # update_google_usage(db, call_log.duration_seconds)
        transcript = _transcribe_with_google(call_log.recording_url)
    # 2. Check Azure Free Tier
    elif get_azure_usage(db) < 300:
        # update_azure_usage(db, call_log.duration_seconds)
        transcript = _transcribe_with_azure(call_log.recording_url)
    # 3. Fallback to Deepgram
    else:
        transcript = _transcribe_with_deepgram(call_log.recording_url)

    call_log.transcript = transcript
    call_log.transcription_status = "COMPLETED"
    db.commit()
    return transcript