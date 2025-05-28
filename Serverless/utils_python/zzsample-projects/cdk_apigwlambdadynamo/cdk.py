#!/usr/bin/env python3
import os
import aws_cdk as cdk
from app import ServerlessStack

app = cdk.App()
env = cdk.Environment(
    account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
    region=os.environ.get("CDK_DEFAULT_REGION")
)

ServerlessStack(app, "ServerlessUserApiStack", env=env)

app.synth()