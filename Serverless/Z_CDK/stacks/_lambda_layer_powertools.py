
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

class LambdaLayerPowertools(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        
        # https://docs.powertools.aws.dev/lambda/python/latest/
        # https://github.com/aws-powertools/powertools-lambda-python
        # https://serverlessrepo.aws.amazon.com/applications/eu-west-1/057560766410/aws-lambda-powertools-python-layer
        
        # New in 3.4.0 - get the latest version using SysMgr public params:
        # https://github.com/aws-powertools/powertools-lambda-python/releases/tag/v3.4.0
        # aws ssm get-parameter /aws/service/powertools/python/<architecture>/<python_version>/latest -> "x86_64" or "arm64"

        # LocalDev:
        # pip install "aws-lambda-powertools[aws-sdk]"
        # poetry add "aws-lambda-powertools[aws-sdk]" --group dev

        # pip install "aws-lambda-powertools"
        # pip install "aws-lambda-powertools[tracer]"
        # pip install "aws-lambda-powertools[validation]"
        # pip install "aws-lambda-powertools[parser]"
        # pip install "aws-lambda-powertools[datamasking]"
        # pip install "aws-lambda-powertools[tracer,parser,validation]"
        # pip install "aws-lambda-powertools[all]"
        # poetry add "aws-lambda-powertools"

        # aws lambda get-layer-version-by-arn --arn arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:5 --region eu-west-1
        # aws lambda get-layer-version-by-arn --arn arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:5 --region eu-west-1

        # Specific Version
        # layer_powertools = _lambda.LayerVersion.from_layer_version_arn(self, "LambdaPowertools",
        #     "arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-313-x86_64:5"
        # )

        # layer_powertools = _lambda.LayerVersion.from_layer_version_arn(self, 'LambdaPowertools',
            # 'arn:aws:lambda:region:account:layer:name:version'
            # arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-313-x86_64:5
            # arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-313-arm64:5    
        # )

        # LATEST
        # layer_powertools = _lambda.LayerVersion.from_layer_version_attributes(self, 'LambdaPowertoolsLatest',
        #     layer_version_arn="arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-313-x86_64",
        #     compatible_runtimes=[_lambda.Runtime.PYTHON_3_13]
        # )

        # layer_powertools = _lambda.LayerVersion.from_layer_version_attributes(self, 'LambdaPowertoolsLatest',
        #     layer_version_arn='arn:aws:lambda:region:account:layer:name:version',
        #     compatible_runtimes=[_lambda.Runtime.PYTHON_3_13]
        # )