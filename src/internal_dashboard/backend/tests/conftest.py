import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from cabinet_secretary_api.main import app, get_db
from cabinet_secretary_api.database import Base

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture to provide a test database session for direct queries in tests
@pytest.fixture(name="test_db_session")
def test_db_session_fixture():
    try:
        db = SessionTesting()
        yield db
    finally:
        db.close()

# Fixture to override the get_db dependency for the FastAPI app during tests
@pytest.fixture(name="override_get_db", autouse=True)
def override_get_db_fixture(test_db_session):
    app.dependency_overrides[get_db] = lambda: test_db_session
    yield
    app.dependency_overrides.pop(get_db)

@pytest.fixture(name="setup_test_db")
def setup_test_db_fixture():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
