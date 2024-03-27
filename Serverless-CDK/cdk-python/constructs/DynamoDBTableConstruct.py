
# from aws_lambda_powertools import Logger, Tracer

import aws_cdk as cdk
from aws_cdk import aws_dynamodb as dynamodb


class DynamoDBTableConstruct(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # DynamoDB table
        self.table = dynamodb.Table(
            self,
            "Table",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        # Outputs
        cdk.CfnOutput(self, "TableName", value=self.table.table_name)
        cdk.CfnOutput(self, "TableArn", value=self.table.table_arn)
        cdk.CfnOutput(self, "TableStreamArn", value=self.table.table_stream_arn)