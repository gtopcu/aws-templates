
from aws_cdk import (
    Stack,
)
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from cdklabs.generative_ai_cdk_constructs.bedrock import (
    Agent,
    ApiSchema,
    BedrockFoundationModel,
)
from constructs import Construct

# https://docs.powertools.aws.dev/lambda/python/2.37.0/core/event_handler/bedrock_agents/#required-resources

class AgentsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        action_group_function = PythonFunction(
            self,
            "LambdaFunction",
            runtime=Runtime.PYTHON_3_12,
            entry="./lambda",  
            index="app.py",
            handler="lambda_handler",
        )

        agent = Agent(
            self,
            "Agent",
            foundation_model=BedrockFoundationModel.ANTHROPIC_CLAUDE_INSTANT_V1_2,
            instruction="You are a helpful and friendly agent that answers questions about insurance claims.",
        )
        agent.add_action_group(
            action_group_name="InsureClaimsSupport",
            description="Use these functions for insurance claims support",
            action_group_executor=action_group_function,
            action_group_state="ENABLED",
            api_schema=ApiSchema.from_asset("./lambda/openapi.json"),  
        )