import os

from aws_lambda_powertools import Logger
from secr.repository.dynamodb.dd_company_repository import get_company_repository

logger = Logger()


def lambda_handler(event: dict, context):
    if event["triggerSource"] != "CustomMessage_AdminCreateUser":
        logger.error(f'Triggersource unknown: {event["triggerSource"]}')
        return event

    company_id = event["request"]["userAttributes"].get("custom:company_id")
    user_email = event["request"]["userAttributes"].get("email")
    # If company_id or user_email is not found, log an error and return the event.
    if not company_id or not user_email:
        logger.error(
            f"Missing company_id or user_email: {event['request']['userAttributes']}"
        )
        return event

    environment = os.environ["ENVIRONMENT"]
    if environment == "DEV":
        domain = "climatise.dev"
    elif environment == "STAGING":
        domain = "climatise.pro"
    elif environment == "PROD":
        domain = "climatise.app"
    else:
        logger.error(f"Unknown environment: {environment}")
        return event

    try:
        company_info = get_company_repository().get_company(company_id)
    except Exception as e:
        logger.error(
            f"Company info could not be fetched for company_id: {company_id}: {str(e)}"
        )
        return event
    if not company_info.is_onboarded:
        email_subject = "Welcome to climatise - onboarding information"

        html_email_content = f"""\
      <!DOCTYPE html>
<head>
    <title>Welcome Email</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table width="100%" bgcolor="#f4f4f4" border="0" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <table align="center" bgcolor="#ffffff" style="max-width: 600px; margin: auto;" cellpadding="20" cellspacing="0">
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <img src="https://climatise.app/logo-dark.png" alt="Climatise logo" width="167" style="width: 167px; max-width: 100%; height: auto; display: block; margin: 0 auto;">
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: center; font-size: 28px; color: #333;">
                            Welcome! Let's get you onboarded
                        </td>
                    </tr>
                    <tr>
                   <td style="font-size: 16px; color: #333;">
                            <p>Hi,</p>
                            <p>Thank you for choosing Climatise to guide your company on its journey toward NetZero. You'll find all you need to get started below.</p>
    <p><b>Onboarding</b></p>
<p> Click the button below to be taken to our login page, and begin the onboarding process.</p>
                            <p style="text-align: left;">
                                <a href="https://{company_info.sub_domain}.{domain}/auth/signin?redirect=/welcome?onboarding={company_info.company_id}" style="min-width:113px; display: inline-flex; align-items: center; justify-content: center; padding: 10px 20px; background-color: #000; color: #fff; text-decoration: none; border-radius: 5px;">
                                 <style="width: auto; height: 16px; margin-right: 10px;">Onboarding
                                 </a></p>
                            If the button does not work, paste this into your browser:</p>
                            <p>https://{company_info.sub_domain}.{domain}/auth/signin?redirect=/welcome?onboarding={company_info.company_id}</p>



<p><b>Login Details</b></p>

<p style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; display: inline-block;">
  <b>Username:</b> {event["request"]["usernameParameter"]}
</p>

<p style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; display: inline-block;">
  <b>Temporary password:</b> {event["request"]["codeParameter"]}
</p>

<p><b>User Guide</p></b>

<p>For a smooth start, we recommend reading our User Guide:</p>


                            <p>
                            <a href="https://climatise.app/Climatis e%20User%20Guide%20For%20Onboarding.pdf" style="min-width: 113px; display: inline-flex; align-items: center; justify-content: center; padding: 10px 20px; background-color: #000; color: #fff; text-decoration: none; border-radius: 5px;">
                            <style="width: auto; height: 20px; margin-right: 10px;">User guide
                            </a>
                            </p>
                            <p>If the button does not work, paste this into your browser:</p>
                            <p>https://climatise.app/onboarding</p>
                        </td>
                    </tr>

       <tr>
                                <td bgcolor="#14253e" style="color: #fff; text-align: center; padding: 20px; font-size: 11px; border-top: 1px solid #ddd;">


                                    <p style="font-size: 22px; margin-top: 15px;"><b>Your climate agenda, our tech</b></p>

                                    <p>Climatise Technology Limited</p>
                                    <p>Unit 2 Horizon Business Village</p>
                                    <p>1 Brooklands Road, Weybridge, Surrey, KT13 0TJ</p>
                                    <p>Company Number 15700898</p>
                                    <p>Copyright © 2024 Climatise Technology Ltd</p>
                                </td>
         """

    elif company_info.is_onboarded:
        email_subject = "Welcome to Climatise"

        html_email_content = f"""\
<!DOCTYPE html>
<head>
    <title>Welcome Email</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table width="100%" bgcolor="#f4f4f4" border="0" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <table align="center" bgcolor="#ffffff" style="max-width: 600px; margin: auto;" cellpadding="20" cellspacing="0">
                    <tr>
                        <td align="center" style="padding: 20px;">
                            <img src="https://climatise.app/logo-dark.png" alt="Climatise logo" width="167" style="width: 167px; max-width: 100%; height: auto; display: block; margin: 0 auto;">
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: center; font-size: 28px; color: #333;">
                            Welcome! Let's get you onboarded
                        </td>
                    </tr>
                    <tr>
                   <td style="font-size: 16px; color: #333;">
                            <p>Hi,</p>
                            <p>Thank you for choosing Climatise to guide your company on its journey toward NetZero. You'll find all you need to get started below.</p>
    <p><b>Login Link</b></p>
<p> Click the button below to be taken to our login page, and begin the onboarding process.</p>
                            <p style="text-align: left;">
                                <a href="https://{company_info.sub_domain}.{domain}/auth/signin" style="min-width:113px; display: inline-flex; align-items: center; justify-content: center; padding: 10px 20px; background-color: #000; color: #fff; text-decoration: none; border-radius: 5px;">
                                 <style="width: auto; height: 16px; margin-right: 10px;">Login
                                 </a></p>
                            If the button does not work, paste this into your browser:</p>
                            <p>https://{company_info.sub_domain}.{domain}/auth/signin</p>



<p><b>Login Details</b></p>

<p style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; display: inline-block;">
  <b>Username:</b> {event["request"]["usernameParameter"]}
</p>

<p style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; display: inline-block;">
  <b>Temporary password:</b> {event["request"]["codeParameter"]}
</p>

<p><b>User Guide</p></b>

<p>For a smooth start, we recommend reading our User Guide:</p>


                            <p>
                            <a href="https://climatise.app/Climatise%20User%20Guide%20For%20Onboarding.pdf" style="min-width: 113px; display: inline-flex; align-items: center; justify-content: center; padding: 10px 20px; background-color: #000; color: #fff; text-decoration: none; border-radius: 5px;">
                            <style="width: auto; height: 20px; margin-right: 10px;">User guide
                            </a>
                            </p>
                            <p>If the button does not work, paste this into your browser:</p>
                            <p>https://climatise.com/onboarding</p>
                        </td>
                    </tr>

       <tr>
                                <td bgcolor="#14253e" style="color: #fff; text-align: center; padding: 20px; font-size: 11px; border-top: 1px solid #ddd;">


                                    <p style="font-size: 22px; margin-top: 15px;"><b>Your climate agenda, our tech</b></p>

                                    <p>Climatise Technology Limited</p>
                                    <p>Unit 2 Horizon Business Village</p>
                                    <p>1 Brooklands Road, Weybridge, Surrey, KT13 0TJ</p>
                                    <p>Company Number 15700898</p>
                                    <p>Copyright © 2024 Climatise Technology Limited Ltd</p>
                                </td>
         """

    try:
        event["response"]["emailMessage"] = html_email_content
        event["response"]["emailSubject"] = email_subject
        logger.info(
            f"Returning event to cognito. Is_onboarded = {company_info.is_onboarded}"
        )
        return event

    except Exception as e:
        logger.error(f"Failed to send email through SES: {str(e)}")
