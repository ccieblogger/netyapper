from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.llm_client import OllamaLLMClient
import os

app = FastAPI()

ollama_client = OllamaLLMClient()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    if not prompt:
        return JSONResponse({"error": "Missing prompt"}, status_code=400)
    response = ollama_client.query(prompt)
    return {"response": response}

@app.post("/dispatch")
def dispatch():
    # Placeholder for dispatch endpoint
    return JSONResponse({"message": "Dispatch endpoint not implemented yet."})

@app.post("/parse-intent")
async def parse_intent(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    if not prompt:
        return JSONResponse({"error": "Missing prompt"}, status_code=400)
    # For now, just echo the LLM response; intent parsing logic can be added later
    response = ollama_client.query(prompt)
    return {"intent": response}
