
import aws_cdk as cdk
from constructs import Construct
from lambda_stack import LambdaStack

class AppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_stack = LambdaStack(self, "LambdaStack")
