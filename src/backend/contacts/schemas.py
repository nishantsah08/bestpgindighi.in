from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ContactBase(BaseModel):
    phone_number: str
    name: Optional[str] = None
    status: str
    svh_id: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
