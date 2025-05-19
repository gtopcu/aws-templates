"""
Sample data loader to create test documents for the RAG application
"""

import os
import argparse

def create_sample_documents(output_dir):
    """
    Create sample text documents for testing the RAG application
    
    Args:
        output_dir: Directory to save the sample documents
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Sample documents
    documents = [
        {
            "filename": "python_basics.txt",
            "content": """# Python Basics

Python is a high-level, interpreted programming language known for its readability and simplicity.

## Key Features
- Easy to learn and use
- Interpreted language
- Dynamically typed
- Object-oriented
- Extensive standard library

## Basic Syntax
Python uses indentation to define code blocks:

```python
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
```

## Data Types
- Integers: `x = 5`
- Floats: `y = 3.14`
- Strings: `name = "Python"`
- Lists: `numbers = [1, 2, 3]`
- Dictionaries: `person = {"name": "John", "age": 30}`
- Tuples: `coordinates = (10, 20)`
- Sets: `unique_numbers = {1, 2, 3}`
- Booleans: `is_active = True`
"""
        },
        {
            "filename": "machine_learning_intro.txt",
            "content": """# Introduction to Machine Learning

Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data.

## Types of Machine Learning
1. **Supervised Learning**: The algorithm learns from labeled training data
   - Classification: Predicting a category (e.g., spam detection)
   - Regression: Predicting a continuous value (e.g., house prices)

2. **Unsupervised Learning**: The algorithm learns patterns from unlabeled data
   - Clustering: Grouping similar data points (e.g., customer segmentation)
   - Dimensionality Reduction: Reducing the number of variables

3. **Reinforcement Learning**: The algorithm learns by interacting with an environment

## Common Algorithms
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines
- Neural Networks
- K-means Clustering

## Evaluation Metrics
- Accuracy
- Precision and Recall
- F1 Score
- ROC Curve and AUC
- Mean Squared Error (MSE)
"""
        },
        {
            "filename": "vector_databases.txt",
            "content": """# Vector Databases

Vector databases are specialized database systems designed to store and query vector embeddings efficiently.

## What are Vector Embeddings?
Vector embeddings are numerical representations of data (text, images, audio) in a high-dimensional space.
These embeddings capture semantic meaning, allowing for similarity searches.

## Key Features of Vector Databases
1. **Similarity Search**: Find vectors that are similar to a query vector
2. **Indexing**: Efficient data structures for fast retrieval
3. **Scalability**: Handle millions or billions of vectors
4. **Filtering**: Combine vector search with metadata filtering

## Popular Vector Databases
- Chroma
- FAISS
- Milvus
- Pinecone
- Weaviate
- Qdrant

## Use Cases
- Semantic search
- Recommendation systems
- Image similarity
- Anomaly detection
- Retrieval Augmented Generation (RAG)
"""
        }
    ]
    
    # Write the documents to files
    for doc in documents:
        with open(os.path.join(output_dir, doc["filename"]), "w", encoding="utf-8") as f:
            f.write(doc["content"])
    
    print(f"Created {len(documents)} sample documents in {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create sample documents for RAG testing")
    parser.add_argument("--output_dir", type=str, default="./sample_docs", help="Directory to save sample documents")
    
    args = parser.parse_args()
    create_sample_documents(args.output_dir)