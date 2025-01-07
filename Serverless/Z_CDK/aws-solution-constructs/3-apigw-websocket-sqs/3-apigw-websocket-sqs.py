# https://docs.aws.amazon.com/solutions/latest/constructs/aws-apigatewayv2websocket-sqs.html
# pip install aws_solutions_constructs.aws_apigateway_sqs

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
from constructs import Construct

from aws_solutions_constructs.aws_apigateway_sqs import ApiGatewayV2WebSocketToSqs
from aws_cdk.aws_apigatewayv2_authorizers import WebSocketLambdaAuthorizer

class ApigwWebsocketSQSStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # TODO
        auth_handler_lambda = None 
        connect_lambda  = None
        disconnect_lambda = None

        authorizer = WebSocketLambdaAuthorizer("Authorizer", auth_handler_lambda)

        ApiGatewayV2WebSocketToSqs(self, 'ApiGatewayV2WebSocketToSqsPattern', 
            connect_route_options=apigw.WebSocketRouteOptions(
                integration=apigw.WebSocketLambdaIntegration("ConnectIntegration", connect_lambda),
                authorizer=authorizer
            ),
            disconnect_route_options=apigw.WebSocketRouteOptions(
                integration=apigw.WebSocketLambdaIntegration("DisConnectIntegration", disconnect_lambda),
            ),
            create_default_route=True
        )
