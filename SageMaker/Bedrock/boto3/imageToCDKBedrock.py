
# https://letsmake.cloud/transforming-diagrams-into-code

import os
import base64
import json
import io
from PIL import Image
import streamlit as st

import boto3
import botocore.exceptions.ClientError

bedrock = boto3.client(region_name="us-east-1", service_name='bedrock-runtime')

def image_base64_encoder(image_name):
    open_image = Image.open(image_name)
    image_bytes = io.BytesIO()
    open_image.save(image_bytes, format=open_image.format)
    image_bytes = image_bytes.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    file_type = f"image/{open_image.format.lower()}"
    return file_type, image_base64

def image_to_text(image_name, text) -> str:
    file_type, image_base64 = image_base64_encoder(image_name)
    system_prompt = """Describe every detail you can about this image, be extremely thorough and detail even the most minute aspects of the image. 

    If a more specific question is presented by the user, make sure to prioritize that answer.
    """
    if text == "":
        text = "Use the system prompt"
    prompt = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 10000,
        "temperature": 0.5,
        "system": system_prompt,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": file_type,
                            "data": image_base64
                        }
                    },
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ]
    }
    json_prompt = json.dumps(prompt)
    response = bedrock.invoke_model(body=json_prompt, modelId="anthropic.claude-3-sonnet-20240229-v1:0",
                                    accept="application/json", contentType="application/json")
    response_body = json.loads(response.get('body').read())
    llm_output = response_body['content'][0]['text']
    return llm_output

st.title(f""":rainbow[Architecture Diagrams with Amazon Bedrock]""")
st.header(f""":rainbow[Diagram Analysis (Claude 3 Sonnet)]""")
with st.container():
    st.subheader('Image File Upload:')
    File = st.file_uploader('Upload an Image', type=["png", "jpg", "jpeg"], key="diag")
    text = st.text_input("OPTIONAL: Do you have a question about the image? Or about anything in general?")
    result1 = st.button("Describe Diagram")
    result2 = st.button("Generate CDK Code")

if result1:
    input_text = "You are a AWS solution architect. The image provided is an architecture diagram. Explain the technical data flow in detail. Do not use preambles."
elif result2:
    input_text = "You are a AWS solution architect. The image provided is an architecture diagram. Provide cdk python code to implement using aws-cdk-lib in detail."

st.write(image_to_text(File.name, input_text))

# streamlit run app.py