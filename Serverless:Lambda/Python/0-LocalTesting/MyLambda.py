import json
import boto3
import os
import logging
from pymediainfo import MediaInfo

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('ssm')

# Required setup
# 1. Set env environment variable to dev/test/prod
# 2. Create & attach mediaInfo layer (https://aws.amazon.com/blogs/media/running-mediainfo-as-an-aws-lambda-function/)
# 3. Set Parameter Store Params:
#   /{env}/guardrails/max_size

env = "dev" #os.getenv("env")
if env is None:
    raise Exception("Environment not set")

#Get max object size config from SSM
try: 
    maxSize = client.get_parameter(
            Name=f'/{env}/guardrails/max_size',
            WithDecryption=False
        )["Parameter"]["Value"]
except Exception as e:
    raise Exception("Max size param not set in SSM")
paramMaxSize = int(maxSize)
logging.info("Max object size: " + str(paramMaxSize))

class MyLambda:

    @staticmethod
    def lambda_handler(event, context):
        
        #print(event)
        #print(context)
        logging.info("In Lambda")

        logging.info("Checking object size")
        MyLambda._checkObjectSize(event)
        
        return {
            'statusCode': 200,
            'body': "Checks successfull"
            #json.dumps(event)
        }

    @staticmethod
    def _checkObjectSize(event:dict) -> None:
        
        #Get object size from S3 event 
        s3_obj_size = int(event["Records"][0]["s3"]["object"]["size"])
        logging.info("Object Size: " + str(s3_obj_size))
        
        if s3_obj_size > paramMaxSize:
            raise Exception("Object exceeds max allowed size")


if __name__ == "__main__":
    #os.system("export env=dev")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())
    with open("./event.json", "r") as fh:
        eventJson = json.loads(fh.read())
        #lambda_handler(eventJson, None)
        MyLambda.lambda_handler(eventJson, None)




https://00-infraops-testbucket.s3.amazonaws.com/short.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIARPTIMKGIBUFUDQNQ%2F20220927%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20220927T172848Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMiJGMEQCIEEXen%2BLl8n%2F7OThpjWBpbOed59Zd8lrXKN45ieHvP8tAiA47UViizKRApzQFg2%2FpjgPqW0%2F0bKj1FkpOXLpYjmv6ir0AggbEAIaDDEwMjIyNDM4NDQwMCIMqkeJB8wYufQae0VAKtECu8B0ynKa%2BQ3crvffQExFLmssFaM3oUcUugWcLK6LGT0nIV%2FD%2BpL0bq6FMNszKQ2ev8rvpVws7sFR9%2Fum6Nn7vjDnlylhHt8mo5%2BFThO6EAbfaFJ0GLrbnVfEjER1MmBKgOZAk5hKMghzjp%2Ffv4rPclHen%2FlZlz2egynnSdaaqvOfFEsNuJybsG%2BIJBfnP%2Ft0kdoadrgKFVz1Jvo8LMLn0xcZ81bko026l7IpBnaRdjAp8i3GT87CH8evQGgk45Hrw6dBpk0ufNQKlE9LviNsd9Ip6VulHpqFAs2Y%2FeKDL2mhPHy9nSzXM5JsZpIehMbUSoiAH%2BNFWjIzhxacY7pd6znzgrzKLJ7oS7fuAIvDgmeGwEFKAVtLPIJZdObmxkAXJNmcDDlgXDatNz3URIA0jODtMFVpBVUBk5b8Uio6p8zptnw0jBCCI4ZN3698pMwaqjDQ5cyZBjqfASXOZmvWxAN0wpPA%2BwPPyiHK08L%2FaJtKLMypFJlm8MGgZxv%2F7o%2BuPNF%2FRW6xX9qx3n2oo7OhWwysqlepDynr2VGO4wA2nNRAIRKY4YGPWg11PRUncCfMSmfmUaO%2B4oSrmuxx%2FSiVEIBHcNbjtfnI8IyBLltWAS1D4M7bvYhHVOeYmhqauijHHW%2Bt%2FKqPNoUpcHbyPWMEucb3EwRtpZG2CQ%3D%3D&X-Amz-Signature=7c05ec496c285635dc2e938ab08ca4ca1dae60ced20dc8fd5f71dcec8b058177




