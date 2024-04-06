
# https://www.philschmid.de/sagemaker-awq-medusa

import json
import os
from huggingface_hub import snapshot_download
from sagemaker.s3 import S3Uploader

from sagemaker.huggingface import get_huggingface_llm_image_uri

# retrieve the llm image uri
llm_image = get_huggingface_llm_image_uri(
  "huggingface",
  version="1.4.2"
)
# print ecr image uri
print(f"llm image uri: {llm_image}")

tmp_dir = "./tmp"
medusa_repository = "text-generation-inference/Mixtral-8x7B-Instruct-v0.1-medusa" # Medusa model
# https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ/discussions/6
llm_repository = "ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ" # AWQ LLM model

snapshot_download(repo_id=medusa_repository, local_dir=tmp_dir)
snapshot_download(repo_id=llm_repository, local_dir=os.path.join(tmp_dir, "llm"),ignore_patterns="*.bin")

# rewrite meudsa base model value
with open(os.path.join(tmp_dir, "config.json"), "r") as f:
    data = json.load(f)
    data["base_model_name_or_path"] = "/opt/ml/model/llm/" # path to llm model in side Amazon SageMaker
with open(os.path.join(tmp_dir, "config.json"), "w") as f_out:
    json.dump(data, indent=2, fp=f_out)

# upload the model to s3
s3_path = S3Uploader.upload(
    local_path=tmp_dir,
    desired_s3_uri=f"s3://{sess.default_bucket()}/medusa/mixtral"
)


import json
from sagemaker.huggingface import HuggingFaceModel

# sagemaker config
instance_type = "ml.g5.12xlarge"
number_of_gpu = 4
health_check_timeout = 300

# Define Model and Endpoint configuration parameter
config = {
  'HF_MODEL_ID': "/opt/ml/model", # path to where sagemaker stores the model
  'SM_NUM_GPUS': json.dumps(number_of_gpu), # Number of GPU used per replica
  'MAX_INPUT_LENGTH': json.dumps(8000),  # Max length of input text
  'MAX_BATCH_PREFILL_TOKENS': json.dumps(16384),  # Number of tokens for the prefill operation.
  'MAX_TOTAL_TOKENS': json.dumps(16384),  # Max length of the generation (including input text)
  'QUANTIZE': "awq" # Quantization method
}

# create HuggingFaceModel with the image uri
llm_model = HuggingFaceModel(
  role=role,
  # path to s3 bucket with model, we are not using a compressed model
  model_data={'S3DataSource':{'S3Uri': s3_path + "/",'S3DataType': 'S3Prefix','CompressionType': 'None'}},
  image_uri=llm_image,
  env=config
)

# Deploy model to an endpoint
# https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.model.Model.deploy
llm = llm_model.deploy(
  initial_instance_count=1,
  instance_type=instance_type,
  container_startup_health_check_timeout=health_check_timeout, # 10 minutes to be able to load the model
)


from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ")

# Prompt to generate
messages = [
    { "role": "user", "content": "How can i make a good american cheese cake? Explain it step-by-step and include time estimates." },
]

# Generation arguments
payload = {
    "do_sample": True,
    "top_p": 0.6,
    "temperature": 0.9,
    "top_k": 50,
    "max_new_tokens": 1024,
    "repetition_penalty": 1.03,
    "return_full_text": False,
    "stop": ["</s>"]
}

chat = llm.predict({
  "inputs":tok.apply_chat_template(messages,tokenize=False,add_generation_prompt=True), # convert messages to model input
  "parameters":payload
})

print(chat[0]["generated_text"])

llm.delete_model()
llm.delete_endpoint()