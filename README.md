# Conversational Interface for MCP-enabled Systems Using Swappable LLMs

A unified Web and CLI interface that allows users to interact with network infrastructure and third-party systems using natural language. Backed by a pluggable LLM engine and an MCP-based agent dispatcher, this project is designed for network automation, CMDB integrations, and more.

---

## 🔥 Features

* Chat-based Web and CLI interfaces
* Swappable LLM backends (OpenAI, Ollama, etc.)
* Structured intent parsing using prompt templates
* Dispatcher that routes tasks to registered MCP servers
* NetBox MCP integration (mock + real modes)
* Support for future agent integrations

---

## 📦 Tech Stack

| Layer         | Technology                             |
| ------------- | -------------------------------------- |
| Frontend      | Vue 3 + Vite + Tailwind CSS + PrimeVue |
| Backend API   | FastAPI (Python)                       |
| CLI Tool      | Python `click`, `rich`                 |
| LLM Interface | LiteLLM / custom adapter               |
| Deployment    | Docker, GitHub Actions                 |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_ORG/llm-mcp-interface.git
cd llm-mcp-interface
```

### 2. Set up Backend (FastAPI)

```bash
cd app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Set up Web Frontend

```bash
cd web
npm install
npm run dev
```

### 4. Run CLI Interface

```bash
cd cli
python query.py "What interfaces are on router R1?"
```

---

## 📁 Directory Structure

```
app/
├── api/                # FastAPI routes
├── core/               # LLM adapter, dispatcher
├── mcp_clients/        # NetBox, Cisco CLI, etc.
├── schemas/            # Pydantic models
├── templates/          # Prompt templates
├── cli/                # CLI interfaces
├── web/                # Web UI (Vue + PrimeVue)
└── main.py             # Entrypoint
```

---

## 📜 License

This project is licensed under the **GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007**:

```
Copyright (C) 2007 Free Software Foundation, Inc.
<https://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
```

For full license text, see: [https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)

---

## 🤝 Contributing

Contributions, feedback, and enhancements are welcome. Please open issues or submit PRs with your improvements.

---

## 🧠 Authors

Built with support from AI tools, network automation experts, and open-source contributions.

