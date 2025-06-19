import json
import boto3
import os
from aws_lambda_powertools import logging

logger = logging.Logger()

# TODO
# read this from sysmgr paramstore
# Load environment variables
SENDER_EMAIL = os.environ.get("SENDER_EMAIL", "support@app.com")

def lambda_handler(event, context):
    """Handles Cognito Custom Message trigger for MFA emails."""
    logger.info(f"Received event: {json.dumps(event)}")

    # Only handle MFA-related triggers
    if event.get("triggerSource") in [
        "CustomMessage_SignUp",
        "CustomMessage_Authentication",
    ]:
        return handle_cognito_otp_email(event)

    return event  # Return unchanged for other events

def handle_cognito_otp_email(event):
    """Handles Cognito MFA verification email."""
    recipient_email = event["request"]["userAttributes"]["email"]
    verification_code = event["request"]["codeParameter"]

    subject = "Your MFA Verification Code"
    body_html = f"""
    <html>
    <body>
        <p>Your MFA verification code is: <strong>{verification_code}</strong></p>
        <p>Please enter this code to complete your login.</p>
    </body>
    </html>
    """

    send_ses_email(recipient_email, subject, body_html)

    # Modify Cognito response so it does not send a default email
    event["response"]["emailSubject"] = subject
    event["response"]["emailMessage"] = (
        f"Your MFA verification code is: {verification_code}"
    )

    return event


def send_ses_email(recipient, subject, body_html):
    """Sends an email using Amazon SES."""
    ses_client = boto3.client("ses")
    response = ses_client.send_email(
        Source=SENDER_EMAIL,
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {"Html": {"Data": body_html, "Charset": "UTF-8"}},
        },
    )
    logger.info(f"SES Email sent: {response}")
