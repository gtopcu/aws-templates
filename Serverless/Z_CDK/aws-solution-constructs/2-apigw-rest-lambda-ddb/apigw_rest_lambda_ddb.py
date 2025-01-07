
# https://docs.aws.amazon.com/solutions/latest/constructs/aws-apigateway-lambda.html
# https://docs.aws.amazon.com/solutions/latest/constructs/walkthrough-part-2-v2.html
# pip install aws_solutions_constructs.aws_apigateway_lambda
# pip install aws_solutions_constructs.aws_lambda_dynamodb

# cdk init diff synth deploy

# curl https://xxx.execute-api.us-east-1.amazonaws.com/prod/
# Outputs:
#   ApigwLambdaDDBStack.RestApiEndpoint0551178A = https://xxx.execute-api.us-east-1.amazonaws.com/prod/

from aws_cdk import (
    App,
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as ddb,
    
)
from constructs import Construct

from aws_solutions_constructs import (
    aws_apigateway_lambda as apigw_lambda,
    aws_lambda_dynamodb as lambda_ddb
)

class ApigwLambdaDDBStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.lambda_fn = _lambda.Function(
          self, 'HitCounterLambda',
          runtime=_lambda.Runtime.PYTHON_3_13,
          handler='hit_counter.handler',
          code=_lambda.Code.from_asset('lambda'),
        )
        # self.lambda_fn.grant_invoke(self.other_lambda_function)

        self.apigw_lambda.ApiGatewayToLambda(
            self, 'ApiGatewayToLambda',
            existing_lambda_obj=self.lambda_fn,
            # lambda_function_props=_lambda.FunctionProps(
            #     runtime=_lambda.Runtime.PYTHON_3_13,
            #     code=_lambda.Code.from_asset('lambda'),
            #     handler='hit_counter.handler',
            # ),
            api_gateway_props=apigw.RestApiProps(
                default_method_options=apigw.MethodOptions(
                    authorization_type=apigw.AuthorizationType.NONE
                )
            )
        )

        self.hit_counter = lambda_ddb.LambdaToDynamoDB(
            self, 'LambdaToDynamoDB',
            existing_lambda_obj=self.lambda_fn,
            # lambda_function_props=_lambda.FunctionProps(
            #     runtime=_lambda.Runtime.PYTHON_3_11,
            #     code=_lambda.Code.from_asset('lambda'),
            #     handler='hitcounter.handler',
            #     environment={
            #         'DOWNSTREAM_FUNCTION_NAME': self.hello_func.function_name
            #     }
            # ),
            # existing_table_obj=ddb_table
            dynamo_table_props=ddb.TableProps(
                table_name='SolutionsConstructsHits',
                # Default - creates a partition key called "id" for DynamoDB Table
                # Enables server-side encryption for DynamoDB Table using AWS managed KMS Key
                # Retains the Table when deleting the CloudFormation stack
                # Enables continuous backups and point-in-time recovery
                partition_key={
                    'name': 'path',
                    'type': ddb.AttributeType.STRING
                },
                billing_mode=ddb.BillingMode.PAY_PER_REQUEST, # Default: On-Demand 
                removal_policy=RemovalPolicy.DESTROY
            ),
            # table_environment_variable_name='DDB_TABLE_NAME' # Default: DDB_TABLE_NAME
            # table_permissions='ReadWrite', # Default: 'ReadWrite', 'All', 'Read', 'Write'
            
        )



            