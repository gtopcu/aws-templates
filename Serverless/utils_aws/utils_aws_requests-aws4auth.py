
# https://pypi.org/project/requests-aws4auth/

import requests
from requests_aws4auth import AWS4Auth
from botocore.session import Session

def s3_list_buckets():
    endpoint = 'http://s3-eu-west-1.amazonaws.com'
    auth = AWS4Auth('<ACCESS ID>', '<ACCESS KEY>', 'eu-west-1', 's3')
    response = requests.get(endpoint, auth=auth)
    print(response.text)

def get_STS_Token():
    auth = AWS4Auth('<ACCESS ID>', '<ACCESS KEY>', 
                     'eu-west-1', 's3', session_token='<SESSION TOKEN>')
    
def get_STS_AutoRefreshingToken():
    credentials = Session().get_credentials()
    auth = AWS4Auth(region='eu-west-1', service='es',
                    refreshable_credentials=credentials)    