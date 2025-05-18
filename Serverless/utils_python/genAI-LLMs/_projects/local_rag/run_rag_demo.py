"""
Demo script to run the complete RAG pipeline
"""

import os
import subprocess
import argparse
from sample_data_loader import create_sample_documents

def run_demo(use_sample_data=True):
    """
    Run a complete demo of the RAG application
    
    Args:
        use_sample_data: Whether to create and use sample data
    """
    # Create sample data if requested
    docs_dir = "./sample_docs"
    if use_sample_data:
        print("Creating sample documents...")
        create_sample_documents(docs_dir)
    
    # Create the vector database directory if it doesn't exist
    db_dir = "./chroma_db"
    os.makedirs(db_dir, exist_ok=True)
    
    # Index the documents
    print("\nIndexing documents...")
    subprocess.run(["python", "local-rag-app.py", "--docs_dir", docs_dir, "--db_dir", db_dir, "--index"])
    
    # Run some sample queries
    sample_queries = [
        "What are the basic data types in Python?",
        "Explain the different types of machine learning",
        "What is a vector database and how is it used in RAG?"
    ]
    
    print("\nRunning sample queries...")
    for query in sample_queries:
        print(f"\n{'='*80}\nQuery: {query}\n{'='*80}")
        subprocess.run(["python", "local-rag-app.py", "--docs_dir", docs_dir, "--db_dir", db_dir, "--query", query])
    
    print("\nDemo completed! You can now run your own queries in interactive mode:")
    print(f"python local-rag-app.py --docs_dir {docs_dir} --db_dir {db_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a demo of the RAG application")
    parser.add_argument("--no-sample-data", action="store_true", help="Don't create sample data")
    
    args = parser.parse_args()
    run_demo(use_sample_data=not args.no_sample_data)