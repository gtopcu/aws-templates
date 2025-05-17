#!/usr/bin/env python3

# pip install aws-cdk-lib 
# pip install aws-cdk.aws-lambda-python-alpha
# pip install aws-lambda-powertools

#!/usr/bin/env python3
from aws_cdk import (
    core,
    aws_apigatewayv2 as apigwv2,
    aws_apigatewayv2_integrations as apigwv2_integrations,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
    aws_iam as iam,
)

class ServerlessStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create DynamoDB table with composite key (id, name)
        users_table = dynamodb.Table(
            self, "UsersTable",
            table_name="users",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="name", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=core.RemovalPolicy.DESTROY,  # For development - change for production
        )

        # Create Lambda function with AWS Lambda Powertools Layer
        powertools_layer = lambda_.LayerVersion.from_layer_version_arn(
            self, "PowertoolsLayer",
            # Use the latest layer ARN for the region you're deploying to
            layer_version_arn=f"arn:aws:lambda:{self.region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:21"
        )

        # Lambda function with bundled dependencies
        user_api_lambda = lambda_python.PythonFunction(
            self, "UserApiFunction",
            architecture=lambda_.Architecture.ARM_64,
            runtime=lambda_.Runtime.PYTHON_3_13,
            memory_size=1024,
            timeout=10,
            system_log_level="INFO",
            log_retention=30,
            entry="lambda_fn",  # Directory containing the lambda code
            index="apigw_lambda.py",  # File containing the handler
            handler="lambda_handler",  # Handler function
            layers=[powertools_layer],
            environment={
                "TABLE_NAME": users_table.table_name,
            },
        )
        
        # Grant the Lambda function permissions to read/write to the DynamoDB table
        users_table.grant_read_write_data(user_api_lambda)

        # Create HTTP API Gateway
        http_api = apigwv2.HttpApi(
            self, "UserApi",
            api_name="user-api",
            description="API for user management"
        )

        # Add Lambda integration
        lambda_integration = apigwv2_integrations.HttpLambdaIntegration(
            "LambdaIntegration", handler=user_api_lambda
        )

        # Add routes with Lambda integration
        http_api.add_routes(
            path="/{proxy+}",
            methods=[apigwv2.HttpMethod.ANY],
            integration=lambda_integration
        )

        # Output the API Gateway URL
        core.CfnOutput(
            self, "ApiUrl",
            value=http_api.url,
            description="URL of the HTTP API Gateway"
        )

app = core.App()
ServerlessStack(app, "ServerlessUserApiStack")
app.synth()