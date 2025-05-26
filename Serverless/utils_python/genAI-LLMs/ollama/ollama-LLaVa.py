
# https://www.youtube.com/watch?v=4Jpltb9crPM

# pip install ollama
# ollama list
# ollama serve
# ollama pull llava 
# ollama pull llava:13b
# ollama pull qwen3:8b
# ollama pull llama4

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


