import unittest
from core.prompt import PromptEngine

class TestPromptEngine(unittest.TestCase):
    def setUp(self):
        self.engine = PromptEngine()

    def test_get_prompt_template_valid(self):
        template = self.engine.get_prompt_template("create_device")
        self.assertIsNotNone(template)
        self.assertIn("description", template)
        self.assertIn("params", template)

    def test_get_prompt_template_invalid(self):
        template = self.engine.get_prompt_template("nonexistent_action")
        self.assertIsNone(template)

    def test_build_prompt_valid(self):
        params = {"device_name": "R1", "device_type": "router", "location": "DC1"}
        prompt = self.engine.build_prompt("create_device", params, "Add a router named R1 in DC1")
        self.assertIsInstance(prompt, str)
        self.assertIn("create_device", prompt)
        self.assertIn("device_name", prompt)
        self.assertIn("Add a router named R1 in DC1", prompt)

    def test_build_prompt_invalid_action(self):
        prompt = self.engine.build_prompt("nonexistent_action", {}, "Test input")
        self.assertIsNone(prompt)

    def test_example_prompt(self):
        prompt = self.engine.example_prompt()
        self.assertIsInstance(prompt, str)
        self.assertIn("You are an instruction parser", prompt)

if __name__ == "__main__":
    unittest.main()
