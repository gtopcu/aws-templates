import json
import boto3

def validate_arguments(args):
  for arg in args:
    if not arg or len(arg) < 1:
      return False
  return True

def sendTemplatedEmail(from_address, to_addresses, template_name, template_data, reply_to_addresses):
  print("Sending email with template")
  email_client = boto3.client('ses')
  response = email_client.send_templated_email(
    Source=from_address,
    Destination={
        'ToAddresses': to_addresses,
    },
    ReplyToAddresses=reply_to_addresses if reply_to_addresses else [],
    Template=template_name,
    TemplateData=template_data
  )
  return response


def sendSimpleEmail(from_address, to_addresses, subject, message_text, message_html, reply_to_addresses):
  print("Sending simple email")
  email_client = boto3.client('ses')
  charset = 'UTF-8'

  body = {}
  if message_html:
    body["Html"] = {
        'Charset': charset,
        'Data': message_html,
    }
  else:
    body["Text"] = {
        'Charset': charset,
        'Data': message_text if message_text else "",
    }

  response = email_client.send_email(
    Source=from_address,
    Destination={'ToAddresses':to_addresses},
    Message={
        'Subject': {
            'Charset': charset,
            'Data': subject,
        },
        'Body': body
    },
    ReplyToAddresses=reply_to_addresses if reply_to_addresses else []
  )
  return response
  
def lambda_handler(event, context):
    status_code = 200
    response_message = 'Successfully sent email!'

    try:
      from_address = event.get("fromAddress")
      to_addresses = event.get("toAddresses")
      subject = event.get("subject")
      message_text = event.get("messageText")
      message_html = event.get("messageHtml")
      reply_to_addresses = event.get("replyToAddresses")

      template_name = event.get("templateName")
      template_data = event.get("templateData")
      
      simple_email_required_arguments = [
       from_address, to_addresses, subject 
      ]

      template_email_required_arguments = [
       from_address, to_addresses,template_name, template_data
      ]

      if validate_arguments(template_email_required_arguments):
        result = sendTemplatedEmail(from_address, to_addresses, template_name, template_data, reply_to_addresses)
        print(result)
      
      elif validate_arguments(simple_email_required_arguments):
        result = sendSimpleEmail(from_address, to_addresses, subject, message_text, message_html, reply_to_addresses)
        print(result)

      else:
        print("Required arguments not found")
        status_code = 400
        response_message = "Required arguments not found"
        

    except Exception as e:
      print(e)
      raise e
   
    return {
      'statusCode': status_code,
      'body': json.dumps({'message': response_message}),
    }