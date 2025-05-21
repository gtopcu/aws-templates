
# https://www.youtube.com/watch?v=wLNBsr_JKuc

# pip install -U bedrock boto3 pydantic 
# pip install "instructor[bedrock]"

import json
import boto3
from enum import StrEnum
import instructor
from pydantic import BaseModel, Field

class ProgrammingParadigm(StrEnum):
    FUNCTIONAL = "Functional"
    PROCEDURAL = "Procedural"
    LOGICAL = "Logical"
    CONCURRENT = "Concurrent"
    OBJECT_ORIENTED = "Object-oriented"
    OTHER = "Other"

class ProgrammingLanguate(BaseModel):
    name: str
    release_year: int
    paradigms: list[ProgrammingParadigm]
    similar_languages: list[str] = Field(..., "Names of similar programming languages (no additional text)")
    compiled_interpreted: str


bedrock_runtime = boto3.client('bedrock-runtime', region_name='eu-west-3')
client = instructor.from_bedrock(bedrock_runtime)

response = client.chat.completions.create(
    modelId = "mistral.mistral-large-2402-v1:0",
    messages = [
        { 'role': 'user', 'content': {'text': 'Give me information about Haskell'} }
    ],
    response_model=ProgrammingLanguate

)

print(response)