import os
import sys
import uuid
import logging
from fastapi import FastAPI
from google.cloud import firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
print("--- SCRIPT START ---")
logging.info("Application starting up...")
print(f"Python version: {sys.version}")
print(f"PYTHONPATH: {os.getenv('PYTHONPATH')}")
print(f"Current working directory: {os.getcwd()}")

app = FastAPI()
print("FastAPI app instantiated.")

# --- Database Connection ---
db = None
print("Attempting to connect to Firestore...")
logging.info("Attempting to connect to Firestore...")
try:
    if os.getenv('FIRESTORE_EMULATOR_HOST'):
        # Connect to the local emulator
        print("Connecting to Firestore emulator...")
        logging.info("Connecting to Firestore emulator...")
        db = firestore.Client(
            project="local-dev" # Use a dummy project ID for the emulator
        )
    else:
        # Connect to the real Firestore database in production
        print("Connecting to production Firestore...")
        logging.info("Connecting to production Firestore...")
        db = firestore.Client()
    print("Firestore connection successful.")
    logging.info("Firestore connection successful.")
except Exception as e:
    print(f"Error connecting to Firestore: {e}")
    logging.error(f"Error connecting to Firestore: {e}")
# --- End Database Connection ---


@app.get("/api/test_db")
async def test_db():
    """
    Performs a simple write and read to the database to confirm connection.
    """
    print("Received request for /api/test_db")
    logging.info("Received request for /api/test_db")
    try:
        doc_id = str(uuid.uuid4())
        doc_ref = db.collection(u'walking_skeleton').document(doc_id)
        
        # Write to DB
        print(f"Writing to document: {doc_id}")
        logging.info(f"Writing to document: {doc_id}")
        doc_ref.set({
            u'message': u'Hello from the backend!',
            u'timestamp': firestore.SERVER_TIMESTAMP
        })
        print("Write successful.")
        logging.info("Write successful.")

        # Read from DB
        print("Reading from document...")
        logging.info("Reading from document...")
        doc = doc_ref.get()
        if doc.exists:
            print("Read successful.")
            logging.info("Read successful.")
            return {"status": "ok", "data": doc.to_dict()}
        else:
            print("Document not found after write.")
            logging.warning("Document not found after write.")
            return {"status": "error", "message": "Document not found after write."}

    except Exception as e:
        print(f"Error in test_db: {e}")
        logging.error(f"Error in test_db: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/api/health")
def read_root():
    print("Received request for /api/health")
    logging.info("Received request for /api/health")
    return {"status": "ok"}

@app.get("/api/test")
def test_endpoint():
    print("Received request for /api/test")
    logging.info("Received request for /api/test")
    return {"status": "ok", "message": "Backend is live!"}

print("--- SCRIPT END ---")
logging.info("Application startup complete.")
