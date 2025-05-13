docker exec netyapper-ollama-1 ollama show llama3:latest

### Prompt ollama directly
curl -X POST http://localhost:11434/api/generate -H 'Content-Type: application/json' -d '{"model": "llama3:latest", "prompt": "Hello, how are you?", "stream": false}'