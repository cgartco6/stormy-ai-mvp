from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from backend.stormy_core import StormyCore
import uvicorn

app = FastAPI(title="Stormy V3.0")
core = StormyCore()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(req: ChatRequest):
    reply = core.get_response(req.message)
    return {"reply": reply, "mood": core.mood}

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("frontend/index.html") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
