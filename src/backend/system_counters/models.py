from sqlalchemy import Column, Integer, String
from ..database_base import Base

class SystemCounter(Base):
    __tablename__ = "system_counters"

    counter_name = Column(String, primary_key=True, index=True)
    current_value = Column(Integer, default=0)
