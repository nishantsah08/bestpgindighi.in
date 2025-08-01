from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uvicorn
from sqlalchemy.orm import Session
from .database import SessionLocal, ChatMessage, create_db_and_tables
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import httpx
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file in the project root
load_dotenv(dotenv_path='/home/nishantsah/bestpgindighi.in/.env')

# Configuration for MCP Service
MCP_SERVICE_URL = "http://34.47.243.114:8001"

# Google Gemini API Key
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # Changed model to gemini-1.5-flash

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    create_db_and_tables()
    yield
    # Shutdown event (if any cleanup is needed)

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000", # For local development
    "http://34.47.243.114:3000", # For your deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

class MCPMessage(BaseModel):
    sender_id: str
    recipient_id: str
    message_type: str
    payload: dict

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Cabinet Secretary API is running"}

@app.post("/chat")
async def chat_endpoint(message: Message, db: Session = Depends(get_db)):
    """
    Handles chat messages, stores them in the database, and uses Google Gemini for AI response.
    Optionally sends messages to MCP service if prefixed with "mcp:".
    """
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Save user message to database
    db_user_message = ChatMessage(sender="user", text=message.text, timestamp=datetime.utcnow())
    db.add(db_user_message)
    db.commit()
    db.refresh(db_user_message)

    ai_response_text = ""

    if message.text.lower().startswith("mcp:"):
        # Extract MCP command and payload
        mcp_command = message.text[4:].strip()
        # For simplicity, let's assume a fixed recipient and message type for now
        mcp_payload = {"command": mcp_command}
        mcp_msg = MCPMessage(
            sender_id="cabinet_secretary_api",
            recipient_id="ministry_ai_placeholder", # Replace with actual recipient logic
            message_type="command",
            payload=mcp_payload
        )
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{MCP_SERVICE_URL}/mcp_send", json=mcp_msg.dict())
                response.raise_for_status() # Raise an exception for bad status codes
                mcp_response = response.json()
                ai_response_text = f"MCP Service Response: {mcp_response.get("message", "No message")}"
        except httpx.RequestError as exc:
            ai_response_text = f"Error connecting to MCP service: {exc}"
        except httpx.HTTPStatusError as exc:
            ai_response_text = f"Error from MCP service: {exc.response.status_code} - {exc.response.text}"
        except Exception as exc:
            ai_response_text = f"An unexpected error occurred with MCP: {exc}"
    else:
        # Use Google Gemini for LLM processing
        try:
            response = model.generate_content(message.text)
            ai_response_text = response.text
        except Exception as exc:
            ai_response_text = f"Error from Gemini LLM: {exc}"

    db_ai_message = ChatMessage(sender="ai", text=ai_response_text, timestamp=datetime.utcnow())
    db.add(db_ai_message)
    db.commit()
    db.refresh(db_ai_message)

    return {"response": ai_response_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)