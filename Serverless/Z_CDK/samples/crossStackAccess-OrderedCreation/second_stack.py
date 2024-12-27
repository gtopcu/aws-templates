
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class SecondStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Example resource: EC2 instance that uses the VPC from MyFirstStack
        # Here we would typically reference the VPC from the first stack
        self.ec2_instance = ec2.Instance(self, "MyInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=self.vpc  # Assuming self.vpc is passed from MyFirstStack
        )