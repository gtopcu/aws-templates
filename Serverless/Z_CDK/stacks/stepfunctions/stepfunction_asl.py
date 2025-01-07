# # step_functions/definition.asl.json
# {
#     "StartAt": "SubmitJob",
#     "States": {
#         "SubmitJob": {
#             "Type": "Pass",
#             "Parameters": {
#                 "jobId.$": "$$.Execution.Id",
#                 "input.$": "$.input"
#             },
#             "Next": "ProcessTask"
#         },
#         "ProcessTask": {
#             "Type": "Task",
#             "Resource": "${ProcessFunctionArn}",
#             "Next": "CheckStatus"
#         },
#         "CheckStatus": {
#             "Type": "Choice",
#             "Choices": [
#                 {
#                     "Variable": "$.status",
#                     "StringEquals": "SUCCESS",
#                     "Next": "JobSucceeded"
#                 },
#                 {
#                     "Variable": "$.status",
#                     "StringEquals": "FAILED",
#                     "Next": "JobFailed"
#                 }
#             ],
#             "Default": "ProcessTask"
#         },
#         "JobSucceeded": {
#             "Type": "Succeed"
#         },
#         "JobFailed": {
#             "Type": "Fail",
#             "Error": "ProcessingError",
#             "Cause": "Job processing failed"
#         }
#     }
# }

# step_functions_stack.py
from aws_cdk import (
    Stack,
    aws_stepfunctions as sfn,
    aws_lambda as _lambda,
    aws_iam as iam,
)
from constructs import Construct
import json
import os

class StepFunctionsAslStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function
        process_lambda = _lambda.Function(
            self, "ProcessFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Create IAM role
        sfn_role = iam.Role(
            self, "StepFunctionsRole",
            assumed_by=iam.ServicePrincipal("states.amazonaws.com")
        )

        # Add Lambda invoke permissions
        sfn_role.add_to_policy(
            iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[process_lambda.function_arn]
            )
        )

        # Load and substitute ASL definition
        definition_path = os.path.join(
            os.path.dirname(__file__),
            'step_functions',
            'definition.asl.json'
        )
        
        with open(definition_path, 'r') as f:
            definition = f.read()
        
        # Replace the placeholder with actual Lambda ARN
        definition = definition.replace(
            "${ProcessFunctionArn}",
            process_lambda.function_arn
        )

        # Create state machine
        state_machine = sfn.CfnStateMachine(
            self, "ProcessingStateMachine",
            definition_string=definition,
            role_arn=sfn_role.role_arn,
            state_machine_type="STANDARD"
        )

# app.py
from aws_cdk import App
# from step_functions_stack import StepFunctionsAslStack

app = App()
StepFunctionsAslStack(app, "StepFunctionsAslStack")
app.synth()

# lambda/handler.py
def lambda_handler(event, context):
    return {
        "status": "SUCCESS",
        "result": "Job processed successfully"
    }