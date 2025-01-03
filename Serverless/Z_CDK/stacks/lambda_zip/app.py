import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    Duration,
)
from constructs import Construct
import subprocess
import os
import shutil

# my-lambda-project/
# ├── lambda/
# │   ├── handler.py
# │   └── requirements.txt
# └── app.py

# pip install aws-cdk-lib
# cdk init app --language python
# cdk synth
# cdk deploy


def _create_deployment_package():
    if os.path.exists("build"):
        shutil.rmtree("build")
    os.makedirs("build")

    shutil.copytree("lambda", "build/lambda_package")

    subprocess.check_call(
        [
            "pip",
            "install",
            "-r",
            "lambda/requirements.txt",
            "-t",
            "build/lambda_package",
        ]
    )

    shutil.make_archive("build/lambda", "zip", "build/lambda_package")
    shutil.rmtree("build/lambda_package")


class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Build the Lambda package
        self._create_deployment_package()

        # Create Lambda function
        self.lambda_fn = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("build/lambda.zip"),
            timeout=Duration.seconds(30),
            memory_size=128,
            environment={
                "ENVIRONMENT": "production",
            },
        )

    _create_deployment_package()


if __name__ == "__main":
    _create_deployment_package()


# app = cdk.App()
# LambdaStack(app, "LambdaZIP") #env=cdk.Environment(account='123456789012', region='us-east-1'),
# app.synth()
