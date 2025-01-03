import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_iam as iam,
    aws_lambda as _lambda,
)
from constructs import Construct

from aws_cdk.aws_lambda import Function, Runtime, Code, Alias, VersionOptions
from aws_cdk.aws_cloudwatch import Alarm, ComparisonOperator
from aws_cdk.aws_codedeploy import LambdaDeploymentGroup, LambdaDeploymentConfig

from datetime import datetime

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        
        /opt -> lambda layer contents
        /tmp -> Ephemeral storage

        """

        # environment_type = self.node.try_get_context("environmentType")
        # context = self.node.try_get_context(environment_type)
        # self.alias_name = context["lambda"]["alias"]
        # self.stage_name = context["lambda"]["stage"]
        current_date =  datetime.today().strftime('%d-%m-%Y')


        # https://docs.powertools.aws.dev/lambda/python/latest/
        self.layer_powertools = _lambda.LayerVersion.from_layer_version_attributes(self, 'LambdaPowertoolsLatest',
            layer_version_arn="arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-313-x86_64",
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_13]
        )

        self.lambda_fn = _lambda.Function(
            self,
            id="LambdaFunction",
            function_name="LambdaFunction",
            # description=f"{self.stack_name}-LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            # architecture= _lambda.Architecture.X86_64,
            memory_size=1769,
            timeout=Duration.seconds(30),
            code=_lambda.Code.from_asset("./lambda"),
            # Includes all files and subdirectories from the directory by default
            # code=_lambda.Code.from_asset("./lambda", 
            #     exclude=["*.txt", "test/*", ".env"],  # Exclude patterns
            #     ignore_mode=_lambda.IgnoreMode.GIT  # Uses .gitignore rules                                    
            #                         IgnoreMode.DOCKER: Uses .dockerignore rules
            #                         IgnoreMode.NONE: Includes everything
            # )
            # code=_lambda.Code.from_asset("build/lambda.zip"),
            # code=_lambda.Code.from_inline("def handler(event, context):\n  print(event)\n  return \"Hello from Lambda!\""),
            handler="mylambda.handler",
            
            removal_policy=RemovalPolicy.DESTROY,
            # environment={
            #     "QUEUE_URL": queue.queue_url
            # },
            # layers=[self.layer_powertools],
            # tracing=_lambda.Tracing.ACTIVE,
            # system_log_level_v2= _lambda.SystemLogLevel.V2_INFO,
            # application_log_level_v2= _lambda.ApplicationLogLevel.V2_INFO,
            # logging_format=_lambda.LoggingFormat.JSON, # default: LoggingFormat.TEXT
            # log_group=None,
            # log_retention=cdk.aws_logs.RetentionDays.ONE_WEEK,
            # log_retention=None,
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
            # role=self.lambda_execution_role
            # environment_encryption=None,
            # ephemeral_storage_size=cdk.Size.mebibytes(10240), # /tmp
            # filesystem= _lambda.FileSystem.from_efs_access_point(
            #     efs_ap=efs_ap,
            #     mount_path="/mnt/lambda"
            # ),
            # environment={
            #     "LOG_LEVEL": "INFO",
            #     "ENVIRONMENT": "DEV",
            #     "AWS_LAMBDA_EXEC_WRAPPER": "/opt/bootstrap",
            #     "AWS_LAMBDA_LOG_GROUP_NAME": "/aws/lambda/LambdaFunction",
            # },
            # current_version_options = VersionOptions(
            #     description = f'Version deployed on {current_date}',
            #     removal_policy = RemovalPolicy.DESTROY
            # )
        )

        # new_version = self.lambda_fn.current_version
        # new_version.apply_removal_policy(RemovalPolicy.RETAIN)

        # alias = Alias(
        #     scope = self,
        #     id = "FunctionAlias",
        #     alias_name = self.alias_name,
        #     version = new_version
        # )

        # Add Lambda URL
        # https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html
        # https://<url-id>.lambda-url.<region>.on.aws
        # self.lambda_fn.add_function_url(
        #     auth_type=_lambda.FunctionUrlAuthType.NONE, # | AWS_IAM
        #     cors=_lambda.FunctionUrlCorsOptions(
        #         allowed_origins=["*"],
        #         allowed_methods=[_lambda.HttpMethod.ALL],
        #         allowed_headers=["*"]
        #     ),
        #     invoke_mode= _lambda.InvokeMode.BUFFERED # | RESPONSE_STEAM
        # )

        # failure_alarm = Alarm(
        #     scope = self,
        #     id = "FunctionFailureAlarm",
        #     metric = alias.metric_errors(),
        #     threshold = 1,
        #     evaluation_periods = 1,
        #     alarm_description = "The latest deployment errors > 0",
        #     alarm_name = f"{self.stack_name}-canary-alarm",
        #     comparison_operator = ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
        # )

        # https://catalog.us-east-1.prod.workshops.aws/workshops/5195ab7c-5ded-4ee2-a1c5-775300717f42/en-US/first-cdk-project/adding-app-configuration
        # LambdaDeploymentGroup(
        #     scope = self,
        #     id = "CanaryDeployment",
        #     alias = alias,
        #     deployment_config = LambdaDeploymentConfig.CANARY_10_PERCENT_5_MINUTES,
        #     alarms = [failure_alarm]
        # )

        # Create Lambda execution role
        # self.lambda_execution_role = iam.Role(
        #     self, "LambdaExecutionRole",
        #     assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        #     managed_policies=[
        #         iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        #     ]
        # )

        # lambda_role = iam.Role(self, "LambdaExecutionRole",
        #     description="Lambda basic execution role",   
        #     assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        #     managed_policies=[
        #         iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        #     ],
        #     inline_policies=iam.PolicyDocument(
        #         statements=[
        #             iam.PolicyStatement(
        #                 actions=["s3:GetObject", "s3:List*"],
        #                 resources=[
        #                     bucket.bucket_arn,
        #                     bucket.arn_for_objects('*'),
        #                 ]
        #             )
        #         ]
        #     )
        # )
        # lambda_role.add_managed_policy(
        #     iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        # )

        cdk.CfnOutput(self,"LambdaFunctionName", value=self.lambda_fn.function_name, export_name="LambdaFunctionName")
        cdk.CfnOutput(self,"LambdaFunctionArn", value=self.lambda_fn.function_arn, export_name="LambdaFunctionArn")

app = cdk.App()
LambdaStack(app, "LambdaStack")  # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()