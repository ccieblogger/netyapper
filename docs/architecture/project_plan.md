# Project Plan: LLM-Powered MCP Integration Interface

This implementation plan outlines the major phases and milestones for building the LLM-MCP system, suitable for submission to a GitHub project board as the initial roadmap. It provides actionable guidance for developers implementing each component.

This revised version focuses initially on building a **CLI-only, end-to-end functional flow** where a user can chat with an LLM, which parses the request and dispatches a structured command to an MCP server and returns the result. Web UI/UX elements have been moved to later phases.

---

## 🗂️ Implementation Phases

### 🧱 Phase 1: Core Infrastructure (CLI-based MVP)

* [ ] **Set up project structure**

  * Create directories for `api/`, `core/`, `mcp_clients/`, `schemas/`, `cli/`
  * Initialize Git, create `.env.example` for config, and install core dependencies
* [ ] **FastAPI server setup**

  * Create `main.py` with FastAPI app and minimal `/chat` and `/dispatch` routes
  * Add basic health check endpoint for connectivity
* [ ] **LLM adapter layer**

  * Create interface `LLMClient` to abstract `.query()`
  * Implement OpenAI + Ollama adapters
* [ ] **Intent parser route**

  * Add `/parse-intent` route to accept user messages and return JSON intent
* [ ] **Dispatcher logic**

  * Route known `action` keys to the appropriate MCP client class
  * Normalize input validation and MCP result formatting
* [ ] **Mock NetBox MCP Client**

  * Implement simulated logic in `netbox_mcp_client.py` to return fake device/interface info
* [ ] **Basic CLI tool**

  * Build `cli/query.py` that submits user input to backend endpoints and prints the result

### 🔗 Phase 2: Real MCP Integration

* [ ] **NetBox MCP client (real mode)**

  * Use `httpx` to connect to a real NetBox API instance
  * Implement device and interface querying functions
* [ ] **Dispatcher enhancement**

  * Route mock/real requests based on environment or CLI flag
  * Ensure structured responses comply with schema

### 💬 Phase 3: LLM Prompting + Schema Enforcement

* [ ] **Prompt engineering**

  * Define prompt templates that extract structured commands from user input
  * Example: `{"action": "get_interface_ip", "params": {"device": "R1", "interface": "GigabitEthernet1"}}`
* [ ] **Schema validation**

  * Implement Pydantic models to validate all structured outputs from the LLM
  * Handle fallback and error cases gracefully in the CLI

### 🌐 Phase 4: Web Interface (Deferred)

* [ ] **Vue + PrimeVue setup**

  * Initialize Vite + Vue 3 project using PrimeVue components
  * Set up project layout, chat panel, and API binding with Axios
* [ ] **Chat UI + Response display**

  * Allow users to type questions and view both LLM responses and JSON output from MCP

### 🎨 Phase 5: UI/UX Enhancements

* [ ] **Styling + layout polish**

  * Use Tailwind CSS and PrimeVue themes for consistent visuals
* [ ] **Agent/dispatcher status view**

  * Show which MCP clients are active/available and display backend logs

### 🧪 Phase 6: Testing + CI

* [ ] **Unit + integration testing**

  * Test all adapters, dispatchers, and MCP clients using `pytest`
* [ ] **Docker setup**

  * Add `Dockerfile` + `docker-compose.yml` for backend + CLI dev
* [ ] **GitHub Actions CI**

  * Linting, unit tests, and build validation

### 🚀 Phase 7: Documentation & Release

* [ ] **Developer docs**

  * Describe CLI usage, routes, config structure, and extension patterns
* [ ] **Swagger and schema docs**

  * Auto-generate with FastAPI OpenAPI integration
* [ ] **Initial release package**

  * Ship with CLI demo, README, and mock NetBox MCP support

---

## 🗂️ GitHub Project Board Usage

Each phase in this plan should be mapped to a GitHub milestone and tracked as a column or label in the GitHub Project board. Issues should be created per task and linked to milestones to provide visibility and traceability.

---

## [2025-05-12] Developer Note

- PromptEngine and YAML registry are implemented and tested as described.
- For developer usage, see `docs/developer/README.md`.
- Example prompt output and tests are available.
