from sqlalchemy.orm import Session
from . import models, schemas
from ..system_counters import service as counter_service

def get_contact_by_phone_number(db: Session, phone_number: str):
    return db.query(models.Contact).filter(models.Contact.phone_number == phone_number).first()

def create_contact(db: Session, contact: schemas.ContactCreate):
    next_id = counter_service.get_next_svh_id(db)
    svh_id = f"SVH-{next_id}"
    contact_data = contact.dict()
    del contact_data["svh_id"]
    db_contact = models.Contact(**contact_data, svh_id=svh_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()

def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, contact: schemas.ContactCreate):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact:
        for key, value in contact.dict().items():
            setattr(db_contact, key, value)
        db.commit()
        db.refresh(db_contact)
    return db_contact
