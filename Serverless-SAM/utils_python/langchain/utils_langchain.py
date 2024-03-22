
# https://www.youtube.com/watch?v=aywZrzNaKjs
# https://python.langchain.com/docs/integrations/chat/openai

"""
python3 -m venv venv
source venv/bin/activate

pip install python-dotenv 

pip install -U langchain-openai

#Deprecated:
pip install langchain
pip install openai

pip install pinecone-client
"""

import os
from dotenv import load_dotenv, find_dotenv

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    PromptTemplate
)
from langchain_openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter

from pinecone import Pinecone, ServerlessSpec, PodSpec

if not load_dotenv(find_dotenv()):
    raise Exception("Failed to load .env file")

OPEN_API_KEY = os.getenv("OPEN_AI_API_KEY")

"""
https://platform.openai.com/account/limits
gpt-3.5-turbo
text-davinci-003
text-embedding-3-large
"""

# Text Model
# llm = OpenAI(name="text-davinci-003", api_key=OPEN_API_KEY, temperature=0.7, max_tokens=1024)
# print(llm.invoke("how far is the moon in km?"))

# Chat Model
# llm = ChatOpenAI(name="gpt-3.5-turbo", api_key=OPEN_API_KEY, temperature=0.7, max_tokens=1024)
# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="What is the capital of France?")
# ]
# response = llm.invoke(messages)
# print(response)

# Templates
# system_template = ("You are a helpful assistant that translates {input_language} to {output_language}.")
# system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
# human_template = "{text}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
# chat_prompt = ChatPromptTemplate.from_messages(
#      [system_message_prompt, human_message_prompt]
#  )
# llm = ChatOpenAI(name="gpt-3.5-turbo", api_key=OPEN_API_KEY, temperature=0.7, max_tokens=1024)
# response: AIMessage = llm.invoke(
#     chat_prompt.format_prompt(
#         input_language="English", output_language="French", text="I love programming."
#     ).to_messages()
# )
# print(response.content)

# Chain = LLM + Prompt
# prompt_template = ("You are an expert data scientist with an expertise in building large language models. Explain term {term}")
# prompt = PromptTemplate(
#                     input_variables=["term"],
#                     template=prompt_template
#                 )
# llm = OpenAI(name="text-davinci-003", api_key=OPEN_API_KEY)
# chain = LLMChain(llm=llm, prompt=prompt)
# print(chain.invoke("autoencoder"))


# Embedding
# https://python.langchain.com/docs/integrations/text_embedding/openai

# textSplitter = RecursiveCharacterTextSplitter(
#     chunk_size=100, chunk_overlap=0, length_function=len,
#     keep_separator=True, is_separator_regex=False
# )
# textSplitter.split_text("This is a very long test document.")
# texts: list[str] = textSplitter.create_documents(["This is a very long test document.", "Continued"])
# print(texts[0].page_content)

# text-embedding-ada-002
# text-embedding-3-large
# embeddings = OpenAIEmbeddings(model="ada", api_key=OPEN_API_KEY) # dimensions=1024
# text = "This is a test document."
# query_result = embeddings.embed_query(text)
# print(query_result)
# response: list[str] = doc_result = embeddings.embed_documents([texts])
# for embedding in response:
#     print(embedding)


# Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

pc = Pinecone(api_key=PINECONE_API_KEY)

print(pc.list_collections())
print(pc.list_indexes())

index = pc.Index(PINECONE_INDEX)
for idx in index.list():
    print(idx)

# index.upsert(
#     vectors=[
#         {
#             "id": "vec1", 
#             "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
#             "metadata": {"genre": "drama"}
#         }, {
#             "id": "vec2", 
#             "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], 
#             "metadata": {"genre": "action"}
#         }, {
#             "id": "vec3", 
#             "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], 
#             "metadata": {"genre": "drama"}
#         }, {
#             "id": "vec4", 
#             "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], 
#             "metadata": {"genre": "action"}
#         }
#     ],
#     namespace= "ns1"
# )

# index.query(
#     namespace="ns1",
#     vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
#     top_k=2,
#     include_values=True,
#     include_metadata=True,
#     filter={"genre": {"$eq": "action"}}
# )
