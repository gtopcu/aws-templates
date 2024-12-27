
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class FirstStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Example resource: VPC
        self.vpc = ec2.Vpc(self, "MyVpc")

