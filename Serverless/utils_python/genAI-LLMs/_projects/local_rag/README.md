
# Local RAG Application with OpenAI
This is a Retrieval-Augmented Generation (RAG) application that runs completely locally without requiring internet connection.
It uses OpenAI models for local inference and ChromaDB as the vector database

## Components
- local-rag-app.py: The main application that implements the RAG system
- sample_data_loader.py: A utility to create sample documents for testing
- run_rag_demo.py: A demo script to run the complete pipeline
- alternative_embeddings.py: Options for embedding generation without OpenAI
- requirements.txt: Dependencies needed for the application

## Prerequisites
1. Install [Ollama](https://ollama.com/download/) to run OpenAI models locally
2. Pull the o4-mini model: `ollama pull o4-mini`
3. Install Python dependencies: `pip install -r requirements.txt`

## Option 1- Running the demo script
`python run_rag_demo.py`

This will:
- Create sample documents about Python, Machine Learning, and Vector Databases
- Index these documents in a ChromaDB vector database
- Run sample queries to demonstrate the RAG system

## Option 2- Indexing your documents
1. Prepare a directory with text documents you want to index
2. Run the indexing process:
   `python local-rag-app.py --docs_dir /path/to/your/documents --index`
3. Start querying:
   `python local-rag-app.py --docs_dir /path/to/your/documents --query "Your question here"`

   Or use interactive mode:
   `python local-rag-app.py --docs_dir /path/to/your/documents`

## How It Works
1. **Document Processing**: Text documents are loaded and split into chunks
2. **Embedding Generation**: Each chunk is converted to an embedding vector using the local model
3. **Vector Storage**: Embeddings are stored in a ChromaDB database
4. **Retrieval**: When a query is received, similar chunks are retrieved from the database
5. **Generation**: The local OpenAI model generates an answer based on the retrieved context

## Customization
You can modify the following parameters in the code:
- `chunk_size`: Size of text chunks (default: 1000)
- `chunk_overlap`: Overlap between chunks (default: 200)
- `top_k`: Number of chunks to retrieve for each query (default: 3)

## Notes
- This application assumes you have Ollama running locally on the default port (11434)
- For better performance, consider using a more powerful model if your hardware supports it
- The vector database is stored in the `./chroma_db` directory by default

## Alternative Embeddings
If you prefer not to use OpenAI for embeddings, modify the LocalRAGSystem class initialization 
in local-rag-app.py with these alternatives:

1. **SentenceTransformer**: Uses the sentence-transformers library for local embedding generation:
`from alternative_embeddings import SentenceTransformerEmbedding`
`embedding_function = SentenceTransformerEmbedding(model_name="all-MiniLM-L6-v2")`
2. **RandomEmbedding**: For testing purposes only (not recommended for production)