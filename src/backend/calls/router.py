from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List

from . import service, schemas, models
from .. import utils
from ..database import get_db
from ..transcription import router as transcription_router

router = APIRouter()

@router.post("/upload", response_model=schemas.CallLog)
async def upload_call_recording(
    caller_role: str = Form(...),
    customer_number: str = Form(...),
    duration_seconds: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    normalized_phone_number = utils.normalize_phone_number(customer_number)
    # In a real application, you would upload the file to a cloud storage
    # and get a URL. For this example, we'll just use a placeholder.
    recording_url = f"/uploads/{file.filename}"

    call_log_data = schemas.CallLogCreate(
        caller_role=caller_role,
        customer_number=normalized_phone_number,
        duration_seconds=duration_seconds,
        contact_id=0  # This will be updated in the service
    )
    call_log = service.create_call_log(db=db, call_log=call_log_data, recording_url=recording_url)

    return call_log

@router.get("/", response_model=List[schemas.CallLog])
def read_call_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_call_logs(db=db, skip=skip, limit=limit)
