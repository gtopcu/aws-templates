
# Build & Deploy lambda from GitHub repo with CodeBuild: https://www.youtube.com/watch?v=AmHZxULclLQ
# Deploy lambda with CodeDeploy: https://www.youtube.com/watch?v=mYcRPKeCPXc

# put requests==2.27.1 in requirements.txt

import time
import requests

def lambda_handler(event, context):

    now = time.time()
    x = requests.get('https://w3schools.com/python/demopage.htm')
    print("Req time: " + str(time.time() - now))
    print("Status Code: " + str(x.status_code))
    #print("Headers:")
    #print(x.headers)
    #print("Body:")
    #print(x.text)
