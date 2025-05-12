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

    def build_prompt(self, action: str, params: Dict[str, Any], user_input: str) -> Optional[str]:
        """
        Build a prompt string for the LLM by injecting the action, params, and user input into a template.
        Returns the constructed prompt, or None if the action is not found.
        """
        schema = self.get_prompt_template(action)
        if not schema:
            return None
        # Example prompt format (can be refined as needed):
        prompt = (
            f"You are an instruction parser.\n"
            f"Supported action: {action}\n"
            f"Description: {schema.get('description', '')}\n"
            f"Parameters: {', '.join(schema.get('params', []))}\n"
            f"\nUser input: {user_input}\n"
            f"Parameters provided: {params}\n"
            f"Respond with a structured JSON intent."
        )
        return prompt

    def example_prompt(self) -> str:
        """
        Output an example prompt for testing/debugging using the first available action.
        """
        actions = self.registry.get_supported_actions()
        if not actions:
            return "No actions available in registry."
        action = actions[0]
        schema = self.get_prompt_template(action)
        params = {p: f"example_{p}" for p in schema.get('params', [])}
        user_input = f"Example user input for action '{action}'"
        return self.build_prompt(action, params, user_input)
