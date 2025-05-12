# Developer Implementation Plan: LLM Intent Dispatcher

This plan outlines a set of sequential, modular workstreams a developer can implement to create the LLM-driven intent parsing and MCP dispatch system, initially using YAML-based config and later PostgreSQL.

---

## 🧱 Workstream 1: Project Scaffold & Dev Environment

**Goal:** Create a baseline FastAPI project with CLI + containers.

### Tasks

* [ ] Create Python project with `app/`, `cli/`, `schemas/`, `core/`, `mcp_clients/`
* [ ] Add `pyproject.toml` or `requirements.txt`
* [ ] Add `docker-compose.dev.yml` with:

  * FastAPI (hosted locally)
  * PostgreSQL (for future DB migration)
  * Optional: Ollama container (if desired)
* [ ] Add CLI entry: `cli/query.py`

---

## 💬 Workstream 2: YAML-Based Action Registry

**Goal:** Define and load `actions.yaml`

### Tasks

* [ ] Create `actions.yaml` with example:

```yaml
get_interface_ip:
  description: Get IP of an interface
  params: [device, interface]
  mcp: netbox
```

* [ ] Create `ActionRegistry` class in `core/registry.py` that:

  * Loads and validates YAML
  * Provides `get_supported_actions()` and `get_action_schema()`

---

## ✨ Workstream 3: Prompt Generator

**Goal:** Dynamically build LLM prompts from YAML registry

### Tasks

* [ ] Create `PromptEngine` in `core/prompt.py`
* [ ] Inject `action`, `params`, and user input
* [ ] Output example prompt for testing/debugging

---

## [2025-05-12] Workstream 3: Prompt Generator Status

- The PromptEngine (`core/prompt.py`) is now implemented and tested.
- Prompts are dynamically built from `actions.yaml` using the `PromptEngine`.
- Example prompt output and unit tests are available (see `core/print_example_prompt.py` and `tests/test_prompt.py`).
- See `docs/developer/README.md` for developer usage, testing, and extension instructions.

---

## Documentation Note

- The prompt generation and registry integration are now implemented as described in this plan.
- For up-to-date usage and extension, see the developer README.

---

## 🔌 Workstream 4: LLM Adapter

**Goal:** Unified access to OpenAI and Ollama

### Tasks

* [ ] Create `LLMClient` interface in `core/llm.py`
* [ ] Implement `OpenAIClient` and `OllamaClient`
* [ ] Use environment variables or `.env` to select backend

---

## 🔍 Workstream 5: Parse Intent Endpoint

**Goal:** Convert natural language to structured JSON intent

### Tasks

* [ ] Create `/parse-intent` route in `api/routes.py`
* [ ] Call `PromptEngine` + `LLMClient`
* [ ] Validate with `ParsedIntent` schema:

```python
class ParsedIntent(BaseModel):
  action: str
  params: dict[str, str]
```

* [ ] Return JSON response or error

---

## 📡 Workstream 6: Dispatcher + MCP Stub

**Goal:** Route structured intent to correct MCP

### Tasks

* [ ] Create `Dispatcher` in `core/dispatcher.py`
* [ ] Map action → MCP client
* [ ] Implement `NetBoxMCPClient` mock with method:

```python
def dispatch(action: str, params: dict) -> dict:
    return {"ip_address": "192.168.1.1"}
```

---

## 🔁 Workstream 7: CLI Integration

**Goal:** Complete CLI-driven round trip

### Tasks

* [ ] In `cli/query.py`:

  * Read user input
  * Send to `/parse-intent`
  * Then send to `/dispatch` endpoint
  * Print result in console

---

## 🧪 Workstream 8: Testing

**Goal:** Provide reliability and future confidence

### Tasks

* [ ] Use `pytest` to test:

  * LLM prompt generation
  * Dispatcher routing
  * Action registry parsing
  * CLI response formatting

---

## 🧰 Workstream 9: PostgreSQL Transition

**Goal:** Replace YAML with DB-driven config (later stage)

### Tasks

* [ ] Create models: `ActionDefinition`, `PromptTemplate`
* [ ] Seed from initial YAML
* [ ] Replace `ActionRegistry` to query via SQLAlchemy
* [ ] Add Alembic migration system
* [ ] Update `PromptEngine` to pull from DB

---

Let me know when you’re ready to generate GitHub issues or initial project files from this plan.
