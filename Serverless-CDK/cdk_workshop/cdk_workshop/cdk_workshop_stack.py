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

# cdk init cdk_workshop --language python
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# export CDK_DEFAULT_ACCOUNT=12312312321
# export CDK_DEFAULT_REGION=us-east-2

export REGION=us-east-2
export PROFILE=default
export ACCOUNT=$(aws sts get-caller-identity --profile $PROFILE)
cdk bootstrap aws://$ACCOUNT/$REGION -c account=$ACCOUNT -c environmentType=qa --profile $PROFILE
#export ACCOUNT=$(aws sts get-caller-identity --profile $PROFILE) | jq -r .Account)
#cdk bootstrap aws://$ACCOUNT/$REGION -c account=$ACCOUNT -c environmentType=qa --profile $PROFILE
cdk bootstrap aws://102224384400/us-east-2 -c environmentType=qa --profile default

https://catalog.us-east-1.prod.workshops.aws/workshops/5195ab7c-5ded-4ee2-a1c5-775300717f42/en-US/first-cdk-project/adding-app-configuration
"""

from datetime import datetime
from aws_cdk import Stack, RemovalPolicy
from constructs import Construct
from aws_cdk.aws_lambda import Function, Runtime, Code, Alias, VersionOptions
from aws_cdk.aws_apigateway import LambdaRestApi, StageOptions
from aws_cdk.aws_cloudwatch import Alarm, ComparisonOperator
from aws_cdk.aws_codedeploy import LambdaDeploymentGroup, LambdaDeploymentConfig

class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment_type = self.node.try_get_context("environmentType")
        context = self.node.try_get_context(environment_type)
        
        self.alias_name = context["lambda"]["alias"]
        self.stage_name = context["lambda"]["stage"]
        current_date =  datetime.today().strftime('%d-%m-%Y')
    
        my_lambda = Function(
            scope = self,
            id = "MyFunction",
            function_name= context["lambda"]["name"],
            handler = "handler.lambda_handler",
            runtime = Runtime.PYTHON_3_9,
            code = Code.from_asset("lambda"),
            current_version_options = VersionOptions(
                description = f'Version deployed on {current_date}',
                removal_policy = RemovalPolicy.DESTROY
            )
        )

        new_version = my_lambda.current_version
        new_version.apply_removal_policy(RemovalPolicy.RETAIN)

        alias = Alias(
            scope = self,
            id = "FunctionAlias",
            alias_name = self.alias_name,
            version = new_version
        )

        LambdaRestApi(
            scope = self,
            id = "RestAPI",
            handler = alias,
            deploy_options = StageOptions(stage_name=self.stage_name)
        )

        failure_alarm = Alarm(
            scope = self,
            id = "FunctionFailureAlarm",
            metric = alias.metric_errors(),
            threshold = 1,
            evaluation_periods = 1,
            alarm_description = "The latest deployment errors > 0",
            alarm_name = f'{self.stack_name}-canary-alarm',
            comparison_operator = ComparisonOperator.GREATER_THAN_THRESHOLD,
        )

        LambdaDeploymentGroup(
            scope = self,
            id = "CanaryDeployment",
            alias = alias,
            deployment_config = LambdaDeploymentConfig.CANARY_10_PERCENT_5_MINUTES,
            alarms = [failure_alarm]
        )
        

