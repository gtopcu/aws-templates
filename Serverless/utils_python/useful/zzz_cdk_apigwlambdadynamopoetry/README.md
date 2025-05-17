AWS Serverless User API
This project creates a serverless application using AWS CDK for Python that includes:

- API Gateway (HTTP API) with proxy integration to a Lambda function
- Lambda function with AWS Lambda Powertools for logging, tracing and API handling
- DynamoDB table for storing user data 

Project Structure
aws-serverless-user-api/
├── app.py                # Main CDK stack definition
├── lambda/
│   ├── app.py            # Lambda function code with Powertools
│   └── requirements.txt  # Lambda dependencies
├── tests/
│   ├── test_stack.py     # CDK stack tests
│   └── test_lambda.py    # Lambda function tests
├── requirements.txt      # Project dependencies
└── README.md             # This file

Prerequisites
AWS CDK v2
Python 3.13 or higher
AWS CLI configured with appropriate credentials

Setup
Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Bootstrap your AWS account for CDK (if not already done): 
cdk bootstrap

Deployment
Deploy the application to your AWS account: 
cdk deploy
This will create all the required resources and output the API Gateway URL

API Endpoints
The API provides the following endpoints:

GET /users - List all users (DynamoDB Scan)
GET /users/{id} - Get users by ID (DynamoDB Query)
Optional query param: name - Get specific user (DynamoDB GetItem)
POST /users - Create a new user (DynamoDB PutItem)
PUT /users/{id} - Update a user (DynamoDB UpdateItem)
DELETE /users/{id}?name={name} - Delete a user (DynamoDB DeleteItem)

Request and Response Examples

List Users
GET /users
Response:
{
  "statusCode": 200,
  "body": [
    {
      "id": "user1",
      "name": "John Doe",
      "email": "john@example.com"
    },
    {
      "id": "user2",
      "name": "Jane Smith",
      "email": "jane@example.com"
    }
  ]
}

Get User by ID
GET /users/user1
Response:
{
  "statusCode": 200,
  "body": [
    {
      "id": "user1",
      "name": "John Doe",
      "email": "john@example.com"
    }
  ]
}

Create User
POST /users
Content-Type: application/json
{
  "id": "user3",
  "name": "Bob Johnson",
  "email": "bob@example.com"
}
Response:
{
  "statusCode": 201,
  "body": {
    "id": "user3",
    "name": "Bob Johnson",
    "email": "bob@example.com"
  }
}

Update User
PUT /users/user1
Content-Type: application/json
{
  "name": "John Doe",
  "email": "john.updated@example.com"
}
Response:
{
  "statusCode": 200,
  "body": {
    "id": "user1",
    "name": "John Doe",
    "email": "john.updated@example.com"
  }
}

Delete User
DELETE /users/user1?name=John%20Doe
Response:
{
  "statusCode": 204,
  "body": ""
}

Running Tests
Run the tests with pytest:
pytest

Cleanup
To remove all resources:
cdk destroy

Notes
For production use, consider adding additional security measures like authentication and authorization.
The current setup uses removal policy set to DESTROY for the DynamoDB table, which means the table will be deleted when you destroy the stack. For production, change this to RETAIN to preserve your data.
