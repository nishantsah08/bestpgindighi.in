from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from cabinet_secretary_api.main import app
from cabinet_secretary_api.database import ChatMessage

# Create a TestClient with the lifespan context
client = TestClient(app)

def test_health_check(setup_test_db):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Cabinet Secretary API is running"}

def test_chat_endpoint(setup_test_db, test_db_session: Session):
    response = client.post("/chat", json={
        "text": "Hello, FastAPI!"
    })
    assert response.status_code == 200
    assert response.json() == {"response": "AI received: Hello, FastAPI!"}

    # Verify message is saved in DB using the fixture-provided session
    messages = test_db_session.query(ChatMessage).all()
    assert len(messages) == 2 # User message and AI message
    assert messages[0].sender == "user"
    assert messages[0].text == "Hello, FastAPI!"
    assert messages[1].sender == "ai"
    assert messages[1].text == "AI received: Hello, FastAPI!"

def test_chat_endpoint_empty_message(setup_test_db):
    response = client.post("/chat", json={
        "text": ""
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Message cannot be empty"}
