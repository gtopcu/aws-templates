# https://www.youtube.com/watch?v=kem-v9MXuG4
# pip install -U -q streamlit, langchain-core, langchain-community, langchain-ollama, ollama, SQLAlchemy

# ollama pull deepseek-r1:8b #14b

# streamlit run langchain_deepseekOllamaSQLAlch_textTosql.py

import re
import json

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st

from sqlalchemy import create_engine, inspect

db_url = "sqlite:///testdb.sqlite"
 # "postgresql+psycopg2://usr:pass@localhost/db"

template = """
You are a SQL generator. When the user provides a DB schema and asks a question, 
output the respective SQL statement to answer the question ONLY and nothing else

Schema: {schema}
User question: {query}
Output (SQL Only):
"""

model = OllamaLLM(model="deepseek-r1:8b", temperature=0)


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
    prompt = ChatPromptTemplate().from_template(template)
    chain = prompt | model

    return clean_text(chain.invoke({"query": query, "schema": schema}))


def clean_text(text: str):
    """deepseek answers using html with <think> tags. lets remove those for plain SQL"""
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()

extract_schema(db_url)
query = st.text_area("Describe what you want to extract from the DB")

if query:
    sql = to_sql_query(query, schema)
    st.code(sql, wrap_lines=True, language="sql")
