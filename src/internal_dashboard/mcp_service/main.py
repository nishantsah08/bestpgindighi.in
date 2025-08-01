from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Dict, Any

app = FastAPI()

class MCPMessage(BaseModel):
    sender_id: str
    recipient_id: str
    message_type: str
    payload: Dict[str, Any]

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Cabinet Secretary MCP Service is running"}

@app.post("/mcp_send")
async def mcp_send(message: MCPMessage):
    """
    Simulates sending an MCP message to another Ministry AI.
    In a real scenario, this would involve actual network communication.
    """
    print(f"[MCP Send] Sending message from {message.sender_id} to {message.recipient_id} of type {message.message_type} with payload: {message.payload}")
    # Here, you would typically implement the logic to forward the message
    # to the appropriate recipient based on recipient_id and message_type.
    # For now, we just acknowledge receipt.
    return {"status": "success", "message": "MCP message simulated as sent"}

@app.post("/mcp_receive")
async def mcp_receive(message: MCPMessage):
    """
    Simulates receiving an MCP message from another Ministry AI.
    """
    print(f"[MCP Receive] Received message from {message.sender_id} for {message.recipient_id} of type {message.message_type} with payload: {message.payload}")
    # Here, you would typically process the incoming message based on its type and payload.
    # For now, we just acknowledge receipt.
    return {"status": "success", "message": "MCP message simulated as received"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001) # Using a different port for MCP service