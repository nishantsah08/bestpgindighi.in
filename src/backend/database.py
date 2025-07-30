from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database_base import Base
from .system_counters.models import Base as SystemCounterBase

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for simplicity

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
    SystemCounterBase.metadata.create_all(bind=engine)
