
from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_notifications as s3_notifications,
    core
)

class MyCdkApp(core.Stack):
    def _init_(self, scope: core.Construct, id: str, **kwargs) -> None:
        super()._init_(scope, id, **kwargs)

        # S3 bucket
        my_bucket = s3.Bucket(
            self, "MyBucket",
            bucket_name="XXXXXXXXXXXXXXXXXXXX",
            removal_policy=core.RemovalPolicy.DESTROY,
            # block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            # enforce_ssl=True,
            # versioned=True,
            # auto_delete_objects=True,
            # encryption=s3.BucketEncryption.KMS_MANAGED
            # encryption=s3.BucketEncryption.S3_MANAGED
            # replication_configuration=s3.ReplicationConfiguration(
            #     role=core.Fn.import_value("S3ReplicationRoleArn"),
            #     rules=[s3.ReplicationRule(
            #         status=s3.ReplicationRuleStatus.ENABLED,
            #         destination=s3.DestinationBucket.from_bucket_arn(
            #             self, "MyDestinationBucket",
            #             core.Fn.import_value("S3ReplicationDestinationArn")
            #         )
            #     )]
            # )
        )

        # Lambda function
        my_lambda = _lambda.Function(
            self, "MyLambda",
            
            runtime=_lambda.Runtime.PYTHON_3_12,
            memory_size=1769,
            timeout=core.Duration.seconds(30),
            handler="cdk_s3_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "BUCKET_NAME": my_bucket.bucket_name
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

        # Grant Lambda function permissions to access S3 bucket
        my_bucket.grant_read_write(my_lambda)

        # Configure S3 put event notification
        notification = s3_notifications.LambdaDestination(my_lambda)
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)

app = core.App()
MyCdkApp(app, "MyCdkApp")
app.synth()