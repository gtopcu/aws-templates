
import boto3

"""
AWS Session Tokens are used for cross-account access along with AWS Identity Center 
which is used for SSO to multiple AWS accounts

Security Benefits:
1. Time-Limited Access: Session tokens expire, reducing risk if compromised
2. Least Privilege: Can assume roles with minimal necessary permissions
3. Audit Trail: AssumeRole operations are logged in CloudTrail
4. No Long-Term Credentials: Eliminates need to store permanent keys

Key Points:
- Session tokens are required when using temporary credentials
- They expire (typically 1-12 hours depending on configuration)
- Missing session token with temporary credentials results in authentication errors
- Automatically handled by AWS SDKs when using IAM roles
- Essential for secure, temporary access patterns in AWS
"""

sts_client = boto3.client('sts')

# When assuming a role, you get temporary credentials:
response = sts_client.assume_role(
    RoleArn='arn:aws:iam::123456789012:role/MyRole',
    RoleSessionName='MySession'
)

# Session Tokens in MFA:
response = sts_client.get_session_token(
    DurationSeconds=3600,
    SerialNumber='arn:aws:iam::123456789012:mfa/user',
    TokenCode='123456'  # MFA code
)

# Returns temporary credentials with session token
credentials = response['Credentials']
# These three values work together:
access_key = credentials['AccessKeyId']
secret_key = credentials['SecretAccessKey']
session_token = credentials['SessionToken']  # Required!


# Method 1: Direct client creation
s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtn...',
    aws_session_token='AQoEXAMPLE...'  # Required for temp credentials
)
s3_client.list_buckets()

# Method 2: Using session
session = boto3.Session(
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtn...',
    aws_session_token='AQoEXAMPLE...'
)
s3 = session.client('s3')