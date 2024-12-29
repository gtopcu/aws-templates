
from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    core
)

class MyCdkApp(core.Stack):
    def _init_(self, scope: core.Construct, id: str, **kwargs) -> None:
        super()._init_(scope, id, **kwargs)

        # DynamoDB Table
        self.ddb_table = dynamodb.Table(
            self, "CDKDynamoTable",
            partition_key=dynamodb.Attribute(name="PK", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="SortKey", type=dynamodb.AttributeType.NUMBER),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            # billing_mode=dynamodb.BillingMode.PROVISIONED,
            # read_capacity=5,
            # write_capacity=5
            # point_in_time_recovery=True,
            # time_to_live_attribute="TTL",
            # stream=dynamodb.StreamViewType.KEYS_ONLY,
            # stream=dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
            # stream=dynamodb.StreamViewType.NEW_IMAGE,
            # server_side_encryption=True,
            # encryption=dynamodb.TableEncryption.AWS_MANAGED,
            # removal_policy=core.RemovalPolicy.DESTROY,
            # removal_policy=core.RemovalPolicy.SNAPSHOT,
            removal_policy=core.RemovalPolicy.RETAIN,
        )

        # Lambda Function
        self.ddb_lambda = _lambda.Function(
            self, "CDKDynamoLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            memory_size=1769,
            timeout=core.Duration.seconds(30),
            handler="cdk_dynamo_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": self.ddb_table.table_name
            },
            # layers=[layer],
            # tracing=_lambda.Tracing.ACTIVE,
            # retry_attempts=0,
            # reserved_concurrent_executions=10,
            # dead_letter_queue=queue
            # vpc=vpc,
            # security_groups=[sg],
            # allow_all_outbound=True,
            # allow_public_subnet=True,
            # allow_public_subnet_ip_ranges=["1.2.3.4/32"],
            # allow_public_subnet_egress=True,
            # allow_public_subnet_egress_ip_ranges=["1.2.3.4/32"],
        )

        # Grant DynamoDB table access to Lambda function
        self.ddb_table.grant_read_write_data(self.ddb_lambda)
        # self.ddb_table.grant_stream_read(self.ddb_lambda)
        # self.ddb_table.grant_full_access(self.ddb_lambda)
        

app = core.App()
MyCdkApp(app, "MyCdkApp")
app.synth()