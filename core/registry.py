import yaml
from typing import List, Dict, Any, Optional

class ActionRegistry:
    """
    Loads and validates actions from a YAML file (mapping format).
    Provides access to supported actions and their schemas.
    """
    def __init__(self, yaml_path: str = "actions.yaml"):
        self.yaml_path = yaml_path
        self.actions = self._load_actions()

    def _load_actions(self) -> Dict[str, Dict[str, Any]]:
        try:
            with open(self.yaml_path, "r") as f:
                data = yaml.safe_load(f)
                if not isinstance(data, dict):
                    raise ValueError("actions.yaml must be a mapping of action names to definitions.")
                for name, action in data.items():
                    if "description" not in action or "params" not in action or "mcp" not in action:
                        raise ValueError(f"Invalid action definition for '{name}': {action}")
                return data
        except Exception as e:
            raise RuntimeError(f"Failed to load actions.yaml: {e}")

    def get_supported_actions(self) -> List[str]:
        return list(self.actions.keys())

    def get_action_schema(self, action_name: str) -> Optional[Dict[str, Any]]:
        return self.actions.get(action_name)

    def get_action_mcp(self, action_name: str) -> Optional[str]:
        action = self.actions.get(action_name)
        if action:
            return action.get("mcp")
        return None
