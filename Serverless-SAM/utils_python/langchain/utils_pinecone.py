
# https://www.youtube.com/watch?v=aywZrzNaKjs

"""
python3 -m venv venv
source venv/bin/activate

pip install python-dotenv 
pip install langchain
pip install pinecone-client
"""

import os
import os
from dotenv import load_dotenv, find_dotenv
from pinecone import Pinecone, ServerlessSpec, PodSpec

if not load_dotenv(find_dotenv()):
    raise Exception("Failed to load .env file")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

print(pc.list_collections())
print(pc.list_indexes())

# if PINECONE_INDEX not in pc.list_indexes().names():
#     pc.create_index(
#         name=PINECONE_INDEX, 
#         dimension=1536, 
#         metric='euclidean', # {"cosine", "dotproduct", "euclidean"}
#         spec= PodSpec( # ServerlessSpec
#             #     cloud='aws',          # 'gcp'
#             #     region='us-west-2'    # 'us-central1'
#         )
#     )

index.upsert(
    vectors=[
        {
            "id": "vec1", 
            "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec2", 
            "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], 
            "metadata": {"genre": "action"}
        }, {
            "id": "vec3", 
            "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec4", 
            "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], 
            "metadata": {"genre": "action"}
        }
    ],
    namespace= "ns1"
)

index.query(
    namespace="ns1",
    vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    top_k=2,
    include_values=True,
    include_metadata=True,
    filter={"genre": {"$eq": "action"}}
)



