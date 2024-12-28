
from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_iam as iam,
)
from constructs import Construct

class LambdaLayerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        my_cdk_project/
        │
        ├── layer/
        │   └── python/
        │       └── your_shared_code/
        │           ├── __init__.py
        │           └── shared_functions.py
        │
        ├── lambda/
        │   └── index.py
        │
        └── app.py

        Layers have a size limit of 250 MB unzipped
        Can enable cross-account access
        """

        lambda_layer = _lambda.LayerVersion(
            self, 'CustomLambdaLayer',
            # Specify the path to your layer code directory
            # This directory should contain a 'python' folder with your packages
            code=_lambda.Code.from_asset('layer'),
            compatible_runtimes=[
                _lambda.Runtime.PYTHON_3_12,
                _lambda.Runtime.PYTHON_3_13
            ],
            description='Custom Lambda Python Layer with shared code',
            layer_version_name='custom-layer-python',
            removal_policy=RemovalPolicy.RETAIN
        )

        # Optional: Create a Lambda function that uses this layer
        lambda_fn = _lambda.Function(
            self, 'Function',
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler='index.handler',
            code=_lambda.Code.from_asset('lambda'),
            layers=[lambda_layer]
        )