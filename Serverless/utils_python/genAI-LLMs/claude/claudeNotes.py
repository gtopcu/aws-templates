
# https://console.anthropic.com/
# pip install anthropic

import anthropic
import os
from dotenv import load_dotenv


if not load_dotenv():
    raise Exception("Failed to load .env file")

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise Exception("ANTHROPIC_API_KEY environment variable not set")


def get_claude_response(prompt: str, model: str = "claude-3-sonnet-20240229", temperature: float = 0.7) -> str:
    """
    Get response from Claude LLM using the Anthropic API.

    Args:
        prompt (str): The input prompt for the model
        model (str): The model to use
        temperature (float): The temperature for sampling

    Returns:
        str: The response from the model
    """
    client = anthropic.Client(api_key=api_key)
    response = client.completions.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens_to_sample=100,
        stop_sequences=[anthropic.HUMAN_PROMPT],
    )
    return response.completion