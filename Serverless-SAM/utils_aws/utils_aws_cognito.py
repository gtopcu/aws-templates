
import boto3

cognito = boto3.client('cognito-idp')

def create_cognito_user(user_pool_id, username, name, email, temp_password, group_name):
  
  response = cognito.admin_create_user(
      UserPoolId=user_pool_id,
      Username=username,
      UserAttributes=[
          {
              'Name': 'name', 
              'Value': name
          },
      ],
      ValidationData=[
          {
              'Name': 'email',
              'Value': email
          },
      ],
      TemporaryPassword=temp_password,
      MessageAction='SUPPRESS'
  )
  if group_name:
      add_user_to_group(user_pool_id, username, group_name)

  print("User created with username: " + username)


def get_user_groups(user_pool_id, username):

  response = cognito.list_groups_for_user(
      UserPoolId=user_pool_id,
      Username=username
  )

  print(f"Groups for user {username}:")
  for group in response['Groups']:
      print(f"- {group['GroupName']}")


def add_user_to_group(user_pool_id, username, group_name):
  
  response = cognito.admin_add_user_to_group(
      UserPoolId=user_pool_id,
      Username=username, 
      GroupName=group_name
  )

  print(f"Added user {username} to group {group_name}")


def remove_user_from_group(user_pool_id, username, group_name):

  response = cognito.admin_remove_user_from_group(
      UserPoolId=user_pool_id, 
      Username=username,
      GroupName=group_name
  )

  print(f"Removed user {username} from group {group_name}")
