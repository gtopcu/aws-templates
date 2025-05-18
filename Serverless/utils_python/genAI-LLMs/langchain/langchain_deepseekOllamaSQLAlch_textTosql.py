# https://www.youtube.com/watch?v=kem-v9MXuG4
# pip install -U -q streamlit, langchain-core, langchain-community, langchain-ollama, ollama, SQLAlchemy

# ollama pull deepseek-r1:8b #14b

import re
import json

from langchain_ollama.llms import OllamaLLM
from sqlalchemy import create_engine, inspect

db_url = "sqlite:///testdb.sqlite"
# "postgresql+psycopg2://usr:pass@localhost/db"

template = """
You are a SQL generator. When the user provides a DB schema and asks a question, 
output the respective SQL statement to answer the question ONLY and nothing else

Schema: {schema}
User question: {query}
Output(SQL Only):
"""

llm = OllamaLLM(model="deepseek-r1:8b", temperature=0)


def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}

    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        # for column in columns:
        #     print(f"{column['name']} {column['type']}")
        schema[table] = [column["name"] for column in columns]

    return json.dumps(schema)


def to_sql_query(query, schema):
    pass


# prompt = llm.invoke(template)
