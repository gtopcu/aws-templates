
# Create a CDK stack which contains an API Gateway API that directs all requests to a lambda function using proxy integration

import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_lambda as _lambda,
    #aws_apigateway as apigw, 
    aws_apigateway as apigw, 
    aws_iam as iam,
)
from constructs import Construct

class ApiGatewayLambdaStackL2(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function
        self.lambda_fn = _lambda.Function(
            self,
            id="LambdaFunction",
            function_name="LambdaFunction",
            # description=f"{self.stack_name}-LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            # architecture= _lambda.Architecture.X86_64,
            memory_size=1769,
            code=_lambda.Code.from_asset("lambda_fns"),
            handler="mylambda.handler",
            timeout=Duration.seconds(30),
            # environment={
            #     "QUEUE_URL": self.queue.queue_url
            # },
            logging_format= _lambda.LoggingFormat.JSON,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Create API Gateway
        self.api_gw = apigw.RestApi(
            self,
            id="RestApi",
            rest_api_name="RestApi",
            description=f"{self.stack_name} - API Gateway with proxy integration to Lambda",
            endpoint_types=[apigw.EndpointType.REGIONAL],
            deploy=True,

            # api_key_source_type=apigw.ApiKeySourceType.HEADER  # Enable API key source

            # cloud_watch_role=True,
            # cloud_watch_role_removal_policy=RemovalPolicy.DESTROY,

            # Can control headers & http status code directly from lambda in proxy integration
            # default_cors_preflight_options=apigw.CorsOptions(
            #     allow_origins=apigw.Cors.ALL_ORIGINS,
            #     allow_methods=apigw.Cors.ALL_METHODS,
            #     allow_headers=apigw.Cors.DEFAULT_HEADERS,
            #     max_age=Duration.seconds(86400),
            # ),

            # default_integration=apigw.LambdaIntegration(
            #     self.lambda_fn,
            #     proxy=True,
            #     integration_responses=[
            #         apigw.IntegrationResponse(
            #             status_code="200",
            #             response_parameters={
            #                 "method.response.header.Access-Control-Allow-Origin": "'*'"
            #             }
            #         )
            #     ]
            # ),

            # deploy_options=apigw.StageOptions(
            #     stage_name="default",
            #     description="Default Stage",
            #     logging_level=apigw.MethodLoggingLevel.INFO,
            #     data_trace_enabled=True,
            #     tracing_enabled=True,
            #     metrics_enabled=True,
            #     throttling_burst_limit=100,
            #     throttling_rate_limit=10
            # ),
            # default_method_options=apigw.MethodOptions(
            #     authorization_type=apigw.AuthorizationType.NONE,
            #     method_responses=[
            #         apigw.MethodResponse(
            #             status_code="200",
            #             response_models={
            #                 "application/json": apigw.Model.EMPTY_MODEL
            #             }
            #         )
            #     ]
            # )
        )
        
        # Create proxy integration
        api_gw_integration = apigw.LambdaIntegration(
            self.lambda_fn,
            proxy=True 
        )

        # Add proxy resource with {proxy+} - catches all routes
        api_gw_proxy = self.api_gw.root.add_resource("{proxy+}")
        # api_gw_proxy = self.api_gw.root.add_resource("/v1/customers/{proxy+}", 
        #     default_cors_preflight_options=apigw.CorsOptions(allow_origins=['*']),
        #     default_integration=api_gw_integration,
        # )
        api_gw_proxy.add_method('ANY', api_gw_integration)  # ANY method will catch all HTTP methods

        # Also add the root path
        self.api_gw.root.add_method('ANY', api_gw_integration)

        # # Create usage plan
        # plan = self.api_gw.add_usage_plan('UsagePlan',
        #     name='Standard',
        #     description='Standard usage plan with API key',
        #     throttle=apigw.ThrottleSettings(
        #         rate_limit=10,
        #         burst_limit=20
        #     ),
        #     quota=apigw.QuotaSettings(
        #         limit=1000,
        #         period=apigw.Period.MONTH
        #     )
        # )

        # # Create API key
        # key = self.api_gw.add_api_key('ApiKey',
        #     api_key_name='MyApiKey',
        #     description='API key for accessing the API'
        # )

        # # Associate API key with usage plan
        # plan.add_api_key(key)

        # Set other config
        # self.api_gw.add_domain_name()
        # self.api_gw.add_api_key()

        cdk.CfnOutput(self,"APIGW-URL", value=self.api_gw.url, export_name="APIGW-URL") # Fn.importValue(exportName)
        cdk.CfnOutput(self,"APIGW-DomainName", value=self.api_gw.domain_name)
        cdk.CfnOutput(self,"APIGW-Stage", value=self.api_gw.deployment_stage)        
        cdk.CfnOutput(self,"LambdaFunctionArn", value=self.lambda_fn.function_arn)
        
app = cdk.App()
ApiGatewayLambdaStackL2(app, "ApiGatewayLambdaStack") # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()


# def handler(event, context):
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         },
#         'body': {
#             'message': 'Hello from Lambda!',
#             'path': event['path'],
#             'method': event['httpMethod'],
#             'queryStringParameters': event['queryStringParameters'],
#             'headers': event['headers']
#         }
#     }
