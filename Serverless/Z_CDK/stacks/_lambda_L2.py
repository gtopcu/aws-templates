import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_iam as iam,
    aws_lambda as _lambda,
)
from constructs import Construct

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        
        /opt -> lambda layer contents
        /tmp -> Ephemeral storage

        """

        # https://docs.powertools.aws.dev/lambda/python/latest/
        self.layer_powertools = _lambda.LayerVersion.from_layer_version_attributes(self, 'LambdaPowertoolsLatest',
            layer_version_arn="arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-313-x86_64",
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_13]
        )

        # Create Lambda execution role
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

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
            layers=[self.layer_powertools],
            # tracing=_lambda.Tracing.ACTIVE,
            # system_log_level_v2= _lambda.SystemLogLevel.V2_INFO,
            # application_log_level_v2= _lambda.ApplicationLogLevel.V2_INFO,
            # log_format= _lambda.LogFormat.JSON,
            # logging_format=_lambda.LoggingFormat.JSON,
            # log_retention=cdk.aws_logs.RetentionDays.ONE_WEEK,
            # log_retention=None,
            # log_group=None,
            # recursive_loop=RecursiveLoop.Terminate,
            # reserved_concurrent_executions=100,
            # runtime_management_mode=_lambda.RuntimeManagementMode.AUTO | FUNCTION_UPDATE,
            # snap_start= _lambda.SnapStartConf.ON_PUBLISHED_VERSIONS
            # retry_attempts=0,
            # max_event_age=Duration.hours(6)
            # ephemeral_storage_size=1024,
            # application_log_level_v2=
            # on_failure= _lambda_dest.SnsDestination(sns.Topic.from_topic_arn(self, "XXX", "XXX")
            # on_success=_lambda_dest.SqsDestination(queue),
            # on_success=_lambda_dest.S3Destination(bucket=bucket)
            # dead_letter_queue=None,
            # dead_letter_queue_enabled=None,
            # dead_letter_topic
            # security_groups=None,
            # vpc=None,
            # vpc_subnets=None,
            # allow_all_outbound=False
            # allow_all_ipv6_outbound=False
            # ipv6_allowed_for_dual_stack=False
            # allow_public_subnet=False
            # profiling=False,
            # profiling_group=None,
            # role=iam.Role.from_role_arn(self, "cdktest-LambdaFunctionRole", "XXX"),
            # environment_encryption=None,
            # ephemeral_storage_size=cdk.Size.mebibytes(10240), # /tmp
            # filesystem= _lambda.FileSystem.from_efs_access_point(
            #     efs_ap=efs_ap,
            #     mount_path="/mnt/lambda"
            # ),
            removal_policy=RemovalPolicy.DESTROY,
            # environment={
            #     "LOG_LEVEL": "INFO",
            #     "ENVIRONMENT": "DEV",
            #     "AWS_LAMBDA_EXEC_WRAPPER": "/opt/bootstrap",
            #     "AWS_LAMBDA_LOG_GROUP_NAME": "/aws/lambda/LambdaFunction",
            # },
        )

        cdk.CfnOutput(self,"LambdaFunctionArn", value=self.lambda_fn.function_arn, export_name="LambdaFunctionArn")

app = cdk.App()
LambdaStack(app, "LambdaStack")  # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()