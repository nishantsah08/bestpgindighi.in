from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from ..database_base import Base

class CallLog(Base):
    __tablename__ = "call_logs"

    id = Column(Integer, primary_key=True, index=True)
    caller_role = Column(String, index=True)
    customer_number = Column(String)
    duration_seconds = Column(Integer)
    recording_url = Column(String)
    transcription_status = Column(String, default="PENDING")
    transcript = Column(String, nullable=True)
    status = Column(String, default="UPLOADED")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    contact_id = Column(Integer, ForeignKey("contacts.id"))
    contact = relationship("Contact")
