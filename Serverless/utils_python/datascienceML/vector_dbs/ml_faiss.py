
# https://faiss.ai/index.html
# https://www.youtube.com/watch?v=SkY2u4UUr6M

# Only install one:
# conda install -c pytorch faiss-cpu
# conda install -c pytorch faiss-gpu -> provides CUDA-enabled indices:


# from langchain.vectorstores.faiss import FAISS
from langchain.vectorstores import FAISS

text_chunks = ["hello world", "this is a test"]
embeddings = "awstitantext/googleembeddings"
faiss = FAISS.from_texts(text_chunks, embeddings=embeddings)
faiss.save_local("faiss_index")
