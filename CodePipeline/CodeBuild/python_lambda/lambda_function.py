
# https://www.youtube.com/watch?v=AmHZxULclLQ

# put pandas==1.2.1 in requirements.txt

import json
#import pandas as pd

def lambda_handler(event, context):

    # d = { "col1":[1,2], "col2":[3,4] }
    # df = pd.DataFrame(data=d)
    # print(df)
    # print("Done v1.0!")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda v1.6!')
    }
