
# from aws_lambda_powertools import Logger, Tracer

import aws_cdk as cdk
from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_dynamodb as dynamodb
)

class CustomDynamoDBTableConstruct(dynamodb.TableV2):
    def __init__(self, scope, id, *, partition_key, billing = None, dynamo_stream = None, encryption = None, global_secondary_indexes = None, local_secondary_indexes = None, removal_policy = None, replicas = None, sort_key = None, table_name = None, time_to_live_attribute = None, warm_throughput = None, contributor_insights = None, deletion_protection = None, kinesis_stream = None, point_in_time_recovery = None, resource_policy = None, table_class = None, tags = None):
        super().__init__(scope, id, partition_key=partition_key, billing=billing, dynamo_stream=dynamo_stream, encryption=encryption, global_secondary_indexes=global_secondary_indexes, local_secondary_indexes=local_secondary_indexes, removal_policy=removal_policy, replicas=replicas, sort_key=sort_key, table_name=table_name, time_to_live_attribute=time_to_live_attribute, warm_throughput=warm_throughput, contributor_insights=contributor_insights, deletion_protection=deletion_protection, kinesis_stream=kinesis_stream, point_in_time_recovery=point_in_time_recovery, resource_policy=resource_policy, table_class=table_class, tags=tags)


class DynamoDBStack(cdk.Stack):
    def __init__(self, scope: cdk.Stack, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # DynamoDB table
        self.ddbtable = dynamodb.TableV2(
            self,
            "DDBTable",
            partition_key=dynamodb.Attribute(
                name="PK", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="SK", type=dynamodb.AttributeType.STRING
            ),
            # local_secondary_indexes=[
            #     dynamodb.LocalSecondaryIndex(
            #         index_name="LSI1",
            #         sort_key=dynamodb.Attribute(
            #             name="LSI1SK", type=dynamodb.AttributeType.STRING
            #         )
            #     )
            # ],
            # global_secondary_indexes=[
            #     dynamodb.GlobalSecondaryIndex(
            #         index_name="GSI1",
            #         partition_key=dynamodb.Attribute(
            #             name="GSI1PK", type=dynamodb.AttributeType.STRING
            #         ),
            #         sort_key=dynamodb.Attribute(
            #             name="GSI1SK", type=dynamodb.AttributeType.STRING
            #         )
            #     )
            # ],
            # billing=dynamodb.BillingMode.PAY_PER_REQUEST,  
            # billing=dynamodb.BillingMode.PROVISIONED,
            # read_capacity=5,
            # write_capacity=5
            # point_in_time_recovery=True,
            # time_to_live_attribute="TTL",
            # stream=dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
            # stream=dynamodb.StreamViewType.NEW_IMAGE,
            # stream=dynamodb.StreamViewType.KEYS_ONLY,
            # table_class=dynamodb.TableClass.STANDARD_INFREQUENT_ACCESS,
            # server_side_encryption=True,
            # encryption=dynamodb.TableEncryption.AWS_MANAGED,
            # contributor_insights=True,
            # removal_policy=RemovalPolicy.DESTROY,
            # removal_policy=RemovalPolicy.SNAPSHOT,
            removal_policy=RemovalPolicy.RETAIN,
            deletion_protection=True
        )

        # Grant access to the table for lambda
        # self.ddbtable.grant_read_write_data(lambda_fn)
        # self.ddbtable.grant_stream_read(lambda_fn)
        # self.ddbtable.grant_full_access(lambda_fn)

        # self.ddbtable.grant(
        #     lambda_role,
        #     "dynamodb:PutItem",
        #     "dynamodb:GetItem",
        #     "dynamodb:UpdateItem",
        #     "dynamodb:DeleteItem",
        # )

        # Outputs
        cdk.CfnOutput(self, "TableName", value=self.ddbtable.table_name)
        cdk.CfnOutput(self, "TableArn", value=self.ddbtable.table_arn)
        # cdk.CfnOutput(self, "TableStreamArn", value=self.ddbtable.table_stream_arn)