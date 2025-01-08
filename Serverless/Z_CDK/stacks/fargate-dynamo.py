# app.py (Your Python application)
# import boto3
# import os

# class DynamoDBService:
#     def __init__(self):
#         # Initialize DynamoDB client
#         self.dynamodb = boto3.resource('dynamodb')
#         self.table = self.dynamodb.Table(os.environ.get('TABLE_NAME', 'YourTableName'))

#     def get_item(self, key):
#         try:
#             response = self.table.get_item(
#                 Key={'id': key}
#             )
#             return response.get('Item')
#         except Exception as e:
#             print(f"Error getting item: {str(e)}")
#             return None

#     def put_item(self, item):
#         try:
#             response = self.table.put_item(
#                 Item=item
#             )
#             return response
#         except Exception as e:
#             print(f"Error putting item: {str(e)}")
#             return None

#     def query_items(self, key_value, index_name=None):
#         try:
#             params = {
#                 'KeyConditionExpression': 'id = :val',
#                 'ExpressionAttributeValues': {':val': key_value}
#             }
#             if index_name:
#                 params['IndexName'] = index_name
                
#             response = self.table.query(**params)
#             return response.get('Items', [])
#         except Exception as e:
#             print(f"Error querying items: {str(e)}")
#             return []

# CDK stack for infrastructure
from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class FargateDynamoDBStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        my_project/
        ├── app/
        │   ├── app.py
        │   ├── requirements.txt
        │   └── Dockerfile
        ├── infrastructure/
        │   └── stack.py
        └── app.py (CDK app)

        - Uses IAM roles instead of access keys
        - Scoped permissions to specific table
        - Runs in private subnets with NAT & load balancing

        """

        # Create DynamoDB table
        table = dynamodb.Table(
            self, "MyTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,  
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )
                
        vpc = ec2.Vpc(self, "MyVPC", max_azs=2)
        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        task_definition = ecs.FargateTaskDefinition(
            self, "MyTaskDefinition",
            memory_limit_mib=512,
            cpu=256
        )

        task_definition.add_to_task_role_policy(
            iam.PolicyStatement(
                actions=[
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Query",
                    "dynamodb:Scan",
                    "dynamodb:UpdateItem",
                    "dynamodb:DeleteItem"
                ],
                resources=[table.table_arn]
            )
        )

        container = task_definition.add_container(
            "MyContainer",
            image=ecs.ContainerImage.from_asset("./app"),
            environment={
                "TABLE_NAME": table.table_name,
                "AWS_DEFAULT_REGION": self.region
            },
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix="MyService"
            )
        )

        # Create Fargate service
        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "MyService",
            cluster=cluster,
            task_definition=task_definition,
            public_load_balancer=True,
            desired_count=2,
            # assign_public_ip=False,
            # redirect_http=True,
            # security_groups=[ec2.SecurityGroup.from_security_group_id(
            #     self, "DefaultSecurityGroup", vpc.vpc_default_security_group
            # )]
            # vpc=vpc,
            # listener_port=80
            # listener_protocol=ecs.ApplicationProtocol.HTTP
            # target_group_health_check={"path": "/health"}
            # health_check_grace_period=cdk.Duration.seconds(60)
        )

# Dockerfile
# FROM python:3.13-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["python", "app.py"]

# requirements.txt
# boto3==1.26.137
# botocore==1.29.137