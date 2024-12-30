from aws_cdk import (
      Stack,
      aws_lambda as _lambda,
      assertions
    )
import pytest
from aws_cdk.assertions import Template, Match, Capture

stack: Stack = None # MyStack
template = Template.from_stack(stack)

@pytest.fixture()
def template():
    return template

def test_s3bucket_created(template):
    assert template.resource_count_is("AWS::S3::Bucket", 1)

def test_sqs_queue_created(template):
    assert template.resource_count_is("AWS::SQS::Queue", 1)

def test_sns_topic_created(template):
    assert template.resource_count_is("AWS::SNS::Subscription", 1)

def test_dynamodb_table_created(template):
    assert template.resource_count_is("AWS::DynamoDB::Table", 1)

def test_dynamodb_table_encrption(template):
    assert template.has_resource_properties("AWS::DynamoDB::Table", {
            "SSESpecification": {
                "SSEEnabled": True
            }
        }
    )

def test_lambda_created(template):
    assert template.resource_count_is("AWS::Lambda::Function", 1)

def test_lambda_properties(template):
    assert template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.13",
        "MemorySize": 256,
        "Environment": {
            "Variables": {
                "ENVIRONMENT": "DEV",
            }
        },
    })

def test_lambda_has_env_vars(template):
    
    envCapture = Capture()
    # envCapture.next()
    # envCapture.as_object()
    # envCapture.as_string()
    template.has_resource_properties("AWS::Lambda::Function", {
        "Environment": envCapture,
        })

    assert envCapture.as_object() == {
            "Variables": {
                "DOWNSTREAM_FUNCTION_NAME": {"Ref": "TestFunctionXXXXX"},
                "HITS_TABLE_NAME": {"Ref": "HitCounterHitsXXXXXX"},
                },
            }

def test_lambda_has_layer(template):
    assert template.has_resource_properties("AWS::Lambda::Function", {
        "Layers": Match.array_with([
            Match.string_like_regexp("arn:aws:lambda:.*:.*:layer:.*")
        ])
    })

def tess_stepfunctions_created(template):
    assert template.resource_count_is("AWS::StepFunctions::StateMachine", 1)

def test_stepfunctions_definition(template):
    
    assert template.has_resource_properties(
        "AWS::StepFunctions::StateMachine",
        {
            "DefinitionString": Match.serialized_json(
                # Match.object_equals() is used implicitly, but we use it explicitly
                # here for extra clarity.
                Match.object_equals(
                    {
                        "StartAt": "StartState",
                        "States": {
                            "StartState": {
                                "Type": "Pass",
                                "End": True,
                                # Make sure this state doesn't provide a next state --
                                # we can't provide both Next and set End to true.
                                "Next": Match.absent(),
                            },
                        },
                    }
                )
            ),
        },
    )

def test_ec2_instances_created(template):
    assert template.resource_count_is("AWS::EC2::Instance", 1)

def test_ec2_has_tags(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "Tags": Match.array_with([
            Match.object_like({
                "Key": "Name",
                "Value": "HelloWorld"
            })
        ])
    })

def test_ec2_has_userdata(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "UserData": Match.object_like({
            "Fn::Base64": Match.string_like_regexp("#!/bin/bash\n.*curl.*")
        })
    })

def test_ec2_has_security_group(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "SecurityGroups": Match.array_with([
            Match.object_like({
                "Fn::GetAtt": Match.array_with([
                    Match.string_like_regexp("WebServerSG.*")
                ])
            })
        ])
    })

def test_ec2_has_iam_role(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "IamInstanceProfile": Match.object_like({
            "Fn::GetAtt": Match.array_with([
                Match.string_like_regexp("WebServerInstanceProfile.*")
            ])
        })
    })

def test_ec2_has_image(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "ImageId": Match.object_like({
            "Ref": "AMI"
        })
    })

def test_ec2_has_key_pair(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "KeyName": Match.object_like({
            "Ref": "KeyPair"
        })
    })

def test_ec2_has_instance_type(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "InstanceType": Match.object_like({
            "Ref": "InstanceType"
        })
    })

def test_ec2_has_vpc(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "SubnetId": Match.object_like({
            "Ref": "VPC"
        })
    })

def test_ec2_has_public_ip(template):
    assert template.has_resource_properties("AWS::EC2::Instance", {
        "AssociatePublicIpAddress": True
    })

def test_ec2_has_eip(template):
    assert template.resource_count_is("AWS::EC2::EIP", 1)

def test_ec2_has_eip_association(template):
    assert template.resource_count_is("AWS::EC2::EIPAssociation", 1)

def test_ec2_has_role(template):
    assert template.has_resource_properties(
        "AWS::IAM::Role",
        Match.object_equals(
            {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "sts:AssumeRole",
                            "Effect": "Allow",
                            "Principal": {
                                "Service": {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "states.",
                                            Match.any_value(),
                                            ".amazonaws.com",
                                        ],
                                    ],
                                },
                            },
                        },
                    ],
                },
            }
        ),
    )

