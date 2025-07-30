from sqlalchemy.orm import Session
from . import models, schemas
from ..contacts import service as contact_service, schemas as contact_schemas

def create_call_log(db: Session, call_log: schemas.CallLogCreate, recording_url: str):
    contact = contact_service.get_contact_by_phone_number(db, phone_number=call_log.customer_number)
    if not contact:
        contact = contact_service.create_contact(db, contact=contact_schemas.ContactCreate(phone_number=call_log.customer_number, status="New Lead"))

    call_log_data = call_log.dict()
    del call_log_data["contact_id"]
    db_call_log = models.CallLog(**call_log_data, recording_url=recording_url, status="UPLOADED", contact_id=contact.id)
    db.add(db_call_log)
    db.commit()
    db.refresh(db_call_log)
    return db_call_log

def get_call_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CallLog).offset(skip).limit(limit).all()

def get_call_log(db: Session, call_id: int):
    return db.query(models.CallLog).filter(models.CallLog.id == call_id).first()
