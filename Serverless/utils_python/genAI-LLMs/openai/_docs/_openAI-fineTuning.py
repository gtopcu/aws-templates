


from openai import OpenAI
client = OpenAI()


# https://platform.openai.com/docs/guides/fine-tuning-best-practices
# hyperparameter tuning for fine-tuning
# client.fine_tuning.jobs.create(
#     training_file="file-abc123",
#     model="gpt-4o-mini-2024-07-18",
#     method={
#         "type": "supervised",
#         "supervised": {
#             "hyperparameters": {"n_epochs": 2},
#         },
#     },
# )