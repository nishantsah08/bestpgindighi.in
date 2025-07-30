from pydantic import BaseModel
from datetime import datetime

class CallLogBase(BaseModel):
    caller_role: str
    customer_number: str
    duration_seconds: int
    contact_id: int

class CallLogCreate(CallLogBase):
    pass

class CallLog(CallLogBase):
    id: int
    recording_url: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
