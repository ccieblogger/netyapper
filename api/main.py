from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
def chat():
    # Placeholder for chat endpoint
    return JSONResponse({"message": "Chat endpoint not implemented yet."})

@app.post("/dispatch")
def dispatch():
    # Placeholder for dispatch endpoint
    return JSONResponse({"message": "Dispatch endpoint not implemented yet."})

@app.post("/parse-intent")
def parse_intent():
    # Placeholder for intent parsing
    return JSONResponse({"message": "Parse-intent endpoint not implemented yet."})
