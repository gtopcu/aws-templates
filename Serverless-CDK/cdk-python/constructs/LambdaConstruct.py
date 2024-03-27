
import aws_cdk as cdk
# from aws_cdk import App, Stack #Construct

from aws_cdk import aws_lambda as _lambda
# from aws_cdk import (
#     aws_lambda as lambda_,
#     aws_dynamodb as dynamodb,
#     aws_sqs as sqs, 
#     aws_s3 as s3,
#     RemovalPolicy,
#     Duration
# )

# from aws_cdk import aws_iam as iam
# from aws_cdk.aws_iam import PolicyStatement, Effect, Role, ServicePrincipal

# from aws_cdk import aws_lambda as lambda_
# from aws_cdk.aws_lambda import Function
# from aws_cdk.aws_lambda_event_sources import SqsEventSource


class LambdaConstruct(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create AWS Lambda function
        self.lambda_function = _lambda.Function(
            self,
            "LambdaFunction",
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda.handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            timeout=cdk.Duration.seconds(60),
            memory_size=1769,
            # tracing=_lambda.Tracing.ACTIVE,            
            # role=None,
            # current_version_options=None,
            # retry_attempts=0,
            # dead_letter_queue=None,
            # reserved_concurrent_executions=10,
            # log_retention=cdk.aws_logs.RetentionDays.ONE_WEEK,
            # vpc=None,
            # security_groups=None,
            # insights_version=_lambda.LambdaInsightsVersion.VERSION_1_0_98_0,
            # code_signing_config=None,
            
            environment={
                "LOG_LEVEL": "INFO",
                "ENVIRONMENT": "DEV",
                "AWS_LAMBDA_EXEC_WRAPPER": "/opt/bootstrap",
                "AWS_LAMBDA_LOG_GROUP_NAME": "/aws/lambda/LambdaFunction",
            },
            # layers=[_lambda.LayerVersion.from_layer_version_arn(
            #               self, 
            #               "LambdaLayer", 
            #               layer_version_arn="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            # )],
            # layers=[self.lambda_layer],
            
        )

        # # Create AWS Lambda layer
        # self.lambda_layer = _lambda.LayerVersion(
        #     self,
        #     "LambdaLayer",
        #     code=_lambda.Code.from_asset("lambda_layer"),
        #     compatible_runtimes=[_lambda.Runtime.PYTHON_3_12],
        # )
        # # Add AWS Lambda layer to AWS Lambda function
        # self.lambda_function.add_layers(self.lambda_layer)

        # Add AWS Lambda function to AWS CloudFormation stack outputs
        cdk.CfnOutput(
            self,
            "LambdaFunctionArn",
            value=self.lambda_function.function_arn,
        )