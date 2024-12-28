
from aws_cdk import App
from lambda_layer_stack import LambdaLayerStack

app = App()
LambdaLayerStack(app, "LambdaLayerStack")
app.synth()