
import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Function, InlineCode, Runtime
from aws_cdk import (
    aws_lambda as _lambda,
    RemovalPolicy,
    Duration
)

class LambdaStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_fn = _lambda.Function(
            self,
            "LambdaFunction",
            function_name="LambdaFunction",
            description="LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            # architecture= _lambda.Architecture.X86_64,
            memory_size=1769,
            # code=_lambda.Code.from_asset("lambda_fns"),
            code=_lambda.Code.from_inline("def handler(event, context):\n  print(event)\n  return \"Hello from Lambda!\""),
            handler="mylambda.handler",
            timeout=Duration.seconds(30),
            removal_policy=RemovalPolicy.DESTROY,
        )