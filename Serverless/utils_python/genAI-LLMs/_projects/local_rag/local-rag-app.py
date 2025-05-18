"""
Local RAG Application using OpenAI o4-mini model
This application runs completely offline without internet connection.
"""

import os
import sys
from typing import List, Dict, Any
import argparse

# For document processing
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# For vector database
import chromadb
from chromadb.utils import embedding_functions

# For local OpenAI model
from openai import OpenAI

class LocalRAGSystem:
    def __init__(self, 
                 docs_dir: str,
                 db_dir: str = "./chroma_db",
                 model_name: str = "o4-mini",
                 chunk_size: int = 1000,
                 chunk_overlap: int = 200):
        """
        Initialize the RAG system with local components
        
        Args:
            docs_dir: Directory containing documents to index
            db_dir: Directory to store the vector database
            model_name: Name of the local OpenAI model to use
            chunk_size: Size of text chunks for indexing
            chunk_overlap: Overlap between chunks
        """
        self.docs_dir = docs_dir
        self.db_dir = db_dir
        self.model_name = model_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Initialize the client for local OpenAI model
        # Assuming the model is running locally via ollama or similar
        self.client = OpenAI(
            base_url="http://localhost:11434/v1",  # Adjust if using a different port
            api_key="ollama",  # Placeholder API key for local models
        )
        
        # Initialize the vector database
        self.chroma_client = chromadb.PersistentClient(path=db_dir)
        
        # Use the local model for embeddings
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key="ollama",
            model_name=model_name,
            api_base="http://localhost:11434/v1"
        )
        
        # Create or get the collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="document_collection",
            embedding_function=self.embedding_function
        )
        
        # Text splitter for document processing
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    
    def load_and_index_documents(self):
        """Load documents from directory and index them in the vector database"""
        print(f"Loading documents from {self.docs_dir}...")
        
        # Load documents from the specified directory
        loader = DirectoryLoader(
            self.docs_dir,
            glob="**/*.txt",  # Load all text files
            loader_cls=TextLoader
        )
        documents = loader.load()
        print(f"Loaded {len(documents)} documents")
        
        # Split documents into chunks
        chunks = self.text_splitter.split_documents(documents)
        print(f"Split into {len(chunks)} chunks")
        
        # Add documents to the vector database
        for i, chunk in enumerate(chunks):
            # Generate embeddings and add to collection
            self.collection.add(
                documents=[chunk.page_content],
                metadatas=[{"source": chunk.metadata.get("source", "unknown")}],
                ids=[f"chunk_{i}"]
            )
        
        print(f"Indexed {len(chunks)} chunks in the vector database")
    
    def query(self, question: str, top_k: int = 3) -> str:
        """
        Query the RAG system with a question
        
        Args:
            question: The question to ask
            top_k: Number of most relevant chunks to retrieve
            
        Returns:
            The generated answer
        """
        # Retrieve relevant documents
        results = self.collection.query(
            query_texts=[question],
            n_results=top_k
        )
        
        retrieved_docs = results["documents"][0]
        
        # Construct the prompt with retrieved context
        context = "\n\n".join(retrieved_docs)
        prompt = f"""Answer the question based on the following context:

Context:
{context}

Question: {question}

Answer:"""
        
        # Generate response using the local model
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )
        
        return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Local RAG Application")
    parser.add_argument("--docs_dir", type=str, required=True, help="Directory containing documents to index")
    parser.add_argument("--db_dir", type=str, default="./chroma_db", help="Directory to store the vector database")
    parser.add_argument("--index", action="store_true", help="Index documents before querying")
    parser.add_argument("--query", type=str, help="Query to run against the RAG system")
    
    args = parser.parse_args()
    
    rag_system = LocalRAGSystem(
        docs_dir=args.docs_dir,
        db_dir=args.db_dir
    )
    
    if args.index:
        rag_system.load_and_index_documents()
    
    if args.query:
        answer = rag_system.query(args.query)
        print("\nQuestion:", args.query)
        print("\nAnswer:", answer)
    else:
        # Interactive mode
        print("Enter your questions (type 'exit' to quit):")
        while True:
            question = input("\nQuestion: ")
            if question.lower() == "exit":
                break
            
            answer = rag_system.query(question)
            print("\nAnswer:", answer)

if __name__ == "__main__":
    main()