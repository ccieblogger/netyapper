import unittest
from core.registry import ActionRegistry

class TestActionRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = ActionRegistry("actions.yaml")

    def test_supported_actions(self):
        actions = self.registry.get_supported_actions()
        self.assertIn("create_device", actions)
        self.assertIn("delete_device", actions)

    def test_get_action_schema(self):
        schema = self.registry.get_action_schema("create_device")
        self.assertIsNotNone(schema)
        self.assertEqual(schema["description"], "Create a new device in the system")
        self.assertIn("device_name", schema["params"])
        self.assertIn("device_type", schema["params"])
        self.assertIn("location", schema["params"])
        self.assertEqual(schema["mcp"], "netbox")

    def test_get_action_mcp(self):
        mcp = self.registry.get_action_mcp("delete_device")
        self.assertEqual(mcp, "netbox")

    def test_invalid_action(self):
        self.assertIsNone(self.registry.get_action_schema("nonexistent_action"))
        self.assertIsNone(self.registry.get_action_mcp("nonexistent_action"))

if __name__ == "__main__":
    unittest.main()
