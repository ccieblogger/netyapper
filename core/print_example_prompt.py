"""
Script to print an example LLM prompt using PromptEngine for testing/debugging.
"""
from core.prompt import PromptEngine

if __name__ == "__main__":
    engine = PromptEngine()
    print("\n--- Example LLM Prompt ---\n")
    print(engine.example_prompt())
    print("\n-------------------------\n")
