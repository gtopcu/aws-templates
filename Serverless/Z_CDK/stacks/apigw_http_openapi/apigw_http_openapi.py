
# https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-open-api.html

import aws_cdk as cdk

from aws_cdk import (
    App,
    Stack,
    RemovalPolicy,
    Duration,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigw, 
    # aws_apigatewayv2_integrations as apigw_integrations,
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration

from constructs import Construct

import yaml
import os


class ApiGWHttpOpenAPIStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        API URL:
        https://api-id.execute-api.region.amazonaws.com/stage

        AWS OpenAPI Extensions:
        x-amazon-apigateway-integration
        x-amazon-apigateway-cors

        Headers:
        x-amzm-header
        x-apigateway-header
        x-api-key
        x-amz-date

        - HTTP APIs do not support request validation. API Gateway ignores the requestBody and schema fields.
        - HTTP APIs support only the OpenAPI 3.0 specification
        - HTTP APIs support only Lambda proxy and HTTP proxy integrations
        - OpenAPI allows users to define an API with multiple security requirements attached to a particular operation, 
          but API Gateway doesn't support this. Each operation can have only one of IAM authorization, a Lambda authorizer, 
          or a JWT authorizer. Attempting to model multiple security requirements results in an error.

        To migrate from a REST API to an HTTP API, you can export your REST API as an OpenAPI 3.0 definition file,
        then import the API definition as an HTTP API. Exporting a REST API from API Gateway:

        https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html

        EXPORT:
            aws apigateway get-export --parameters extensions='apigateway' --rest-api-id abcdefg123 --stage-name dev --export-type swagger latestswagger2.json
            
            The exported definition file includes API Gateway extensions by default:
            aws apigatewayv2 export-api \
                --api-id api-id  \
                --output-type YAML  \
                --specification OAS30 \
                --stage-name prod \
                stage-definition.yaml

            Doesn't specify a stage - exports the latest configuration of your API, whether it has been deployed to a stage or not. 
            The exported definition file doesn't include API Gateway extensions:
            aws apigatewayv2 export-api \
                --api-id api-id  \
                --output-type JSON  \
                --specification OAS30 \
                --no-include-extensions \
                latest-api-definition.json

            Get Export (Sign with Sig4):
            https://<host>/restapis/<restapi_id>/stages/<stage_name>/exports/oas30?extensions=integration|postman

            GET /restapis/<restapi_id>/stages/<stage_name>/exports/oas30
            Host: apigateway.us-east-1.amazonaws.com
            Accept: application/json (for yaml: application/yaml)

        IMPORT:
            aws apigatewayv2 import-api --body file://api-definition.json

        """

        self.lambda_fn = _lambda.Function(
            self,
            id="LambdaFunction",
            function_name="LambdaFunction",
            # description=f"{self.stack_name}-LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            architecture= _lambda.Architecture.X86_64,
            memory_size=1769,
            code=_lambda.Code.from_asset("lambda_fns"),
            handler="mylambda.handler",
            timeout=Duration.seconds(30),
            # environment={
            #     "QUEUE_URL": queue.queue_url
            # },
            # layers= [ mylayer ],
            # logging_format=_lambda.LoggingFormat.JSON,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # #!/bin/bash
        # URL=<Rest API Endpoint>
        # while true; do
        #     echo "$(date +%F_%H%M%S) - $(curl -s $URL)"
        #     sleep 5
        # done
        # chmod +x script.sh
        # bash ./script.sh

        # Load and process OpenAPI definition
        definition_path = os.path.join(
            os.path.dirname(__file__),
            'openapi',
            'definition.yaml'
        )
        
        with open(definition_path, 'r') as f:
            definition = yaml.safe_load(f)

        # Replace Lambda ARN placeholders
        definition_str = yaml.dump(definition)
        replacements = {
            "${GetItemsFunctionArn}": self.lambda_fn.function_arn,
            "${CreateItemFunctionArn}": self.lambda_fn.function_arn,
            "${GetItemFunctionArn}": self.lambda_fn.function_arn
        }
        
        for key, value in replacements.items():
            definition_str = definition_str.replace(key, value)

        # Create HTTP API
        http_api = apigw.CfnApi(
            self, "HttpApi",
            body=yaml.safe_load(definition_str),
            protocol_type="HTTP"
        )

        # Create Stage
        stage = apigw.CfnStage(
            self, "DefaultStage",
            api_id=http_api.ref,
            auto_deploy=True,
            stage_name="$default"
        )

        # Grant Lambda permissions
        for function in [self.lambda_fn]:
            apigw.CfnApi.EndpointConfiguration
            function.add_permission(
                f"ApiGateway-{function.function_name}",
                principal=apigw.HttpApi.SERVICE_PRINCIPAL,
                action="lambda:InvokeFunction",
                source_arn=f"arn:aws:execute-api:{self.region}:{self.account}:{http_api.ref}/*/*"
            )

        cdk.CfnOutput(self, "ApiUrl", value=f"https://{http_api.ref}.execute-api.{self.region}.amazonaws.com/")
        cdk.CfnOutput(self, "ApiArn", value=f"arn:aws:execute-api:{self.region}:{self.account}:{http_api.ref}/*/*")
        
        # cdk.CfnOutput(self, "API_Endpoint", value=self.api_gw.api_endpoint)
        # cdk.CfnOutput(self, "API_URL", value=self.api_gw.url)
        # cdk.CfnOutput(self, "API_ID", value=self.api_gw.api_id)
        # cdk.CfnOutput(self, "HTTP_API_Name", value=self.api_gw.http_api_name)
        # cdk.CfnOutput(self, "HTTP_API_ID", value=self.api_gw.http_api_id)


app = cdk.App()
ApiGWHttpOpenAPIStack(app, "ApiGWHttpOpenAPIStack") # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()


# # lambda/handler.py
# def get_items(event, context):
#     return {
#         "statusCode": 200,
#         "body": '{"items": []}'
#     }

# def create_item(event, context):
#     return {
#         "statusCode": 201,
#         "body": '{"message": "Item created"}'
#     }

# def get_item(event, context):
#     item_id = event['pathParameters']['id']
#     return {
#         "statusCode": 200,
#         "body": f'{{"id": "{item_id}"}}'
#     }

