#!/bin/bash
# scripts/check_ollama.sh

if ! nc -z localhost 11434; then
  echo "Ollama server not running. Starting ollama serve..."
  nohup ollama serve > /dev/null 2>&1 &
  sleep 2
else
  echo "Ollama server is already running."
fi
