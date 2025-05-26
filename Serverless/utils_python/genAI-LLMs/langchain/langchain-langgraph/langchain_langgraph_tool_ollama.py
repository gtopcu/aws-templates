
# https://www.youtube.com/watch?v=9mLzD997JsU

# pip install ollama, imap_tools
# ollama list
# ollama serve
# ollama pull qwen3:8b
# ollama pull llava 
# ollama pull llama4

import ollama

import os
import json
from typing import TypedDict

from dotenv import load_dotenv
# from imap_tools import MailBox, AND

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, START, END

load_dotenv()

class ChatState(TypedDict):
    messages: list

@tool
def list_unread_emails():
    """Return a bullet list of every UNREAD email's UID, subject, date and sender"""
    print("Tool use: list_unread_emails")

    response = json.dumps([
        {
            "UID": "1111-2222-33333333-44444444-5555-6666",
            "Subject": "Hello there",
            "Date": "2025-05-25T15:14:00",
            "Sender": "gtopcu@gmail.com"
        },
        {
            "UID": "1111-2222-33333333-44444444-5555-6667",
            "Subject": "Hello there 2",
            "Date": "2025-05-25T15:15:00",
            "Sender": "gtopcu2@gmail.com"
        }
    ])
    return response

llm = init_chat_model(model="qwen3:8b", model_provider="ollama")
llm = llm.bind_tools([list_unread_emails])
# llm.invoke(prompt).content

def llm_node(state):
   response = llm.invoke(state['messages'])
   return {'messages': state['messages'] + [response]}

def router(state):
   last_message = state['messages'][-1]
   return 'tools' if getattr(last_message, 'tool_calls', None) else 'end'

# tool_node = ToolNode([list_unread_emails])
tool_node = ToolNode([list_unread_emails])

def tools_node(state):
    result = tool_node.invoke(state)

    return {
        'messages': state['messages'] + result['messages']
    }


builder = StateGraph(ChatState)
builder.add_node('llm', llm_node)
builder.add_node('tools', tool_node)
builder.add_edge(START, 'llm')
builder.add_edge('tools', 'llm')
builder.add_conditional_edges('llm', router, {'tools': 'tools', 'end': END})

graph = builder.compile()

if "__name__" == "__main__":
    state = { "messages": [] }
    print("Type an instruction or 'quit'\n")

    while True:
        user_message = input("> ")
        if user_message.lower() == "quit":
            break
        state["messages"].append({"role":"user", "content": user_message})
        state = graph.invoke(state)
        print(state["messages"][-1].content)