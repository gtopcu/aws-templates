#!/usr/bin/env python3

# python3 -m venv .venv
# source .venv/bin/activate
# pip install pip-tools
# pip-compile requirements/requirements.in

# https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html
# python -m pip install aws-cdk-lib

# cdk init app --language python
# source .venv/bin/activate
# pip install -r requirements.txt

# export CDK_DEFAULT_ACCOUNT=12312312321
# export CDK_DEFAULT_REGION=us-east-2

"""
cdk init app --language python
cdk ls -> Lists the stacks in the app
cdk synth -> Synthesizes 
cdk bootstrap -> Deploys the CDK Toolkit staging stack; see Bootstrapping
cdk deploy (-all) -> Deploys the specified stack(s)
cdk watch -> Watch for changes
cdk destroy -> Destroys the specified stack(s)
cdk diff -> Compares the specified stack with the deployed stack or a local CloudFormation template
cdk metadata -> Displays metadata about the specified stack
cdk context -> Manages cached context values
cdk docs (doc) -> Opens the CDK API reference in your browser
cdk doctor -> Checks your CDK project for potential problems
"""

import os
import aws_cdk as cdk
from cdk_python_1.cdk_python_1_stack import CdkPython1Stack

app = cdk.App()

CdkPython1Stack(app, "CdkPython1Stack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
