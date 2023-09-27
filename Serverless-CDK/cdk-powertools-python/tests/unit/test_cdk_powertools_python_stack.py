import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_powertools_python.cdk_powertools_python_stack import CdkPowertoolsPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_powertools_python/cdk_powertools_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPowertoolsPythonStack(app, "cdk-powertools-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
