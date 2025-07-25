from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .auth.models import Base  # Import the Base

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
