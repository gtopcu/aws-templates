
# https://platform.openai.com/

import openai

system_prompt = "You are a helpful assistant."
prompt = "What is the capital of France?"

response = openai.Completion.create(
        engine="davinci",
        prompt=f"{system_prompt}\n{prompt}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
print(response.choices[0].text)

client = openai.OpenAI(api_key="<YOUR_OpenAI_API_KEY>")
response = client.chat(
    system_prompt=system_prompt,
    messages=[prompt]
)
print(response.choices[0].message.content)