
# https://pypi.org/project/cdklabs.generative-ai-cdk-constructs/
# pip install cdklabs.generative-ai-cdk-constructs

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

class BedrockAgentCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        action_group_function = PythonFunction(
            self,
            "BedrockAgentLambda",
            runtime=Runtime.PYTHON_3_13,
            entry="./lambda",  
            index="agentLambdaPowertools.py",
            handler="lambda_handler",
        )

        agent = Agent(
            self,
            "Agent",
            foundation_model=BedrockFoundationModel.ANTHROPIC_CLAUDE_INSTANT_V1_2,
            instruction="You are a helpful and friendly agent that schedules meetings by asking the attendee's email",
        )
        agent.add_action_group(
            action_group_name="ScheduleMeetings",
            description="Use this function to schedule a meeting with an attendee. The attendee email is required",
            action_group_executor=action_group_function,
            action_group_state="ENABLED",
            api_schema=ApiSchema.from_asset("./openapi.json"),  
        )

        cdk.CfnOutput(self, "AgentId", value=agent.agent_id)
        cdk.CfnOutput(self, "AgentArn", value=agent.agent_arn)
        cdk.CfnOutput(self, "AgentAliasId", value=agent.agent_alias_id)
        cdk.CfnOutput(self, "AgentAliasArn", value=agent.agent_alias_arn)
        cdk.CfnOutput(self, "AgentResourceArn", value=agent.agent_resource_arn)
        cdk.CfnOutput(self, "AgentRoleArn", value=agent.agent_role_arn)

app = cdk.App()
BedrockAgentCdkStack(app, "BedrockAgentsCdkStack")
app.synth()