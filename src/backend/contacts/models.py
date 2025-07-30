from sqlalchemy import Column, Integer, String, DateTime, func
from ..database_base import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    phone_number = Column(String, unique=True, index=True)
    svh_id = Column(String, unique=True, index=True)
    status = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
