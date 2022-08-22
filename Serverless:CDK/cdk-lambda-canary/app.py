#!/usr/bin/env python3
from aws_cdk import App, Environment
import aws_cdk as cdk
import os

from cdk_lambda_canary.cdk_lambda_canary_stack import CdkLambdaCanaryStack

app = cdk.App()

environment_type = app.node.try_get_context("environmentType")
environment_context = app.node.try_get_context(environment_type)
region = environment_context["region"]
account = app.node.try_get_context("account")
stack_name = f'{app.node.try_get_context("prefix")}-{environment_type}'


CdkLambdaCanaryStack(
    app, 
    stack_name, 
    env = Environment(
        account = account,
        region = region
    )
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
