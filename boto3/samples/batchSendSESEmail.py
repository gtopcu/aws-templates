import os
import sys
import datetime
import json
import random
import boto3
from requests import NullHandler

os.system("clear")
"""
print(os.environ)
txt = input()
print("hi")
print(round(2.2))
print(datetime.datetime.now().isoformat())
s3 = boto3.resource("s3")
"""

from_address = "info@spiky.ai"
to_addresses = ["gtopcu@gmail.com"]
subject = "Test email"
message_text = "Have a great day!"

print("Sending simple email")
email_client = boto3.client('ses')
charset = 'UTF-8'

body = {}
body["Text"] = {
    'Charset': charset,
    'Data': message_text
}

for i in range(0, 1000):
    response = email_client.send_email(
        Source=from_address,
        Destination={'ToAddresses':to_addresses},
        Message={
            'Subject': {
                'Charset': charset,
                'Data': subject,
            },
            'Body': body
        },
        ReplyToAddresses=[]
    )
    print(response)

