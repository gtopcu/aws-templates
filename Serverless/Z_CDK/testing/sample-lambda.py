# tests/infrastructure/test_lambda_stack.py
import aws_cdk as cdk
from aws_cdk.assertions import Template, Match
import pytest
# from lambda_stack import LambdaStack

def test_lambda_stack():

    app = cdk.App()
    stack = LambdaStack(app, "TestStack")
    template = Template.from_stack(stack)
    
    template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": Match.exact("python3.13"),
        "Handler": Match.exact("mylambda.handler"),
        "MemorySize": Match.exact(128), #1769
        "Timeout": Match.exact(30)
    })

    template.has_resource_properties("AWS::Lambda::Function", {
        "Environment": Match.object_like({
            "Variables": Match.object_like({
                "ENVIRONMENT": Match.exact("dev")
            })
        })
    })
    
    template.has_resource_properties("AWS::Lambda::Url", {
        "AuthType": Match.exact("NONE"),
        "Cors": {
            "AllowOrigins": Match.array_with(["*"]),
            "AllowMethods": Match.array_with(["*"]),
            "AllowHeaders": Match.array_with(["*"])
        }
    })
    
    template.resource_count_is("AWS::IAM::Role", 1)
    
    # Test IAM role has basic execution policy
    template.has_resource_properties("AWS::IAM::Role", {
        "ManagedPolicyArns": Match.array_with([
            Match.string_like_regexp(".*AWSLambdaBasicExecutionRole")
        ])
    })

