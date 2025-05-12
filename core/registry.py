import yaml
from typing import List, Dict, Any, Optional

class ActionRegistry:
    """
    Loads and validates actions from a YAML file.
    Provides access to supported actions and their schemas.
    """
    def __init__(self, yaml_path: str = "actions.yaml"):
        self.yaml_path = yaml_path
        self.actions = self._load_actions()

    def _load_actions(self) -> List[Dict[str, Any]]:
        try:
            with open(self.yaml_path, "r") as f:
                data = yaml.safe_load(f)
                if not isinstance(data, list):
                    raise ValueError("actions.yaml must contain a list of actions.")
                for action in data:
                    if "name" not in action or "parameters" not in action:
                        raise ValueError(f"Invalid action definition: {action}")
                return data
        except Exception as e:
            raise RuntimeError(f"Failed to load actions.yaml: {e}")

    def get_supported_actions(self) -> List[str]:
        return [action["name"] for action in self.actions]

    def get_action_schema(self, action_name: str) -> Optional[Dict[str, Any]]:
        for action in self.actions:
            if action["name"] == action_name:
                return action
        return None
