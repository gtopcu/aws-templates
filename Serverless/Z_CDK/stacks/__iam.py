
import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_iam as iam,
)

from constructs import Construct

stack = None
lambda_fn = None
bucket = None


class IAMStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        #  # https://docs.aws.amazon.com/cdk/v2/guide/define-iam-l2.html

        # Add this to use the role customization feature
        iam.Role.customizeRoles(stack);

        # Granting access to IAM Group/Users
        iam_group = iam.Group(self, 'data-science')
        iam_user = iam.User(self, 'my-user', groups=[iam_group])
        bucket.grant_read(iam_user)

        existing_role = iam.Role.from_role_name(self, "Role", 
            "my-pre-existing-role", 
            mutable=False) # Prevent CDK from attempting to add policies to this role

        
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        lambda_fn.add_to_role_policy(iam.PolicyStatement(
            actions=['s3:GetObject', 's3:List*'],
            resources=[
                bucket.bucket_arn,
                bucket.arn_for_objects('*'),
            ]
        ))

        ec2_role = iam.Role(
            self, "EC2Role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMPatchAssociation"),
            ],
            inline_policies=ec2_policy
        )

        ec2_policy = iam.Policy( self, "EC2Policy",
            roles=[ec2_role],
            policy_name="EC2Policy",
            # document=ssm_policy_document
            # statements=ssm_policy_document.statements
        )

        ssm_policy_document = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=[
                        "ssm:UpdateInstanceInformation",
                        "ssmmessages:CreateControlChannel",
                        "ssmmessages:CreateDataChannel",
                        "ssmmessages:OpenControlChannel",
                        "ssmmessages:OpenDataChannel"
                    ],
                    resources=["*"],
                    effect=iam.Effect.ALLOW
                )
            ]
        )