
# https://console.anthropic.com/

# pip install langchain
# pip install anthropic[all]
# pip install langchain[anthropic]
# pip install anthropic

import os

from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage

from dotenv import load_dotenv

# Load environment variables from .env file
if not load_dotenv():
    raise Exception("Failed to load .env file")

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise Exception("ANTHROPIC_API_KEY environment variable not set")

chat = ChatAnthropic(
    anthropic_api_key=api_key, 
    model="claude-3-sonnet-20240229" 
)

messages = [HumanMessage(content="Hello, how are you today?")]
response = chat(messages)

print(response.content)