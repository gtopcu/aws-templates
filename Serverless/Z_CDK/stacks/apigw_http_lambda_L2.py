from aws_cdk import App, Stack

import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigw, # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigatewayv2/README.html
    # aws_apigatewayv2_integrations as apigw_integrations,
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration

from constructs import Construct


class ApiGWHttpLambdaProxyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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


        lambda_integration = HttpLambdaIntegration("LambdaProxyIntegration", self.lambda_fn)

        self.api_gw = apigw.HttpApi(self, id="HttpApi", 
                api_name="HttpApi",
                cors_preflight=apigw.CorsPreflightOptions(
                    allow_methods=[apigw.CorsHttpMethod.GET, apigw.CorsHttpMethod.HEAD,
                    apigw.CorsHttpMethod.OPTIONS, apigw.CorsHttpMethod.POST
                    ],
                    allow_origins=["*"],
                    max_age=Duration.days(10)
                ),
                create_default_stage=True,
                default_authorization_scopes=None,
                default_authorizer=None,
                description="HttpApi",
                disable_execute_api_endpoint=False,
                http_api_name="HttpApi",
                parameter_mapping=apigw.ParameterMapping
                (
                default_domain_mapping=None,
                default_integration=lambda_integration,
                description="HttpApi",
                disable_execute_api_endpoint=False,
                route_selection_expression= None
        )

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

        # self.api_gw.add_routes(
        #     path="/customers",
        #     methods=[apigw.HttpMethod.GET, apigw.HttpMethod.ANY, apigw.CorsHttpMethod],
        #     integration=lambda_integration
        # )

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
