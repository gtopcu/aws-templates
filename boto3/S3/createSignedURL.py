import logging
import boto3
import botocore
from botocore.exceptions import ClientError

# !!!! GIVE S3 ACCESS TO LAMBDA !!!!!

def create_presigned_url(region, bucket_name, object_name, expiration):
    # Choose AWS CLI profile, If not mentioned, it would take default
    # boto3.setup_default_session(profile_name='personal')
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3',region_name=region,config=boto3.session.Config(signature_version='s3v4',))
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        logging.error("Error generating pre-signed S3 URL: " + str(e))
        raise e
    # The response contains the presigned URL
    #print(response)
    return response

create_presigned_url("us-east-2", '00-infraops-testbucket','short.mp4', 600)

https://00-infraops-testbucket.s3.amazonaws.com/short.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIARPTIMKGILKY7NWMX%2F20220927%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20220927T175258Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLWVhc3QtMiJGMEQCICKvm6lwf48YnZkEUzGvFMHBrPf1jbmA8Wi%2BrTMaA%2BhhAiAe3nzIJSR73izVEsTcMrt9rG0VpCH5rNq92F8rCaHSMyr0AggbEAIaDDEwMjIyNDM4NDQwMCIMA%2FLwdspqppfUcWo2KtECYW6Cneh8dJ1B1XKwmJnoC%2BEyWpx6MM59sh0JcaGTDu%2B%2B58hLqZ1swE0jzbHTecO140fDQ11Ak%2BIzJGNAFsJGANqqWtaPVxouf%2BoGI38wHnyVPagrQsljPDTwTHRSIlUK0ZDpA1MKl2o%2BeOlItNhTBIp%2BxfmVj6yc7naeNo5yVbhguo4T8%2BRj8OtJcjV4uF0uvgacI%2B%2BLKPL8nZQrxjD%2FqS2QW2XMAhK3ouW05AObur3F1r8oo%2B6oiMIFCmovIVxgKYxTrHUMg8zcuNi%2BXodepsd9kgkHA4nF5Rt4%2BsYIk%2BZUjL8AAh6RI88ooxclgDM4GBctd3aBFSWqgGzWojgPJqyFhE7kGRcpYO1OBqLq%2FGzvsyFLV2%2BrUnAu9rX%2FbffWwsOCyZ4nV8QTxRZd8PF74t5JBkaXT7WYlN8eZh1wnNypM%2F3aL%2FIE%2F6RlNl82Jx1ORzD58MyZBjqfAX2i5BD04GxtoTk41ivWgeEhi0dFvXi0RIYx1lshS9BmH4PfHpGRRLBMoSf%2FrmylDjVLeN5zE1XMFg%2BRKDBe658G2LY%2F8bJSC1UyTSMJ076EaasZb04Q9EfHuh80NX4E%2Bh78sLG9BigFFsLboyd2Qvyue%2Fb2H4iD9jhtt%2BYqywOZx0vNDaxS0ZEPRkZxgwirVTW6hhN6DUmBbWOWNCRnPA%3D%3D&X-Amz-Signature=f748e8d506aecb8c1812dfc8a8be9ba583a8c6ba14162e7f64d9176eb9611b64



