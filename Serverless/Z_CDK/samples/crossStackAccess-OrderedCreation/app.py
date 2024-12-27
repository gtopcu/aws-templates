
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

from first_stack import FirstStack
from second_stack import SecondStack

class MyApp(core.App):
    def __init__(self):
        super().__init__()

        first_stack = FirstStack(self, "FirstStack")
        second_stack = SecondStack(self, "SecondStack", first_stack.vpc)
        second_stack.add_dependency(first_stack)

app = MyApp()
app.synth()