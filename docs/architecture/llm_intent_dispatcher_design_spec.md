# LLM Intent Dispatcher System Design Specification

## 📌 Purpose

Define a scalable and extensible system for translating natural language queries into structured commands routed to agent-based MCP servers. This system will support both local and API-based LLMs, and will evolve from a YAML-driven registry to a PostgreSQL-backed configuration interface.

---

## 🎯 Key Goals

* Provide CLI-based chat with LLM to execute structured tasks
* Use prompt engineering to extract structured JSON intents
* Support pluggable MCP backends via a dispatching interface
* Start with YAML action registry → transition to PostgreSQL
* Enable eventual extension via Web UI (admin-editable registry)

---

## 🧱 Architecture Overview

```
┌────────────┐         ┌──────────────┐         ┌────────────┐
│    CLI     │ ─────▶ │ FastAPI App  │ ─────▶ │ LLMClient  │
└────────────┘         │ /parse-intent│         │ (Ollama /  │
                       │ /dispatch    │         │  OpenAI)   │
                       └──────┬───────┘         └────┬──────┘
                              ▼                      ▼
                     ┌────────────┐         ┌────────────────┐
                     │ Action     │         │ MCP Dispatcher │
                     │ Registry   │         │ + MCP Clients  │
                     └────────────┘         └────────────────┘
```

---

## 🧩 Core Components

### 1. `LLMClient`

* Unified interface to OpenAI and Ollama
* Wraps model config, prompt handling, and API call

### 2. `PromptEngine`

* Generates prompt using `actions.yaml` (or future DB model)
* Injects supported actions + expected schema
* Example:

```text
You are an instruction parser...
Supported actions:
- get_interface_ip: Get IP of an interface (device, interface)
User: What is the IP of Gig1 on R1?
```

### 3. `actions.yaml`

```yaml
get_interface_ip:
  description: Get IP of interface
  params: [device, interface]
  mcp: netbox
```

### 4. `/parse-intent`

* Receives user message
* Uses `PromptEngine` → calls `LLMClient`
* Validates LLM response against schema:

```json
{"action": "get_interface_ip", "params": {"device": "R1", "interface": "GigabitEthernet1"}}
```

### 5. `Dispatcher`

* Uses action registry to find MCP client
* Calls:

```python
dispatch(action: str, params: dict) -> dict
```

### 6. MCP Clients

* Implement `MCPClient` interface:

```python
class MCPClient:
  def get_actions(self) -> List[str]
  def dispatch(self, action: str, params: dict) -> dict
```

* First target: `NetBoxMCPClient`

### 7. PostgreSQL Transition

* Define DB schema:

  * `ActionDefinition`
  * `PromptTemplate`
* Migrate from `actions.yaml` → DB
* Eventually editable via Web UI/API

---

## 📦 Extensibility Plan

| Layer         | Extension Mode      | Future Support            |
| ------------- | ------------------- | ------------------------- |
| Actions       | YAML → DB           | Web UI for editing        |
| MCP Clients   | Plugin registry     | Auto-discovery (optional) |
| Prompt Engine | Schema-based inject | Per-user prompts          |
| LLM Backends  | Swappable adapter   | Model config in DB        |

---

## 🔐 CLI Flow Summary

1. User submits question via CLI
2. FastAPI `/parse-intent` builds prompt
3. LLM returns structured intent
4. Dispatcher routes to MCP
5. MCP returns result
6. CLI prints response

---

## [2025-05-12] Prompt Generator Implementation Note

- The PromptEngine is implemented as described, with YAML-driven prompt construction and example output.
- See `docs/developer/README.md` for developer instructions on prompt and action modification, testing, and environment setup.

---

Next: See Developer Implementation Plan for file structure, initial code, and task breakdown.
