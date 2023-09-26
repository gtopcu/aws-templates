import boto3

client = boto3.client('ssm')

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameter.html#
def get_parameter(parameter_name:str, decrypt: bool):
    return client.get_parameter(
        Name=parameter_name,
        WithDecryption=decrypt
    )
