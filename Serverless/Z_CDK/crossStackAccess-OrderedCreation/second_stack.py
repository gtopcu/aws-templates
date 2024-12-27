
import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2

class SecondStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, current_vpc:ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Example resource: EC2 instance that uses the VPC from MyFirstStack
        # Here we would typically reference the VPC from the first stack
        self.ec2_instance = ec2.Instance(self, "MyInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=current_vpc  # Assuming vpc is passed from FirstStack
        )