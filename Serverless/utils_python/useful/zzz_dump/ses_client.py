import os
from functools import lru_cache

import boto3
from aws_lambda_powertools import logging


logger = logging.Logger()

# TODO 
# read this from sysmgr parameter store
SENDER_EMAIL = "support@app.com"

class EmailRequest:
    source_id: str
    company_id: str


def send_email(email_request: EmailRequest) -> None:

    # cc_emails = cognitoHandler().get_moderator_user_emails()
    cc_emails = ["gtopcu@mgmail.com"]

    if not cc_emails:
        logger.error("No admin users found")
        return

    res = get_ses_client().send_email(
        Source=SENDER_EMAIL,
        Destination={
            "CcAddresses": cc_emails,
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": f"""
    The following file has been uploaded for company {email_request.company_id}:
        SourceId:    {email_request.source_id}
        S3 Location: <a class="ulink" href="{get_s3_link(email_request.bucket_key)}" target="_blank">{email_request.bucket_key}</a>

    Note: The S3 location is within the data bucket: {os.environ['DATA_BUCKET_NAME']}
    """,
                },
            },
            "Subject": {
                "Charset": "UTF-8",
                "Data": f"New file upload notification: {email_request.company_id}:{email_request.source_id}",
            },
        },
    )
    logger.info(f"Sent email: {res}")


def get_s3_link(bucket_key: str) -> str:
    return f"""https://eu-west-2.console.aws.amazon.com/s3/object/{os.environ['DATA_BUCKET_NAME']}?region=eu-west-2&bucketType=general&prefix={bucket_key}"""


@lru_cache
def get_ses_client():
    return boto3.client("ses")
