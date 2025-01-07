
from aws_cdk import (
    Stack,
    aws_apigatewayv2 as apigatewayv2,
    aws_apigatewayv2_integrations as integrations,
    aws_lambda as lambda_,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    CfnOutput,
    RemovalPolicy
)
from constructs import Construct

class WebSocketApiStack(Stack):
    def _init_(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super()._init_(scope, construct_id, **kwargs)

        # Create DynamoDB table to store connection IDs
        connections_table = dynamodb.Table(
            self, "ConnectionsTable",
            partition_key=dynamodb.Attribute(
                name="connectionId",
                type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Create WebSocket API
        websocket_api = apigatewayv2.WebSocketApi(
            self, "WebSocketAPI",
            route_selection_expression="$request.body.action"
        )

        # Create WebSocket Stage
        stage = apigatewayv2.WebSocketStage(
            self, "WebSocketStage",
            web_socket_api=websocket_api,
            stage_name="default",
            auto_deploy=True
        )

        # Create Lambda functions for WebSocket handlers
        connect_handler = lambda_.Function(
            self, "ConnectHandler",
            runtime=lambda_.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/connect"),
            environment={
                "CONNECTIONS_TABLE": connections_table.table_name,
            }
        )

        disconnect_handler = lambda_.Function(
            self, "DisconnectHandler",
            runtime=lambda_.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/disconnect"),
            environment={
                "CONNECTIONS_TABLE": connections_table.table_name,
            }
        )

        message_handler = lambda_.Function(
            self, "MessageHandler",
            runtime=lambda_.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/message"),
            environment={
                "CONNECTIONS_TABLE": connections_table.table_name,
            }
        )

        # Grant DynamoDB permissions
        connections_table.grant_read_write_data(connect_handler)
        connections_table.grant_read_write_data(disconnect_handler)
        connections_table.grant_read_write_data(message_handler)

        # Grant permissions to execute API Gateway Management API
        execute_api_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["execute-api:ManageConnections"],
            resources=[f"arn:aws:execute-api:{self.region}:{self.account}:{websocket_api.api_id}/*"]
        )

        connect_handler.add_to_role_policy(execute_api_policy)
        disconnect_handler.add_to_role_policy(execute_api_policy)
        message_handler.add_to_role_policy(execute_api_policy)

        # Create integrations
        connect_integration = apigatewayv2.WebSocketLambdaIntegration(
            "ConnectIntegration",
            handler=connect_handler
        )

        disconnect_integration = apigatewayv2.WebSocketLambdaIntegration(
            "DisconnectIntegration",
            handler=disconnect_handler
        )

        message_integration = apigatewayv2.WebSocketLambdaIntegration(
            "MessageIntegration",
            handler=message_handler
        )

        # Add routes
        websocket_api.add_route(
            "$connect",
            integration=connect_integration
        )

        websocket_api.add_route(
            "$disconnect",
            integration=disconnect_integration
        )

        websocket_api.add_route(
            "$default",
            integration=message_integration
        )

        # Output the WebSocket URL
        CfnOutput(
            self, "WebSocketURL",
            value=stage.url,
            description="WebSocket API URL"
        )


# # lambda/connect/index.py
# import os
# import boto3
# import json

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table(os.environ['CONNECTIONS_TABLE'])

# def handler(event, context):
#     connection_id = event['requestContext']['connectionId']
    
#     # Store connection ID
#     table.put_item(
#         Item={
#             'connectionId': connection_id
#         }
#     )
    
#     return {
#         'statusCode': 200,
#         'body': 'Connected'
#     }

# # lambda/disconnect/index.py
# import os
# import boto3

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table(os.environ['CONNECTIONS_TABLE'])

# def handler(event, context):
#     connection_id = event['requestContext']['connectionId']
    
#     # Remove connection ID
#     table.delete_item(
#         Key={
#             'connectionId': connection_id
#         }
#     )
    
#     return {
#         'statusCode': 200,
#         'body': 'Disconnected'
#     }

# # lambda/message/index.py
# import os
# import boto3
# import json
# from boto3.dynamodb.conditions import Scan

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table(os.environ['CONNECTIONS_TABLE'])

# def send_message(connection_id, message, domain_name, stage):
#     gatewayapi = boto3.client('apigatewaymanagementapi',
#         endpoint_url=f'https://{domain_name}/{stage}'
#     )
    
#     try:
#         gatewayapi.post_to_connection(
#             ConnectionId=connection_id,
#             Data=json.dumps(message).encode('utf-8')
#         )
#     except gatewayapi.exceptions.GoneException:
#         # If connection is no longer valid, remove it
#         table.delete_item(Key={'connectionId': connection_id})

# def broadcast_message(message, domain_name, stage):
#     # Get all connections
#     connections = table.scan()
    
#     # Send message to all connections
#     for item in connections['Items']:
#         send_message(item['connectionId'], message, domain_name, stage)

# def handler(event, context):
#     domain_name = event['requestContext']['domainName']
#     stage = event['requestContext']['stage']
#     connection_id = event['requestContext']['connectionId']
    
#     # Handle incoming message
#     body = json.loads(event.get('body', '{}'))
    
#     # Example: Echo the message back to the sender
#     send_message(connection_id, {
#         'message': f"Received: {body.get('message', '')}"
#     }, domain_name, stage)
    
#     # Example: Broadcast message to all connected clients
#     broadcast_message({
#         'broadcast': f"Broadcast: {body.get('message', '')}"
#     }, domain_name, stage)
    
#     return {
#         'statusCode': 200,
#         'body': 'Message sent'
#     }