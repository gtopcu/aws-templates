"""
Alternative embedding options for the RAG application
This module provides embedding functions that can be used instead of OpenAI embeddings
"""

from typing import List
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Warning: sentence-transformers not installed. SentenceTransformerEmbedding will not work.")

class SentenceTransformerEmbedding:
    """
    Embedding function using SentenceTransformer models
    These models can run completely offline
    """
    
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialize with a SentenceTransformer model
        
        Args:
            model_name: Name of the model to use (default: all-MiniLM-L6-v2)
        """
        self.model = SentenceTransformer(model_name)
    
    def __call__(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        embeddings = self.model.encode(texts)
        return embeddings.tolist()

class RandomEmbedding:
    """
    Random embedding function for testing purposes
    Not recommended for production use
    """
    
    def __init__(self, dim=384, seed=42):
        """
        Initialize with embedding dimension
        
        Args:
            dim: Dimension of the embedding vectors
            seed: Random seed for reproducibility
        """
        self.dim = dim
        np.random.seed(seed)
    
    def __call__(self, texts: List[str]) -> List[List[float]]:
        """
        Generate random embeddings for a list of texts
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of random embedding vectors
        """
        embeddings = []
        for _ in texts:
            # Generate a random vector and normalize it
            vec = np.random.randn(self.dim)
            vec = vec / np.linalg.norm(vec)
            embeddings.append(vec.tolist())
        return embeddings

# Example usage:
# from chromadb.utils import embedding_functions
# sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
# collection = client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef)