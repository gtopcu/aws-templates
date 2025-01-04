
# https://docs.aws.amazon.com/solutions/latest/constructs/aws-apigateway-lambda.html
# pip install aws_solutions_constructs.aws_apigateway_lambda

# cdk init diff synth deploy
# outputs API GW URL: 
# curl https://xxx.execute-api.us-east-1.amazonaws.com/prod/

from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    App,
    Stack
)

from aws_solutions_constructs import (
    aws_apigateway_lambda as apigw_lambda
)

class ApigwLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        apigw_lambda.ApiGatewayToLambda(
            self, "ApiGatewayToLambda",
            lambda_function_props=_lambda.FunctionProps(
                runtime=_lambda.Runtime.PYTHON_3_13,
                code=_lambda.Code.from_asset("lambda"),
                handler="mylambda.handler",
            ),
            api_gateway_props=apigw.RestApiProps(
                default_method_options=apigw.MethodOptions(
                    authorization_type=apigw.AuthorizationType.NONE
                )
            )
        )