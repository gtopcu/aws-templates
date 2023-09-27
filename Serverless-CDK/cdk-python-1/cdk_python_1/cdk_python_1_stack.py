#from aws_cdk import App, Construct
from aws_cdk import (
    Stack,
    aws_sqs as sqs, Duration,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

#import aws_cdk as cdk
#import aws_cdk.aws_s3 as s3
#import aws_cdk.aws_lambda as lambda_

class CdkPython1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "CDKQueue1",
            visibility_timeout=Duration.seconds(300),
            removal_policy=RemovalPolicy.DESTROY
        )

        bucket = s3.Bucket(self, "CDKBucket1", bucket_name="cdk-bucket-1", 
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True)

