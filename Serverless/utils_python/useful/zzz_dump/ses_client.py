import os
from functools import lru_cache

import boto3
from botocore.exceptions import ClientError
from aws_lambda_powertools import logging

logger = logging.Logger()

DEFAULT_SENDER_EMAIL = "support@climatise.com"
EMAIL_CHARSET = 'UTF-8'

session = boto3.Session()
ses_client = session.client('ses', region_name='eu-west-2')

def send_email(sender: str, recipient: list[str], subject: str, body_text: str, body_html: str) -> dict | str:
    """
    Sends an email using AWS SES.

    Args:
        sender: The sender's email address.
        recipient: A list of recipient email addresses.
        subject: The subject of the email.
        body_text: The plain text body of the email.
        body_html: The HTML body of the email.

    Returns:
        The SES response if successful, an error message otherwise.
    """
    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={'ToAddresses': recipient},
            Message={
                'Subject': {'Data': subject, 'Charset': EMAIL_CHARSET},
                'Body': {
                    'Text': {'Data': body_text, 'Charset': EMAIL_CHARSET},
                    'Html': {'Data': body_html, 'Charset': EMAIL_CHARSET},
                },
            },
        )
        logger.info(f"Email sent! Message ID: {response['MessageId']}")
        return response
    except ClientError as e:
        error_message = f"Error sending email: {e.response['Error']['Message']}"
        logger.error(error_message)
        return error_message