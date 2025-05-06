## LLM + MCP Integration System Architecture

### 🧭 Overview

This document defines the architecture for an application that allows users to interact with LLMs (Large Language Models) via Web and CLI interfaces. The system enables users to query external systems (e.g., NetBox, Cisco devices) using natural language. The LLM interprets user input, generates structured commands, and dispatches them to the appropriate Model Context Protocol (MCP) agent.

---

### 🎯 Goals

* Provide a unified Web and CLI conversational interface.
* Enable LLM-based understanding and transformation of natural language into structured tasks.
* Support pluggable LLM backends (e.g., OpenAI API, Ollama-hosted models).
* Enable dynamic routing of structured tasks to MCP servers based on capability.
* Return actionable and human-readable results to the user.

---

### ⚙️ System Components

#### 1. **Frontend**

* **Web Interface**: Vue 3 + Vite + Tailwind CSS
* **UI Components**: Preference for PrimeVue components and styling for consistent design and feature-rich UI
* **CLI Interface**: Python `click` + `rich`/`textual`
* Displays chat conversation with LLM and response outputs

#### 2. **Backend API**

* **Framework**: FastAPI (Python)
* **Endpoints**:

  * `/chat`: Handle chat input, invoke LLM, and dispatch to MCP
  * `/parse-intent`: Extract intent/entities from LLM
  * `/dispatch`: MCP dispatcher for routing structured tasks

#### 3. **LLM Adapter Layer**

* Wraps local (Ollama) and external (OpenAI, Groq) models
* Abstracts model config, API keys, prompt handling
* Supports context injection for system capabilities

#### 4. **Dispatcher Layer**

* Maintains MCP capability routing map
* Delegates structured task to correct MCP agent
* Handles request transformation, error normalization

#### 5. **MCP Integration Layer**

* HTTP/gRPC clients to interact with MCP servers
* Each MCP server exposes capabilities and actions (e.g., NetBox, CiscoCLI)
* Returns structured responses to backend

#### 6. **Result Formatter**

* Uses LLM to generate user-friendly response from raw MCP result
* Re-injects data for formatting if necessary

#### 7. **Authentication (Future Phase)**

* Basic token auth or OAuth for user sessions
* Role-based access control for MCP capabilities

---

### 🔄 Data Flow

1. User submits question (Web/CLI)
2. LLM parses question → JSON action object
3. Backend routes action via dispatcher → appropriate MCP
4. MCP executes command, returns result
5. Backend formats result via LLM (if needed)
6. Response returned to frontend

---

### 🔌 Supported LLM Backends

* **Local**: Ollama, LM Studio (e.g., Mistral, LLaMA3)
* **API**: OpenAI, Anthropic, Groq, TogetherAI

---

### 📦 Supported MCPs (Initial Targets)

* `netbox-mcp`: Queries device info from NetBox
* `cisco-cli-mcp`: Runs show commands and parses output
* `generic-rest-mcp`: Wrapper to talk to REST-based systems

---

### 📁 Suggested Directory Structure

```
app/
├── api/                # FastAPI routes
├── core/               # Dispatcher, LLM adapter, settings
├── mcp_clients/        # NetBox, Cisco MCP integrations
├── schemas/            # Pydantic models for intent and results
├── templates/          # Prompt templates
├── cli/                # CLI entrypoints
├── web/                # Web UI (Vue 3 + Vite)
└── main.py             # App entrypoint
```

---

### 📈 Scaling Considerations

* Add Redis for job queueing or caching
* Use PostgreSQL for history/log storage
* Move MCP capability discovery to registry service

---

### 🧪 Testing Strategy

* Use `pytest` with test MCP stubs
* Mock LLM responses for predictable CI
* Add integration tests for dispatcher + MCP agents

---

Let me know when you're ready to review the project specification document.
