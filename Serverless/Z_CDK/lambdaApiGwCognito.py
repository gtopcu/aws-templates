
from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_cognito as cognito,
    aws_iam as iam,
    core
)

class MyCdkApp(core.Stack):
    def _init_(self, scope: core.Construct, id: str, **kwargs) -> None:
        super()._init_(scope, id, **kwargs)

        # Cognito User Pool
        user_pool = cognito.UserPool(
            self, "MyUserPool",
            self_sign_up_enabled=True,
            sign_in_aliases=cognito.SignInAliases(
                email=True,
                username=True,
                phone=False,
                preferred_username=False
            )
        )

        # Lambda function
        my_lambda = _lambda.Function(
            self, "MyLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            memory_size=1769,
            timeout=core.Duration.seconds(30),
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "USER_POOL_ID": user_pool.user_pool_id
            }
        )

        # Grant Lambda function permissions to access Cognito User Pool
        user_pool.grant_invoke(my_lambda)

        # API Gateway
        api = apigateway.RestApi(
            self, "MyAPI",
            rest_api_name="MyAPI",
            # description="This service serves as CDK test",
            # deploy_options=apigateway.StageOptions(stage_name="prod"),
            # deploy=True,
            # retain_deployments=False,
            # default_cors_preflight_options=apigateway.CorsOptions(allow_origins=apigateway.Cors.ALL_ORIGINS),
            # default_integration=integration,
            # default_method_options=apigateway.MethodOptions(authorization_type=apigateway.AuthorizationType.COGNITO),
            # default_method_authorization_scopes=[user_pool.user_pool_arn],
            # endpoint_types=[apigateway.EndpointType.REGIONAL],
            # cloud_watch_role=True,
            # disable_execute_api_endpoint=False,
            # binary_media_types=["*/*"],
            # minimum_compression_size=0,
            # default_method_pricing=apigateway.MethodLoggingLevel.INFO,
            # default_resource_policy=apigateway.ResourcePolicy(
            #     statements=[apigateway.PolicyStatement(actions=["execute-api:Invoke"], resources=["execute-api:/*/*/*"])]
            # ),
            # policy=iam.PolicyDocument(statements=[iam.PolicyStatement(actions=["execute-api:Invoke"], resources=["execute-api:/*/*/*"])]),
        )

        # Cognito Authorizer
        cognito_authorizer = apigateway.CfnAuthorizer(
            self, "CognitoAuthorizer",
            rest_api_id=api.rest_api_id,
            name="CognitoAuthorizer",
            type="COGNITO_USER_POOLS",
            identity_source="method.request.header.Authorization",
            provider_arns=[user_pool.user_pool_arn]
        )

        # Integration between API Gateway and Lambda
        integration = apigateway.LambdaIntegration(
            my_lambda,
            proxy=True,
            allow_test_invoke=True,
            # request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        # API Gateway Method
        api.root.add_method("ANY", integration,
                            authorization_type=apigateway.AuthorizationType.COGNITO,
                            authorizer=apigateway.CfnAuthorizer.IdentifierProperty(id=cognito_authorizer.ref))

app = core.App()
MyCdkApp(app, "MyCdkApp")
app.synth()