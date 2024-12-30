
# https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigatewayv2/README.html
# https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
# https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

import aws_cdk as cdk

from aws_cdk import (
    App,
    Stack,
    RemovalPolicy,
    Duration,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigw, 
    # aws_apigatewayv2_integrations as apigw_integrations,
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration

from constructs import Construct


class ApiGWHttpLambdaProxyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        # https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging.html
        aws logs create-log-group --log-group-name my-log-group
        aws apigatewayv2 update-stage --api-id abcdef \
            --stage-name '$default' \
            --access-log-settings '{"DestinationArn": "arn:aws:logs:region:account-id:log-group:log-group-name", "Format": "$context.identity.sourceIp - - [$context.requestTime] \"$context.httpMethod $context.routeKey $context.protocol\" $context.status $context.responseLength $context.requestId"}'

        https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-throttling.html
        aws apigatewayv2 update-stage \
            --api-id a1b2c3d4 \
            --stage-name dev \
            --route-settings '{"GET /pets":{"ThrottlingBurstLimit":100,"ThrottlingRateLimit":2000}}'

        https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html
        Create JWT authorizer for Cognito:
        aws apigatewayv2 create-authorizer \
            --name cognito-authorizer \
            --api-id api-id \
            --authorizer-type JWT \
            --identity-source '$request.header.Authorization' \
            --jwt-configuration Audience=audience,Issuer='https://cognito-idp.us-east-2.amazonaws.com/userPoolID'
        
        Update route to use JWT authorizer:
        aws apigatewayv2 update-route \
            --api-id api-id  \
            --route-id route-id  \
            --authorization-type JWT \
            --authorizer-id authorizer-id \
            --authorization-scopes user.email 
    
        Update route to use IAM authorization(must have execute-api permission):
            aws apigatewayv2 update-route \
                --api-id abc123 \
                --route-id abcdef \
                --authorization-type AWS_IAM   

        # Modifying request body/headers/querystring/path:
        https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        
        # Custom Domain:
        https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-custom-domain-names.html

        API URL:
        https://api-id.execute-api.region.amazonaws.com/stage

        """

        self.lambda_fn = _lambda.Function(
            self,
            "LambdaFunction",
            function_name="LambdaFunction",
            description="LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            # architecture= _lambda.Architecture.X86_64,
            memory_size=1769,
            code=_lambda.Code.from_asset("lambda_fns"),
            handler="mylambda.handler",
            timeout=Duration.seconds(30),
            # environment={
            #     "QUEUE_URL": queue.queue_url
            # },
            # layers= [ mylayer ],
            logging_format=_lambda.LoggingFormat.JSON,
            # role=iam.Role.from_role_arn(self, "cdktest-LambdaFunctionToSqsRole", "XXX"),
            removal_policy=RemovalPolicy.DESTROY,
        )


        lambda_integration = HttpLambdaIntegration("LambdaProxyIntegration", self.lambda_fn, timeout=Duration.seconds(29))

        self.api_gw = apigw.HttpApi(self, id="HttpApi", 
                api_name="HttpApi",
                description="HttpApi",
                create_default_stage=True,
                default_authorization_scopes=None,
                # default_authorizer=cognito_jwt_authorizer,
                disable_execute_api_endpoint=False,
                http_api_name="HttpApi",
                parameter_mapping=None,
                default_domain_mapping=None,
                default_integration=lambda_integration,
                description="HttpApi",
                disable_execute_api_endpoint=False,
                route_selection_expression= None,
                # cors_preflight=apigw.CorsPreflightOptions(
                #     allow_methods=[apigw.CorsHttpMethod.GET, apigw.CorsHttpMethod.HEAD,
                #     apigw.CorsHttpMethod.OPTIONS, apigw.CorsHttpMethod.POST
                #     ],
                #     allow_origins=["*"],
                #     max_age=Duration.days(10)
                # ),
        )

        # /{proxy+}
        # /parent/{proxy+}
        # {customPath}/pets/{petID}
        # self.api_gw.add_routes(
        #     path="/customers",
        #     methods=[apigw.HttpMethod.GET, apigw.HttpMethod.ANY, apigw.CorsHttpMethod],
        #     integration=lambda_integration
        # )

        # lambda_authorizer = apigw.HttpAuthorizer(
        #     authorizer_type=apigw.HttpAuthorizerType.LAMBDA,
        #     authorizer_name="LambdaAuthorizer",
        #     authorizer_uri=self.lambda_fn.function_arn,
        #     authorizer_payload_format_version=apigw.PayloadFormatVersion.VERSION_2_0,
        #     enable_simple_responses=True,
        #     identity_source=["$request.header.Authorization"],
        #     authorizer_result_ttl=Duration.seconds(600)
        # )

        # iam_authorizer = apigw.HttpAuthorizer(
        #     authorizer_type=apigw.HttpAuthorizerType.IAM,
        #     authorizer_name="IAMAuthorizer",
        #     authorizer_payload_format_version=apigw.PayloadFormatVersion.VERSION_2_0,
        #     enable_simple_responses=True,
        #     identity_source=["$request.header.Authorization"],
        #     authorizer_result_ttl=Duration.seconds(600)
        # )

        # cognito_jwt_authorizer = apigw.HttpAuthorizer(
        #     authorizer_type=apigw.HttpAuthorizerType.JWT,
        #     jwt_configuration=apigw.HttpJwtAuthorizer(
        #                     audience=["audience"],
        #                     issuer="https://cognito-idp.us-east-2.amazonaws.com/userPoolID"
        #                 )
        #     )

        # cognito_jwt_authorizer = apigw.CfnAuthorizer(
        #     self,
        #     "JWTAuthorizer",
        #     api_id=self.api_gw.api_id,
        #     authorizer_type="JWT",
        #     identity_source=["$request.header.Authorization"],
        #     jwt_configuration=apigw.CfnAuthorizer.JWTConfigurationProperty(
        #         audience=["audience"],
        #         issuer="https://cognito-idp.us-east-2.amazonaws.com/userPoolID"
        #     ),
        #     name="JWTAuthorizer"
        # )

        # jwt_authorizer = api_gwIHttpRouteAuthorizer(
        #             jwt=HttpJwtAuthorizer(
        #                 issuer_url="XXX",
        #                 audience=[self.lambda_fn.function_id]
        #             )
        #         ),
        #         default_domain_mapping=apigw.HttpDomainMappingOptions(
        #             api=self.api_gw,
        #             domain_name=apigw.DomainName(
        #                 certificate=apigw.Certificate.from_certificate_arn(self, "Certificate", "XXX"),
        #                 domain_name="serverlessland.com",
        #                 endpoint_type=apigw.EndpointType.REGIONAL,
        #                 security_policy=apigw.SecurityPolicy.TLS_1_2
        #             )
        #         ),
        #         default_route_details=apigw.HttpRouteDetails(
        #             authorizer=apigw.HttpAuthorizer(
        #                 authorizer_type=apigw.HttpAuthorizerType.JWT,
        #                 jwt_configuration=apigw.HttpJwtAuthorizer(
        #                     audience=[self.lambda_fn.function_id],
        #                     issuer="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        #                 )
        #             ),
        #             authorization_scopes=None,
        #             kwargs=None,
        #             operation=None,
        #             parameter_mapping=None,
        #             payload_format_version=apigw.PayloadFormatVersion.VERSION_2_0
        #         )
        #     )

        # self.api_gw.add_stage(construct_id="HttpApi$default", auto_deploy=True)
        # self.api_gw.add_vpc_link(construct_id="VpcLink", vpc_link_name="VpcLink", vpc_link_description="VpcLink", vpc_id=None, subnets=None)

        # self.api_gw.metric_client_error
        # self.api_gw.metric_server_error
        # self.api_gw.metric_count
        # self.api_gw.metric_data_processed
        # self.api_gw.metric_integration_latency
        # self.api_gw.metric_latency
        
        cdk.CfnOutput(self, "API_Endpoint", value=self.api_gw.api_endpoint)
        cdk.CfnOutput(self, "API_URL", value=self.api_gw.url)
        cdk.CfnOutput(self, "API_ID", value=self.api_gw.api_id)
        cdk.CfnOutput(self, "HTTP_API_Name", value=self.api_gw.http_api_name)
        cdk.CfnOutput(self, "HTTP_API_ID", value=self.api_gw.http_api_id)


app = cdk.App()
ApiGWHttpLambdaProxyStack(app, "ApiGWHttpLambdaProxyStack") # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()
