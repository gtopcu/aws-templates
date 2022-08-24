
# https://www.youtube.com/watch?v=Tke8YTHqEbQ

# cdk init app --language python
# source .venv/bin/activate
# pip install -r requirements.txt
# sam local invoke -t ./cdk.out/CdkPowertoolsPythonStack.template.json aainfraopscdktestlambda4413BD1B

from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda
)
from aws_cdk.aws_lambda import Function, Runtime, Code, Alias, VersionOptions
from constructs import Construct
import datetime

class CdkPowertoolsPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        current_date =  datetime.datetime.today().strftime('%d-%m-%Y')
        
        # Create Lambda function
        lambda_fn = _lambda.Function(
            self, "aa-infraops-cdktestlambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="ptLambda.handler",
            code=_lambda.Code.from_asset("lambda_fns"),
            current_version_options = VersionOptions(
                description = f'Version deployed on {current_date}',
                removal_policy = RemovalPolicy.RETAIN
            )
        )
        new_version = lambda_fn.current_version
        new_version.apply_removal_policy(RemovalPolicy.RETAIN)

        alias = Alias(
            scope = self,
            id = "FunctionAlias",
            alias_name = "dev",
            version = new_version
        )

        
