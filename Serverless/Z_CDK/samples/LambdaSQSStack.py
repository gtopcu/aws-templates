from aws_cdk import App, Stack

import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_sqs as sqs,
    aws_s3 as s3,
)

from constructs import Construct


class LambdaSQSStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create AWS Lambda function
        self.lambda_fn = _lambda.Function(
            self,
            "LambdaFunction",
            function_name="LambdaFunction",
            description="LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            # architecture= _lambda.Architecture.X86_64,
            memory_size=1769,
            code=_lambda.Code.from_asset("lambda_fns"),
            handler="mylambda.handler",
            timeout=Duration.seconds(30),
            # environment={
            #     "QUEUE_URL": queue.queue_url
            # },
            # layers= [ mylayer ],
            # tracing=_lambda.Tracing.ACTIVE,
            logging_format=_lambda.LoggingFormat.JSON,
            # log_retention=cdk.aws_logs.RetentionDays.ONE_WEEK,
            # log_retention=None,
            # log_group=None,
            # reserved_concurrent_executions=100,
            # retry_attempts=0,
            # max_event_age=Duration.hours(6)
            # ephemeral_storage_size=1024,
            # application_log_level_v2=
            # on_failure= _lambda_dest.SnsDestination(sns.Topic.from_topic_arn(self, "XXX", "XXX")
            # on_success=_lambda_dest.SqsDestination(queue),
            # on_success=_lambda_dest.S3Destination(bucket=bucket)
            # security_groups=None,
            # vpc=None,
            # profiling=False,
            # role=iam.Role.from_role_arn(self, "cdktest-LambdaFunctionToSqsRole", "XXX"),
            # environment_encryption=iam.Role.from_role_arn(self, "cdktest-LambdaFunctionToSqsRole", "XXX"),
            removal_policy=RemovalPolicy.DESTROY,
            # environment={
            #     "LOG_LEVEL": "INFO",
            #     "ENVIRONMENT": "DEV",
            #     "AWS_LAMBDA_EXEC_WRAPPER": "/opt/bootstrap",
            #     "AWS_LAMBDA_LOG_GROUP_NAME": "/aws/lambda/LambdaFunction",
            # },
        )

        # Create SQS Queue
        self.queue = sqs.Queue(
            self,
            "cdktest-LambdaToSqsQueue",
            queue_name="cdktest-LambdaToSqsQueue",
            visibility_timeout=Duration.seconds(
                300
            ),  # must be at least x6 lambda timeout
            retention_period=Duration.seconds(1209600),  # 14 days max
            # set maxReceiveCount to at least 5 on the lambda
            # redrive_allow_policy=None
            # delivery_delay=0,
            # receive_message_wait_time=Duration.seconds(20),
            # dead_letter_queue=dead_letter_queue
            # encryption=sqs.QueueEncryption.KMS_MANAGED,
            # encryption_master_key=None,
            # max_message_size_bytes=262144,
            # fifo=False,
            # content_based_deduplication=False,
            # use_content_based_deduplication=False,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # self.lambda_fn.from_function_arn()
        # self.lambda_fn.add_environment( "QUEUE_URL", queue.queue_url)
        # self.lambda_fn.add_alias("Alias", description="Alias", version=lambda_fn.current_version)
        # self.lambda_fn.add_function_url(
        #     auth_type=_lambda.FunctionUrlAuthType.NONE,
        #     cors=_lambda.FunctionUrlCorsOptions(
        #         allow_credentials=False,
        #         allowed_headers=["*"],
        #         allowed_methods=["*"],
        #         allowed_origins=["*"],
        #         max_age=Duration.seconds(0),
        #     ),
        # )
        # self.lambda_fn.add_permission( "sqs:SendMessage",
        #     principal= _lambda.ServicePrincipal("sqs.amazonaws.com"),
        #     action="lambda:InvokeFunction",
        #     source_arn=self.queue.queue_arn,
        #     source_account=cdk.Aws.ACCOUNT_ID,
        # )

        # lambda_fn.add_event_source_mapping()
        self.lambda_fn.add_event_source(
            _lambda.SqsEventSource(
                self.queue,
                enabled=True,
                retry_attempts=5,
                # max_concurrency=1,
                # parallelization_factor=1,
                # batch_size=1,
                # max_batching_window=Duration.minutes(1),
                # report_batch_item_failures=True,
            )
        )

        # Grant send message to lambda function
        self.queue.grant_send_messages(self.lambda_fn)
        self.queue.grant_consume_messages(self.lambda_fn)
        self.queue.grant_purge(self.lambda_fn)
        self.queue.grant(self.lambda_fn, "sqs:DeleteMessage")

        cdk.CfnOutput(
            self,
            "LambdaFunctionArn",
            value=self.lambda_fn.function_arn,
            export_name="LambdaFunctionArn",
        )
        cdk.CfnOutput(self, "QueueARN", value=self.queue.queue_arn)


app = cdk.App()
LambdaSQSStack(
    app, "LambdaApiGWStack"
)  # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()
