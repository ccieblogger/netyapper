import click
import requests
from rich import print

API_URL = "http://localhost:8000"  # Adjust if backend runs elsewhere

@click.group()
def cli():
    """CLI tool for netyapper backend interaction."""
    pass

@cli.command()
@click.argument("prompt")
def chat(prompt):
    """Send a prompt to the /chat endpoint and print the LLM response."""
    resp = requests.post(f"{API_URL}/chat", json={"prompt": prompt})
    if resp.ok:
        print(f"[bold green]LLM:[/bold green] {resp.json().get('response')}")
    else:
        print(f"[bold red]Error:[/bold red] {resp.text}")

@cli.command()
@click.argument("action")
@click.option("--device", default=None, help="Device name")
@click.option("--interface", default=None, help="Interface name")
def dispatch(action, device, interface):
    """Send an action to the /dispatch endpoint and print the result."""
    params = {k: v for k, v in {"device": device, "interface": interface}.items() if v}
    resp = requests.post(f"{API_URL}/dispatch", json={"action": action, "params": params})
    if resp.ok:
        print(f"[bold blue]Result:[/bold blue] {resp.json()}")
    else:
        print(f"[bold red]Error:[/bold red] {resp.text}")

if __name__ == "__main__":
    cli()
