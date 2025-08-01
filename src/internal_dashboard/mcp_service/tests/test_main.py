from fastapi.testclient import TestClient
from cabinet_secretary_mcp_service.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Cabinet Secretary MCP Service is running"}

def test_mcp_send():
    message_payload = {
        "sender_id": "cabinet_secretary_ai",
        "recipient_id": "finance_ministry_ai",
        "message_type": "query_budget",
        "payload": {"year": 2025, "department": "education"}
    }
    response = client.post("/mcp_send", json=message_payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "MCP message simulated as sent"}

def test_mcp_receive():
    message_payload = {
        "sender_id": "finance_ministry_ai",
        "recipient_id": "cabinet_secretary_ai",
        "message_type": "budget_report",
        "payload": {"status": "approved", "amount": 1000000}
    }
    response = client.post("/mcp_receive", json=message_payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "MCP message simulated as received"}
