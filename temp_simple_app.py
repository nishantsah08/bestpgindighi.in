from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def read_root():
    return {"message": "Hello from simple FastAPI!"}
