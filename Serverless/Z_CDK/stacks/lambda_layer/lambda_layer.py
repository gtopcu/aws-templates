
# https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html

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
        aws lambda publish-layer-version --layer-name my-layer \
            --description "My layer" \
            --license-info "MIT" \
            --zip-file fileb://layer.zip \
            --compatible-runtimes python3.12 python3.13 \
            --compatible-architectures "arm64" "x86_64"

        aws lambda delete-layer-version --layer-name my-layer --version-number 1
        aws lambda list-layers --compatible-runtime python3.13
        aws lambda list-layer-versions --layer-name my-layer

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

        Lambda loads the layer content into the /opt directory of that execution environment. 
        For each Lambda runtime, the PATH variable already includes specific folder paths within the /opt directory. 
        To ensure that the PATH variable picks up your layer content, your layer .zip file should have its 
        dependencies in the following folder paths:

        python
        python/lib/python3.x/site-packages (site directories)
        """
        # pip install -t ./layers/python/lib/python3.11/site-packages/ -r ./requirements.txt
        # zip -r layer.zip ./python
        # aws s3 cp layer.zip s3://bucket/layer.zip
        # layer_powertools = _lambda.LayerVersion(
        #     self, 'LambdaPowertools',
        #     code=_lambda.Code.from_asset('./layers/layer.zip'),
        #     compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
        #     description='Lambda Powertools',
        #     layer_version_name='v1.0.0'
        # )

        self.lambda_layer = _lambda.LayerVersion(
            self,
            "CustomLambdaLayer",
            code=_lambda.Code.from_asset("layer"),
            compatible_runtimes=[
                _lambda.Runtime.PYTHON_3_13,
            ],
            compatible_architectures=[
                _lambda.Architecture.ARM_64,
                _lambda.Architecture.X86_64
            ],
            description="Custom Lambda Python Layer",
            layer_version_name="custom-layer-python",
            removal_policy=RemovalPolicy.RETAIN,
        )

        self.lambda_fn = _lambda.Function(
            self,
            "Function",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda"),
            layers=[self.lambda_layer],
        )

        # self.lambda_fn.add_to_role_policy(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.ALLOW,
        #         actions=[
        #             "lambda:GetLayerVersion",
        #             "lambda:PublishLayerVersion",
        #             "lambda:DeleteLayerVersion",
        #         ],
        #         resources=[
        #             self.lambda_layer.layer_version_arn,
        #         ],
        #     )
        # )

        # self.lambda_layer.add_permission(
        #     "allow_lambda_to_access_layer",
        #     principal=iam.ServicePrincipal("lambda.amazonaws.com"),
        #     action="lambda:GetLayerVersion",
        # )
