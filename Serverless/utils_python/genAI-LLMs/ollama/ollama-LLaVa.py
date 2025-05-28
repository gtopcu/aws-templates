
# https://www.youtube.com/watch?v=4Jpltb9crPM
# https://ollama.com/download

# pip install ollama
# ollama -v | -h | --help
# ollama list
# ollama run llava:13b (auto-pull)
# ollama ps
# ollama serve
# ollama stop llama4
# ollama pull qwen3:8b
# ollama push llama4

#  create      Create a model from a Modelfile
#  show        Show information for a model
#  cp          Copy a model
#  rm          Remove a model


# ollama run llama4

# Embedding model: 
# ollama pull mxbai-embed-large

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


