import os
import json
import boto3

# queue_url = os.getenv("QUEUE_URL")
# session = boto3.session.Session()
# client = session.client("sqs")

# Receive and print SQS message
def handler(event, context): 
    # print(event)
    # print(context)

    # response = client.receive_message(
    #     QueueUrl=queue_url,
    #     AttributeNames=[
    #         'SentTimestamp'
    #     ],
    #     MaxNumberOfMessages=1,
    #     MessageAttributeNames=[
    #         'All'
    #     ],
    #     VisibilityTimeout=0,
    #     WaitTimeSeconds=0
    # )
    # print(response)
    # if "Messages" in response:
    #     message = response["Messages"][0]
    #     receipt_handle = message["ReceiptHandle"]
    #     client.delete_message(
    #         QueueUrl=queue_url,
    #         ReceiptHandle=receipt_handle
    #     )
    #     print("Received and deleted message: %s" % message)
    # else:
    #     print("No messages to process")
    return event["Records"][0]["body"]
    # return response["Messages"][0]["Body"]
    

    # output = []
    # for record in event["Records"]:
    #     #message = your_business_logic(record)
    #     output.append(message)
    # for message in output:
    #     response = client.send_message(json.dumps(output))
    # return response