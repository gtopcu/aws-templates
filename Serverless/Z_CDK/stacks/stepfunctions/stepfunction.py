# step_functions_stack.py
from aws_cdk import (
    Stack,
    Duration,
    aws_iam as iam,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
    aws_lambda as _lambda,
    aws_logs as cw
)
from constructs import Construct

import json

class StepFunctionsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # sfn.Activity
        # sfn.Condition
        # sfn.Choice
        # sfn.Condition
        # sfn.Chain
        # sfn.Map
        # sfn.DistributedMap
        # sfn.Errors
        # sfn.Fail
        # sfn.Succeed
        # sfn.Parallel
        # sfn.Pass
        # sfn.State

        process_lambda = None

        # log_group = cw.LogGroup(self, "MyLogGroup")
        # definition = sfn.Chain.start(sfn.Pass(self, "Pass"))
        # sfn.StateMachine(self, "MyStateMachine",
        #     definition_body=sfn.DefinitionBody.from_chainable(definition),
        #     logs=sfn.LogOptions(
        #         destination=log_group,
        #         level=sfn.LogLevel.ALL
        #     )
        # )

        # Create IAM role for Step Functions
        sfn_role = iam.Role(
            self, "StepFunctionsRole",
            assumed_by=iam.ServicePrincipal("states.amazonaws.com"),
            description="Role for Step Functions state machine"
        )
        # Add permissions to invoke Lambda
        sfn_role.add_to_policy(
            iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[process_lambda.function_arn]
            )
        )
        # Add CloudWatch Logs permissions
        sfn_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "logs:CreateLogDelivery",
                    "logs:GetLogDelivery",
                    "logs:UpdateLogDelivery",
                    "logs:DeleteLogDelivery",
                    "logs:ListLogDeliveries",
                    "logs:PutResourcePolicy",
                    "logs:DescribeResourcePolicies",
                    "logs:DescribeLogGroups"
                ],
                resources=["*"]  # You might want to restrict this
            )
        )

        # ***************************************************************************************
        # 1- Create state machine from ASL definition
        # with open('sf.asl', 'r') as f:
        #     definition = json.load(f)

        # state_machine = sfn.CfnStateMachine(
        #     self, "ProcessingStateMachine",
        #     definition_string=json.dumps(definition),
        #     role_arn="arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME", # sfn_role.arn
        #     state_machine_type="STANDARD"
        # )
        
        # state_machine = sfn.fromFile(self, "ProcessingStateMachine", "sf.asl")

        # ***************************************************************************************
        # 2- Define Step Function within CDK

        submit_job = sfn.Pass(
            self, "SubmitJob",
            comment="Submit job for processing",
            parameters={
                "jobId.$": "$$.Execution.Id",
                "input.$": "$.input"
            }
        )

        process_task = tasks.LambdaInvoke(
            self, "ProcessTask",
            lambda_function=process_lambda,
            output_path="$.Payload"
        )

        job_failed = sfn.Fail(
            self, "JobFailed",
            cause="Job processing failed",
            error="ProcessingError"
        )

        job_succeeded = sfn.Succeed(
            self, "JobSucceeded",
            comment="Job completed successfully"
        )

        check_status = sfn.Choice(self, "CheckStatus")
        condition_success = sfn.Condition.string_equals("$.status", "SUCCESS")
        condition_failed = sfn.Condition.string_equals("$.status", "FAILED")

        definition = submit_job\
            .next(process_task)\
            .next(
                check_status
                .when(condition_success, job_succeeded)
                .when(condition_failed, job_failed)
                .otherwise(process_task)
            )

        state_machine = sfn.StateMachine(
            self, "ProcessingStateMachine",
            definition=definition,
            timeout=Duration.minutes(5),
            state_machine_type=sfn.StateMachineType.STANDARD,
            tracing_enabled=True
        )

# app = App()
# StepFunctionsStack(app, "StepFunctionsStack")
# app.synth()

# # lambda/handler.py
# def lambda_handler(event, context):
#     return {
#         "statusCode": 200,
#         "result": "Job processed successfully"
#     }