
# --------------------------------------------------------------------------------------------------------
# https://docs.aws.amazon.com/cdk/v2/guide/cdk_pipeline.html

# cdk bootstrap aws://102224384400/us-east-2 
# npx cdk bootstrap aws://ACCOUNT-NUMBER/REGION --profile ADMIN-PROFILE \
#     --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess

# https://docs.aws.amazon.com/cdk/v2/guide/cdk_pipeline.html
# npx cdk bootstrap aws://ACCOUNT-NUMBER/REGION --profile ADMIN-PROFILE \
#     --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess \
#     --trust PIPELINE-ACCOUNT-NUMBER

# cdk bootstrap --termination-protection
# aws cloudformation describe-stacks --stack-name CDKToolkit --query "Stacks[0].EnableTerminationProtection"
# true

# git clone GITHUB-CLONE-URL cdk-pipeline
# cd cdk-pipeline
# cdk init app --language python
# source .venv/bin/activate # On Windows, run `.\venv\Scripts\activate` instead
# python -m pip install -r requirements.txt

# You must deploy a pipeline manually once. After that, the pipeline keeps itself up to date from the repo:
# git add --all
# git commit -m "initial commit"
# git push
# cdk deploy

# --------------------------------------------------------------------------------------------------------

import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep, Wave
from app_stage import AppStage

class PipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, cdk_environment:cdk.Environment, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "CDK-Pipeline",
                        pipeline_name="CDK-Pipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("OWNER/REPO", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]))


        stage = pipeline.add_stage(AppStage(self, "stage-app", env=cdk_environment))

        # prod_stage = pipeline.add_stage(AppStage(self, "app-stage-prod", env=cdk_environment))
        # prod_stage.add_pre(ManualApprovalStep("Manual approval stage"))
        # prod_stage.add_post(ManualApprovalStep("Manual approval stage"))

        # You can add stages to a Wave to deploy them in parallel, for example when deploying 
        # a stage to multiple accounts or Regions:
        # wave = pipeline.add_wave("wave")
        # wave.add_stage(AppStage(self, "MyAppEU", env=cdk_environment))
        # wave.add_stage(AppStage(self, "MyAppUS", env=cdk_environment))

        # ------------------------------------------------------------------------------------------------------------

        # 1-Testing using ShellStep:
        # stage.add_post(ShellStep("Run validation shell script", commands=["sudo bash ../tests/validate.sh"]))

        # 2-Using CF Outputs in ShellStep:
        # load_balancer_address = cdk.CfnOutput(lb_stack, "LbAddress",
        #     value=f"https://{lb_stack.load_balancer.load_balancer_dns_name}/")

        # pass the load balancer address to a shell step
        # stage.add_post(ShellStep("Echo LoadBalancer Adress",
        #     env_from_cfn_outputs={"lb_addr": lb_stack.load_balancer_address}
        #     commands=["echo $lb_addr"]))


        # 3-Using programs: 
        # For more complex tests, you can bring shell scripts or programs) into the ShellStep via the inputs property
        # The inputs can be any step that has an output, including a source (such as a GitHub repo) or another ShellStep

        # source   = CodePipelineSource.git_hub("OWNER/REPO", "main")
        # pipeline =  CodePipeline(self, "Pipeline",
        #                 pipeline_name="Pipeline",
        #                 synth=ShellStep("Synth",
        #                     input=source,
        #                     commands=["npm install -g aws-cdk",
        #                         "python -m pip install -r requirements.txt",
        #                         "cdk synth"]))

        # stage = pipeline.add_stage(AppStage(self, "test", env=cdk_environment))
        # stage.add_post(ShellStep("validate", input=source,
        #     commands=["sh ../tests/validate.sh"],
        # ))


        # 4-Getting the additional files from the synth step - If your tests need to be compiled as part of synthesis

        # synth_step = ShellStep("Synth",
        #                 input=CodePipelineSource.git_hub("OWNER/REPO", "main"),
        #                 commands=["npm install -g aws-cdk",
        #                 "python -m pip install -r requirements.txt",
        #                 "cdk synth"])

        # pipeline   = CodePipeline(self, "Pipeline", pipeline_name="MyPipeline", synth=synth_step)

        # stage = pipeline.add_stage(AppStage(self, "test", cdk_environment))

        # # run a script that was compiled during synthesis
        # stage.add_post(ShellStep("validate",
        #     input=synth_step,
        #     commands=["node test/validate.js"],
        # ))



