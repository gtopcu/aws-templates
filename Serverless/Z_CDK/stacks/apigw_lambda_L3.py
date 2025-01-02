
# from aws_cdk import aws_apigateway as apigw
# from aws_cdk import aws_lambda_nodejs as nodejs

# api = apigw.LambdaRestApi(self, "MyApi",
#     handler=nodejs.NodejsFunction(self, "Handler",
#         entry="lambda/handler.ts"
#     )
# )

# The main benefits of using the L3 LambdaRestApi construct are:

# - Simplified setup - creates all necessary resources with a single construct
# - Automatic permissions - handles IAM roles and permissions automatically
# - Default configurations - provides sensible defaults for common settings
# - Built-in proxy integration - automatically sets up proxy integration
# - Easy CORS configuration - simplifies adding CORS support
# - Automatic deployments - creates and manages deployment stages


# ----------------------------------------------------------------------------------------------------

import aws_cdk as cdk

from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class ApiGatewayLambdaStackL3(Stack):
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
            #     "QUEUE_URL": queue.queue_url
            # },
            logging_format= _lambda.LoggingFormat.JSON,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Create API Gateway with Lambda integration using L3 construct
        self.api_gw = apigw.LambdaRestApi(
            self,
            id="RestApi",
            rest_api_name="RestApi",
            description=f"{self.stack_name} - API Gateway with proxy integration to Lambda",
            handler=self.lambda_fn, # or lambda version/alias
            proxy=True,
            # deploy=True,
            endpoint_types=[apigw.EndpointType.REGIONAL],
            deploy_options=apigw.StageOptions(
                stage_name='default',
                throttling_rate_limit=10,
                throttling_burst_limit=20,
                logging_level=apigw.MethodLoggingLevel.INFO,
                metrics_enabled=True,
                data_trace_enabled=True
            ),
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=apigw.Cors.ALL_METHODS
            ),
            cloud_watch_role=True,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # cdk.importVpc(self, "VpcId", "vpc-12345678")  
        # api_gw.from_rest_api_id("ApiGatewayRestApiId")
        cdk.CfnOutput(self,"APIGW-URL", value=self.api_gw.url, export_name="APIGW-URL") # Fn.importValue(exportName)
        cdk.CfnOutput(self,"APIGW-DomainName", value=self.api_gw.domain_name)
        cdk.CfnOutput(self,"APIGW-Stage", value=self.api_gw.deployment_stage)        
        cdk.CfnOutput(self,"LambdaFunctionArn", value=self.lambda_fn.function_arn)

app = cdk.App()
ApiGatewayLambdaStackL3(app, "ApiGatewayLambdaStack") # env=cdk.Environment(account='102224384400', region='us-east-2')
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
