start:
	./scripts/check_ollama.sh
	uvicorn api.main:app --reload
