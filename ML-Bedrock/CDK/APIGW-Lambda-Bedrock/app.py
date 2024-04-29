
# https://towardsaws.com/detailed-roadmap-generative-ai-implementation-in-serverless-computing-using-aws-bedrock-f243755f0a3b

#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.api_lambda_bedrock_stack.api_lambda_bedrock_stack import ApiLambdaBedrockStack


app = cdk.App()
ApiLambdaBedrockStack(app, "ApiLambdaBedrockStack",
   
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
   
    )

app.synth()

# npm run build
# cdk synth
# export CDK_NEW_BOOTSTRAP=1
# cdk bootstrap --trust=YOUR-AWS-ACCOUNT aws://YOUR-AWS-ACCOUNT/us-east-1 --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess aws://YOUR-AWS-ACCOUNT/us-east-1 --verbose --profile=default