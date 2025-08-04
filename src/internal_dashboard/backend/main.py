import os
import uuid
from fastapi import FastAPI
from google.cloud import firestore

app = FastAPI()

# --- Database Connection ---
db = None
if os.getenv('FIRESTORE_EMULATOR_HOST'):
    # Connect to the local emulator
    db = firestore.Client(
        project="local-dev" # Use a dummy project ID for the emulator
    )
else:
    # Connect to the real Firestore database in production
    db = firestore.Client()
# --- End Database Connection ---


@app.get("/api/test_db")
async def test_db():
    """
    Performs a simple write and read to the database to confirm connection.
    """
    try:
        doc_id = str(uuid.uuid4())
        doc_ref = db.collection(u'walking_skeleton').document(doc_id)
        
        # Write to DB
        doc_ref.set({
            u'message': u'Hello from the backend!',
            u'timestamp': firestore.SERVER_TIMESTAMP
        })

        # Read from DB
        doc = doc_ref.get()
        if doc.exists:
            return {"status": "ok", "data": doc.to_dict()}
        else:
            return {"status": "error", "message": "Document not found after write."}

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/health")
def read_root():
    return {"status": "ok"}