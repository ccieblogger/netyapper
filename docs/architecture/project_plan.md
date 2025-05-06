# Project Plan: LLM-Powered MCP Integration Interface

This implementation plan outlines the major phases and milestones for building the LLM-MCP system, suitable for submission to a GitHub project board as the initial roadmap. It provides actionable guidance for developers implementing each component.

---

## 🗂️ Implementation Phases

### 🧱 Phase 1: Core Infrastructure

* [ ] **Set up project structure**

  * Establish directories for `api/`, `core/`, `mcp_clients/`, `schemas/`, `cli/`, and `web/`
  * Initialize Git, create `.env.example` for config, and set up dependency managers (`pip`, `npm`)
* [ ] **FastAPI server**

  * Create `main.py` with app factory and router registration
  * Scaffold basic `/health`, `/chat`, and `/dispatch` endpoints
* [ ] **LLM adapter layer**

  * Create a Python interface (e.g., `LLMClient`) that supports `.query(prompt: str)`
  * Implement wrappers for OpenAI and Ollama
* [ ] **Dispatcher for MCP routing**

  * Create `dispatcher.py` that maps `action` → `MCP client`
  * Validate structured command schema and handle errors cleanly
* [ ] **Mock NetBox MCP client**

  * Create a class with methods like `get_interface_ip(device, interface)` returning static values for now

### 💬 Phase 2: LLM & Intent Handling

* [ ] **Prompt design**

  * Define system prompts that ask the LLM to emit structured JSON from user queries
  * Example: `{ "action": "get_interface_ip", "params": { "device": "R1", "interface": "GigabitEthernet1" } }`
* [ ] **`/parse-intent` endpoint**

  * Create endpoint that accepts a user message and returns LLM-emitted JSON
  * Test LLM edge cases (vague input, incomplete data)
* [ ] **Validation and schema enforcement**

  * Define Pydantic schemas for structured intents
  * Validate incoming LLM outputs against schemas
* [ ] **CLI wrapper**

  * Add `query.py` to `cli/` that uses `click` or `argparse` to take user input and send it to the FastAPI server

### 🌐 Phase 3: Web Interface

* [ ] **Vue project scaffolding**

  * Initialize app using Vite + Vue 3 + PrimeVue + Tailwind
  * Set up layout, router, and component folder structure
* [ ] **Chat UI component**

  * Use PrimeVue's chat box or input components
  * Show user input, LLM response, and optionally structured action preview
* [ ] **API integration**

  * Use Axios to connect frontend to `/chat` and `/parse-intent`
  * Handle loading states, error messages, and JSON visualization

### 🔗 Phase 4: MCP Integration

* [ ] **Real NetBox MCP client**

  * Implement REST API calls to NetBox instance using `httpx`
  * Query interfaces, devices, and site attributes
* [ ] **Command routing**

  * Enhance dispatcher logic to call the real client instead of mock
  * Ensure robust error handling if MCP is offline or returns errors
* [ ] **Data transformation**

  * Convert NetBox API response to standard response format (to be sent back to LLM or UI)

### 🎨 Phase 5: UI/UX Polish

* [ ] **Component styling**

  * Customize PrimeVue components using Tailwind or PrimeFlex
  * Ensure visual consistency with light/dark modes if needed
* [ ] **MCP status indicators**

  * Add UI to show available MCP agents and their status
  * Optionally provide UI to inspect dispatcher routing
* [ ] **Feedback enhancement**

  * Include structured JSON view alongside conversational response

### 🧪 Phase 6: Testing + CI

* [ ] **Unit tests**

  * Use `pytest` for LLM adapter, dispatcher, and MCP clients
  * Mock external APIs and model outputs
* [ ] **Integration tests**

  * Validate complete query-to-response loop
  * Include tests for malformed inputs and agent errors
* [ ] **Dockerization**

  * Create `Dockerfile` and `docker-compose.yml` for web + API + MCP testing
* [ ] **GitHub Actions**

  * Add workflows to lint, test, and build Docker images

### 🚀 Phase 7: Documentation & Release

* [ ] **Developer documentation**

  * Describe endpoints, config variables, MCP patterns
* [ ] **API and schema reference**

  * Auto-generate Swagger docs via FastAPI
* [ ] **Release candidate**

  * Create example `.env` file
  * Add demo query scripts and NetBox sample data

---

## 🗂️ GitHub Project Board Usage

Each phase in this plan should be mapped to a GitHub milestone and tracked as a column or label in the GitHub Project board. Issues should be created per task and linked to milestones to provide visibility and traceability.

Let me know if you'd like assistance creating GitHub issues from this roadmap.
