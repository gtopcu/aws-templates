
# https://console.anthropic.com/
# pip install langchain anthropic

import anthropic
import os

from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage

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