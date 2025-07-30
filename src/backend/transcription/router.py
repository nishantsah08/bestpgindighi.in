from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import service
from ..database import get_db
from ..calls import service as call_service

router = APIRouter()

@router.post("/create/{call_id}", response_model=str)
def create_transcription(call_id: int, db: Session = Depends(get_db)):
    db_call_log = call_service.get_call_log(db, call_id=call_id)
    if not db_call_log:
        raise HTTPException(status_code=404, detail="Call log not found")

    return service.transcribe_audio(db=db, call_log=db_call_log)
