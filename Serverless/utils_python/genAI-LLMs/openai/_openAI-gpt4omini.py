
# Finetuning:
# https://medium.com/@cakirduygu/openai-ile-fine-tuning-%C3%BCniversite-soru-cevap-sohbet-robotu-yaratma-99b373225f7b

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(response.choices[0].message.content) # The 2020 World Series was played at Globe Life Field in Arlington, Texas. It was a neutral site due to the COVID-19 pandemic, with no home field advantage for either team.

