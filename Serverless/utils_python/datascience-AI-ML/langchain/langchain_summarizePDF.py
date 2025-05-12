
# https://www.youtube.com/watch?v=doRpfmXncEE
# pip install python-dotenv langchain langchain-community langchain-openai langchain-anthropic

import os
from dotenv import load_dotenv

from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()
# OPENAI_API_KEY=xxxx
# ANTHROPIC_API_KEY=xxxx

def summarize_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()
    # llm = ChatOpenAI(temperature=0, model_name="gpt-4o") 
    llm = ChatAnthropic(temperature=0, model_name="claude-3-7-sonnet")
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    summary = chain.invoke(docs)

if __name__ == "__main__":
    summary = summarize_pdf("file.pdf")
    print("Summary: ")
    print(summary["output.txt"])


# import os
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_anthropic import ChatAnthropic
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.chains.summarize import load_summarize_chain

# def summarize_pdf(pdf_path, api_key):
#     """
#     Summarize a PDF file using Claude 3.5 Sonnet via LangChain
    
#     Args:
#         pdf_path (str): Path to the PDF file
#         api_key (str): Anthropic API key
    
#     Returns:
#         str: Summarized text of the PDF
#     """
#     # Validate input
#     if not os.path.exists(pdf_path):
#         raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
#     # Load the PDF
#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()
    
#     # Split the document into chunks
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=4000,
#         chunk_overlap=200,
#         length_function=len
#     )
#     split_docs = text_splitter.split_documents(documents)
    
#     # Initialize Claude model
#     llm = ChatAnthropic(
#         model='claude-3-5-sonnet-20240620',
#         anthropic_api_key=api_key,
#         temperature=0.3
#     )
    
#     # Create summarization chain
#     chain = load_summarize_chain(
#         llm, 
#         chain_type='map_reduce', 
#         verbose=True
#     )
    
#     # Generate summary
#     summary = chain.run(split_docs)
    
#     return summary

# def main():
#     # Replace with your actual API key
#     ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
#     if not ANTHROPIC_API_KEY:
#         raise ValueError("Please set the ANTHROPIC_API_KEY environment variable")
    
#     # Path to your PDF file
#     pdf_path = 'document.pdf'
    
#     try:
#         # Generate and print summary
#         summary = summarize_pdf(pdf_path, ANTHROPIC_API_KEY)
#         print("\n--- PDF SUMMARY ---")
#         print(summary)
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()