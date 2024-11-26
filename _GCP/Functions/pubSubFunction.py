
import base64
from cloudevents.http import CloudEvent

import functions_framework

@functions_framework.cloud_event
def subscribe(cloud_event: CloudEvent) -> None:
    print(
        "Hello, " + base64.b64decode(cloud_event.data["message"]["data"]).decode() + "!"
    )

# import functions_framework
# import base64
# import json

# @functions_framework.cloud_event
# def process_pubsub_message(cloud_event):
#     if cloud_event.data:
#         pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode()
#         print(f"Received message: {pubsub_message}")
#        
#         try:
#             message_json = json.loads(pubsub_message)
#             print(f"Processed JSON: {message_json}")
#         except json.JSONDecodeError:
#             print("Message is not JSON format")           
#     return "OK"