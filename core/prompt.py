"""
PromptEngine: Dynamically builds LLM prompts from YAML registry templates.

Phases:
- Skeleton class and docstrings
- YAML registry integration (future phase)
- Prompt construction logic (future phase)
- Example output (future phase)
- Testing & docs (future phase)
"""

from typing import Any, Dict, Optional
from core.registry import ActionRegistry

class PromptEngine:
    """
    PromptEngine dynamically builds prompts for LLMs using templates from a YAML registry.

    Methods will be added in future phases to:
    - Load templates from YAML registry
    - Inject action, params, and user input
    - Output example prompts for testing/debugging
    """
    def __init__(self, registry: Optional[ActionRegistry] = None, registry_path: str = "actions.yaml"):
        """
        Initialize the PromptEngine with an ActionRegistry instance or YAML path.
        """
        if registry is not None:
            self.registry = registry
        else:
            self.registry = ActionRegistry(registry_path)

    def get_prompt_template(self, action_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve the prompt template (action schema) for a given action from the registry.
        Returns None if the action is not found.
        """
        return self.registry.get_action_schema(action_name)

    # Future methods:
    # def load_templates(self, registry_path: str): ...
    # def build_prompt(self, action: str, params: Dict[str, Any], user_input: str) -> str: ...
    # def example_prompt(self) -> str: ...
