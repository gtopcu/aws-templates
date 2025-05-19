
""" 
Can answer from unstructured & structured data such as code, PDF, website, DBs and unstructured data

The pipeline for converting raw unstructured data  into a QA chain is as follows:
1. Loading: Langchain integration hub contains many loaders for loading unstructured data. Each loader returns a Document object
2. Splitting: TextSplitters split documents into splits of specified size
3. Storage: Storage (usually a vector store) will house and often embed the splits
4. Retrieval: The app retrieves the splits from storage (often with similar embeddings to the input question)
5. Generation: An LLM produces an answer using a prompt that includes the question and the retrieved data
6. Conversation(Extension): Hold a long term conversion by adding a Memory to your QA chain

This whole pipeline can all be wrapped in a single object: VectorstoreIndexCreator
This sample will load the data from a blog site
"""

# pip install langchain langchain-experimental langchain-community langchain_openai
# pip install chromadb
# pip install python-dotenv

# from dotenv import load_dotenv

# if not load_dotenv():
#     raise Exception("Failed to load .env file")

# OPEN_API_KEY = os.getenv("OPEN_AI_API_KEY")
# if not OPEN_API_KEY:
#     raise Exception("OPEN_API_KEY environment variable not set")

from langchain_openai import OpenAI
# from langchain.document_loaders import WebBaseLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings.openai import OpenAIEmbeddings

openai_embedding = OpenAIEmbeddings(openai_api_key="my-api-key")
openai_embedding.embed_documents(texts="adsffsdsafd")

loader = WebBaseLoader(web_path="https://blog.serverlessadvocate.com/dedicated-outbound-ip-address-with-aws-lambda-637cc05d95cd")
index = VectorstoreIndexCreator(embedding=openai_embedding).from_loaders([loader])
# index = VectorstoreIndexCreator().from_loaders([loader])
#index.query("How can I set an outbound IP address for lambda?")