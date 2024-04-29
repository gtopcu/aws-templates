
# https://www.youtube.com/watch?v=y_VtqdK6io0

# pip install openai pandas
# .ipynb

import openai
import pandas as pd
import json

df = pd.read_excel("input.xlsx") # Prompt Title Description Tags
df.head()

df["response_strings"] = df.apply(lambda row: f"""Title: {row["Title"]}
Description: {row["Description"]}
Tags: {row["Tags"]}""", axis=1)
df
df.response_strings.values[0]

system_prompt = "You are an assistant. Given a rough video description, you come up with a YouTube title, description and tags"

all_conversations = []
for idx, row in df.iterrows():
    all_conversations.append({"messages": [ {"role": "system", "content": system_prompt},
                                            {"role": "user", "content": row["Prompt"]},
                                            {"role": "assistant", "content": row["response_strings"]}]})
all_conversations[0]

with open('instances.jsonl', 'w') as f:
    for conversation in all_conversations:
        f.write(json.dumps(conversation) + '\n') 

client = openai.OpenAI(api_key="<YOUR_OpenAI_API_KEY>")
with open('instances.jsonl', 'rb') as f:
    response = client.files.create(file=f, purpose="fine-tune")

response
file_id = response["id"]
# file_id = "file-xxxx"

response = client.fine_tunes.create(training_file=file_id, model="gpt-3.5-turbo")
response
job_id = response["id"]

# client.fine_tuning.jobs.cancel(job_id)
client.fine_tuning.jobs.list(limit=10)
client.fine_tuning.jobs.retrieve(job_id)
model_id = client.fine_tuning.jobs.retrieve(job_id)["fine_tuned_model"] # ft:gpt-3.5-turbo:user:xxxxx

# completion = client.chat.completions.create(model=model_id, prompt="What is the title of the video?")
completion = client.chat.completions.create(model=model_id, messages=[{"role": "user", "content": "What is the title of the video?"}])
completion.choices[0].message.content








