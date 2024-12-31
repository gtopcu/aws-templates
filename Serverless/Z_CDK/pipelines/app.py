#!/usr/bin/env python3
import aws_cdk as cdk

from pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "CDKPipelineStack",
    env=cdk.Environment(account="111111111111", region="eu-west-1")
)

app.synth()