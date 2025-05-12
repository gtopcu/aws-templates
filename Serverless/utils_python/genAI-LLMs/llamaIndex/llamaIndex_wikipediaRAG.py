
# https://www.youtube.com/watch?v=M9GtHb32F8w

"""
pip install dotenv streamlit llama-index llama-index-readers-wikipedia
.env should contain OPENAI_API_KEY
"""

import os
import streamlit as st
from dotenv import load_dotenv

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
# from llama_index.core import VectorStoreQueryMode, VectorStoreQuery, Document, DocumentStore, DocumentStoreQueryMode, DocumentStoreQuery

# from llama_index.vector_stores import ChromaVectorStore
# from llama_index.vector_stores.types import (
#     VectorStore,
#     VectorStoreQueryMode,
#     VectorStoreQuery,
# )
# from llama_index.prompts.prompts import (
#     Prompt,
#     PromptTemplate,
#     QuestionAnswerPrompt,
#     QuestionAnswerPromptTemplate,
# )

load_dotenv()

INDEX_DIR = "wiki_rag"
PAGES = [ "Artificial Intelligence", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision" ]

@st.cache_resource
def get_index():
    if os.path.isdir(INDEX_DIR):
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        return load_index_from_storage(storage_context)

    docs = WikipediaReader().load_data(pages=PAGES, auto_suggest=False)
    embedding_model = OpenAIEmbedding(model="text-embedding-3-small")
    index = VectorStoreIndex.from_documents(docs, embedding_model=embedding_model)
    
    return index


@st.cache_resource
def get_query_engine():
    index = get_index()

    llm = OpenAI(
        model="gpt-4o-mini",
        temperature=0
        # max_tokens=512,
        # streaming=True,
    )

    return index.as_query_engine(
        llm=llm,
        similarity_top_k=3
        # response_mode="tree_summarize",
        # use_async=True,
    )

def main():

    st.title("Wikipedia RAG with LlamaIndex")
    st.write("This is a simple example of using LlamaIndex to query Wikipedia articles.")
    st.write("You can ask questions about the following topics:")
    st.write(", ".join(PAGES))

    question = st.text_input("Enter your question:")
    if st.button("Submit") and question:
        with st.spinner("Loading..."):
            qe = get_query_engine()
            response = qe.query(question)

            st.subheader("Answer:")
            st.write(response.response)
            # st.subheader("Source Documents:")
            # for doc in response.source_nodes:
            #     st.write(f"- {doc.node.text[:100]}... (Source: {doc.node.get_doc_id()})")
            #     st.write(f"- {doc.node.get_doc_id()}")
            
            st.subheader("Retrieved Context") 

            for src in response.source_nodes:
                st.markdown(src.node.get_content())

    if __name__ == "__main__":
        main()