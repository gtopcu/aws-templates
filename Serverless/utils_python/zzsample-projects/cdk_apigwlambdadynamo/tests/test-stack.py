import aws_cdk as cdk
import aws_cdk.assertions as assertions

from app import ServerlessStack

def test_dynamodb_table_created():
    app = cdk.App()
    stack = ServerlessStack(app, "ServerlessUserApiStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::DynamoDB::Table", {
        "TableName": "users",
        "KeySchema": [
            {"AttributeName": "id", "KeyType": "HASH"},
            {"AttributeName": "name", "KeyType": "RANGE"}
        ],
        "AttributeDefinitions": [
            {"AttributeName": "id", "AttributeType": "S"},
            {"AttributeName": "name", "AttributeType": "S"}
        ],
        "BillingMode": "PAY_PER_REQUEST"
    })

def test_lambda_function_created():
    app = cdk.App()
    stack = ServerlessStack(app, "ServerlessUserApiStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
        "Handler": "index.lambda_handler",
        "Runtime": "python3.14",
        "Environment": {
            "Variables": {
                "TABLE_NAME": "users"
            }
        }
    })

def test_api_gateway_created():
    app = cdk.App()
    stack = ServerlessStack(app, "ServerlessUserApiStack")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::ApiGatewayV2::Api", 1)
    template.resource_count_is("AWS::ApiGatewayV2::Route", 1)
    template.resource_count_is("AWS::ApiGatewayV2::Integration", 1)