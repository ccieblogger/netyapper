import os
import httpx
from typing import Any, Dict

class LLMClient:
    """
    Abstract base class for LLM clients.
    """
    def query(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError("LLMClient subclasses must implement query()")

class OllamaLLMClient(LLMClient):
    """
    LLM client for local Ollama server.
    """
    def __init__(self, api_url: str = None, model: str = "llama3:latest"):
        self.api_url = api_url or os.getenv("OLLAMA_API_URL", "http://localhost:11434")
        self.model = model

    def query(self, prompt: str, **kwargs) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt
        }
        try:
            response = httpx.post(f"{self.api_url}/api/generate", json=payload, timeout=30)
            response.raise_for_status()
            # Ollama returns streaming JSON objects, one per line. Collect all 'response' fields and join them.
            lines = response.text.strip().splitlines()
            import json
            contents = []
            for line in lines:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    if "response" in data:
                        contents.append(data["response"])
                except Exception:
                    continue
            return "".join(contents).strip()
        except Exception as e:
            return f"[OllamaLLMClient Error] {e}"

# Placeholder for future OpenAI adapter
class OpenAILLMClient(LLMClient):
    def query(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError("OpenAI adapter not implemented for local-only development.")
