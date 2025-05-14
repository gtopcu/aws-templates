
# https://platform.openai.com/
# https://platform.openai.com/docs/

# https://platform.openai.com/docs/overview
# https://platform.openai.com/docs/libraries

# Setting up OpenAI SDK:
# export OPENAI_API_KEY="your_api_key_here"
# pip install openai

# =================================================================================================
# Text Generation
# =================================================================================================

# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)


# =================================================================================================
# Image Analysis
# =================================================================================================

# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input=[
#         {"role": "user", "content": "what teams are playing in this image?"},
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_image",
#                     "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"
#                 }
#             ]
#         }
#     ]
# )

# print(response.output_text)