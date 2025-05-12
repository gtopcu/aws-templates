
# https://www.youtube.com/watch?v=4Jpltb9crPM

# pip install ollama
# ollama pull llava

import ollama

# res = ollama.chat(
#     model=llama2:13b
#     max_tokens=4096
# )

res = ollama.chat(
    model='llava',
    # model='llava:13b',
    messages=[
        {
            'role': 'user',
            'content': 'List the animals in this image separated by commas',
            'images': ['./animals.jpg']
            # 'image': 'https://example.com/image.jpg'
        }
    ]
)
print(res['message']['content'])


