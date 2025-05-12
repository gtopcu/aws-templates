
# pip install langchain langchain-experimental langchain-community langchain_openai
# pip install python-dotenv

# from dotenv import load_dotenv

# if not load_dotenv():
#     raise Exception("Failed to load .env file")

# OPEN_API_KEY = os.getenv("OPEN_AI_API_KEY")
# if not OPEN_API_KEY:
#     raise Exception("OPEN_API_KEY environment variable not set")


# from langchain.llms import OpenAI # deprecated
from langchain_openai import OpenAI
# from langchain.utilities import SQLDatabase # deprecated
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///hotels.db")
llm = OpenAI(temperature=0, verbose=True, api_key="adfsdsdf")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

db_chain.run("How many hotels are there?") # SELECT COUNT(*) FROM HOTELS