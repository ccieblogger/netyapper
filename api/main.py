from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.llm_client import OllamaLLMClient
import os
from mcp_clients.netbox_mcp_client import MockNetBoxMCPClient
from schemas.netbox import DeviceInfoRequest, InterfaceIPRequest

app = FastAPI()

ollama_client = OllamaLLMClient()
mock_netbox = MockNetBoxMCPClient()

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
async def dispatch(request: Request):
    data = await request.json()
    action = data.get("action")
    params = data.get("params", {})
    if not action:
        return JSONResponse({"error": "Missing action"}, status_code=400)
    # Example dispatcher logic for mock NetBox MCP
    if action == "get_device_info":
        device = params.get("device")
        if not device:
            return JSONResponse({"error": "Missing device parameter"}, status_code=400)
        result = mock_netbox.get_device_info(device)
        return result
    elif action == "get_interface_ip":
        device = params.get("device")
        interface = params.get("interface")
        if not device or not interface:
            return JSONResponse({"error": "Missing device or interface parameter"}, status_code=400)
        result = mock_netbox.get_interface_ip(device, interface)
        return result
    else:
        return JSONResponse({"error": f"Unknown action: {action}"}, status_code=400)

@app.post("/parse-intent")
async def parse_intent(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    if not prompt:
        return JSONResponse({"error": "Missing prompt"}, status_code=400)
    # For now, just echo the LLM response; intent parsing logic can be added later
    response = ollama_client.query(prompt)
    return {"intent": response}
