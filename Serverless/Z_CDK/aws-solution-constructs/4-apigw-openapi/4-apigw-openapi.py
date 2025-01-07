# https://docs.aws.amazon.com/solutions/latest/constructs/aws-openapigateway-lambda.html
# pip install aws_solutions_constructs.aws_openapigateway_lambda

# cdk init diff synth deploy

# curl https://xxx.execute-api.us-east-1.amazonaws.com/prod/
# Outputs:
#   ApigwLambdaDDBStack.RestApiEndpoint0551178A = https://xxx.execute-api.us-east-1.amazonaws.com/prod/

from aws_cdk import (
    App,
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as ddb,
)
from aws_cdk.aws_s3_assets import Asset
from constructs import Construct

from aws_solutions_constructs.aws_openapigateway_lambda import OpenApiGatewayToLambda, ApiIntegration, RestApiBaseProps

class ApigwWebsocketSQSStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        api_definition = Asset(self, "ApiDefinitionAsset", path="./openapi/apiDefinition.yaml")  # deploy_time=False bundling=DOCKET
        #api_definition = Asset(self, "SampleAsset", path=path.join(__dirname, "sample-asset-directory")    

        api_integration = ApiIntegration(id="MessagesHandler", lambda_function_props={
            "runtime": _lambda.Runtime.NODEJS_20_X,
            "handler": "index.handler",
            "code": _lambda.Code.from_asset("./messages-lambda")
        })
        
        # Automatically transforms an incoming OpenAPI Definition (residing locally or in S3) by auto-populating the uri 
        # fields of the x-amazon-apigateway-integration integrations with the resolved value of the backing lambda functions
        openapigateway_to_lambda = OpenApiGatewayToLambda(self,
            id="OpenApiGatewayToLambda",
            api_integrations=[api_integration],
            api_definition_asset=api_definition,
            # api_definition_json=api_definition,
            # api_definition_yaml=api_definition,
            api_gateway_props=RestApiBaseProps(
                rest_api_name="OpenApiGatewayToLambda",
                default_method_options=apigw.MethodOptions(
                    authorization_type=apigw.AuthorizationType.NONE
                )
            ),
            # internal_transform_memory_size: Number,
            # internal_transform_timeout: Duration,
        )

    # const apiIntegrations: ApiIntegration[] = [
    #   {
    #     id: 'MessagesHandler',
    #     lambdaFunctionProps: {
    #       runtime: lambda.Runtime.NODEJS_20_X,
    #       handler: 'index.handler',
    #       code: lambda.Code.fromAsset(`${__dirname}/messages-lambda`),
    #     }
    #   },
    #   {
    #     id: 'PhotosHandler',
    #     existingLambdaObj: new lambda.Function(this, 'PhotosLambda', {
    #       runtime: lambda.Runtime.NODEJS_20_X,
    #       handler: 'index.handler',
    #       code: lambda.Code.fromAsset(`${__dirname}/photos-lambda`),
    #     })
    #   }