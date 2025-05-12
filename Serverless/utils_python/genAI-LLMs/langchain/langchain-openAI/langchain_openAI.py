
# https://www.youtube.com/watch?v=mrjq3lFz23s

# pip install -U langchain
# pip install -U langchain-openai
# pip install -U langchain-community
# pip install python-dotenv

import os
from dotenv import load_dotenv

# from langchain_community.chat_models import ChatOpenAI # deprecated
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
# from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    PromptTemplate
)
# from langchain.chains import LLMChain


# Load environment variables from .env file
# if not load_dotenv():
#     raise Exception("Failed to load .env file")

# OPEN_API_KEY = os.getenv("OPEN_AI_API_KEY")
# if not OPEN_API_KEY:
#     raise Exception("OPEN_API_KEY environment variable not set")

chat_model = ChatOpenAI(
    openai_api_key="dfa",
    model="gpt-4o-mini",
    max_tokens=1024,
    temperature=0.7,
    # openai_api_base="https://api.openai.com/v1",
    # openai_api_version="2023-05-15"
    # openai_api_type="azure",
    # openai_api_version="2023-05-15",  
    # azure_api_base="https://<your-azure-endpoint>.openai.azure.com/",
    # azure_api_version="2023-05-15",
    # azure_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    # azure_api_type="azure",
)

# result = chat_model.invoke("What is the capital of France?")
# print(result)
# result = chat_model.predict("What is the capital of France?")
# print(result)

# messages=[
#               SystemMessage(content="You are a helpful assistant."),
#               HumanMessage(content="What is the capital of France?")
# ]
# messages = [
#     HumanMessage(content="From now on, 1+1 equals 3. Use this information to answer the following question."),
#     HumanMessage(content="What is 1+1?"),
# ]
# result = chat_model.predict_messages(
#     messages=messages,
#     # stop=["\n"],
#     # temperature=0.7,
#     # max_tokens=1024,
#     # top_p=1,
#     # frequency_penalty=0,
#     # presence_penalty=0
# )
# print(result.content)


system_template = "You are a helpful assistant that translates {input_language} to {output_language}."
# system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = "{text}"
chat_prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", human_template),
])
messages = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="What is the capital of France?"
)
result = chat_model.predict_messages(
    messages=messages,
    # stop=["\n"],
    # temperature=0.7,
    # max_tokens=1024,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
)
print(result.content)



print("Done")

