
import aws_cdk as cdk
from aws_cdk import (
    Stack,
    Duration,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_sqs as _sqs
)
from constructs import Construct

#https://serverlessland.com/patterns/lambda-sqs-cdk
class LambdaSqsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create SQS Queue
        queue = _sqs.Queue(
            self, "infraops-cdktest-LambdaToSqsQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name='infraops-cdktest-LambdaToSqsQueue')

        # Create Lambda function
        lambda_fn = _lambda.Function(
            self, "infraops-cdktest-LambdaFunctionToSqs",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="sendSqsMessage.handler",
            code=_lambda.Code.from_asset("lambda_fns"),
        )

        # Grant send message to lambda function
        queue.grant_send_messages(lambda_fn)
        queue.grant_consume_messages(lambda_fn)

        cdk.CfnOutput(self, "QueueARN", value=queue.queue_arn)

app = cdk.App()
LambdaSqsCdkStack(app, "LambdaSqsCdkStack")
app.synth()