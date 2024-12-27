
import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2

from first_stack import FirstStack
from second_stack import SecondStack

class MyApp(cdk.App):
    def __init__(self):
        super().__init__()

        first_stack = FirstStack(self, "FirstStack")
        second_stack = SecondStack(self, "SecondStack", vpc=first_stack.vpc)
        second_stack.add_dependency(first_stack)

app = MyApp()
app.synth()