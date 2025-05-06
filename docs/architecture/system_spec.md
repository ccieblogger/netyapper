## Project Specification: LLM-Powered MCP Integration Interface

### 📌 Project Title

**Conversational Interface for MCP-enabled Systems Using Swappable LLMs**

---

### 🧭 Objective

Develop a unified Web and CLI application that allows users to interact with network management and third-party systems via natural language. The system utilizes a pluggable LLM backend to convert user prompts into structured commands and dispatches them to registered MCP (Model Context Protocol) servers.

---

### 🔍 Scope

* Support for both local and remote LLMs (Ollama, OpenAI, etc.)
* Structured intent parsing via LLM prompting
* Backend routing logic to dispatch commands to appropriate MCP servers
* Web UI (Vue) and CLI interface
* Initial integration with NetBox MCP

---

### 🎯 MVP Features

1. CLI to submit natural language queries
2. Web UI for chat-like interaction with the system
3. LLM abstraction layer with support for:

   * OpenAI via API key
   * Ollama via local HTTP API
4. Dispatcher service to route actions to MCP agents
5. MCP client for NetBox with mock and real modes
6. Structured JSON format for LLM intent extraction
7. Basic prompt framework with system instructions
8. Return results as structured and/or natural language

---

### 📋 Functional Requirements

* User can query: "What IP is assigned to Gig1 on R1?"
* System returns: "192.168.1.1" (via NetBox MCP)
* Must support multiple MCP agents and route to correct one
* Pluggable LLM engine (swappable at runtime or config)
* Unified format for all commands (e.g., `{action, params}`)
* Prompt injection with context about system capabilities
* CLI and Web must reuse same backend logic

---

### 🏗️ Non-Functional Requirements

* Self-contained backend (FastAPI)
* Modular and testable architecture
* Works offline with Ollama LLM
* Minimal frontend dependencies (Vue 3 + Tailwind)
* Async API calls for performance

---

### 🧩 Technical Stack

| Layer             | Technology                         |
| ----------------- | ---------------------------------- |
| Web UI            | Vue 3 + Vite + Tailwind + PrimeVue |
| CLI Tool          | Python `click`, `rich`             |
| API Server        | FastAPI (Python)                   |
| LLM Adapter       | LiteLLM / custom class             |
| LLM Models        | OpenAI, Ollama                     |
| MCP Client        | HTTP MCP interface                 |
| DevOps (optional) | Docker, GitHub Actions             |

---

### 🧪 Testing Plan

* Unit tests for LLM adapter and dispatcher
* Integration tests for query-to-MCP loop
* CLI tests with example inputs and outputs
* UI tests via Playwright or Cypress (optional)

---

### 📈 Success Criteria

* Users can successfully retrieve data via LLM from MCP
* LLM decisions are interpretable and auditable
* Multiple LLM backends can be swapped with config
* MCP agents can be easily extended with minimal boilerplate

---

Let me know when you'd like to turn this into GitHub issues, CI workflows, or documentation.
