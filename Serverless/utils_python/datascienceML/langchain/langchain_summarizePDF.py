
# https://www.youtube.com/watch?v=doRpfmXncEE
# pip install python-dotenv langchain langchain-community langchain-openai langchain-anthropic

import os
from dotenv import load_dotenv

from langchain.chains.summarize import import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()
# OPENAI_API_KEY=xxxx
# ANTHROPIC_API_KEY=xxxx

def summarize_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo") #gpt-4o
    llm = ChatAnthropic(temperature=0, model_name="claude-3-5-haiku-latest") #sonnet
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    summary = chain.invoke(docs)

if __name__ == "__main__":
    summary = summarize_pdf("file.pdf")
    print("Summary: ")
    print(summary["output.txt"])