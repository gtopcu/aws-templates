
import aws_cdk as cdk

from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_logs as cw_logs,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _lambda_sources,
    aws_lambda_destinations as _lambda_dest,
    aws_sqs as sqs,
    aws_apigateway as apigw,
    aws_dynamodb as ddb,
    aws_sns as sns,
    aws_sns_subscriptions as sns_subs,

    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_rds as rds,
    aws_elasticache as elasticache,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_wafv2 as waf
)
from constructs import Construct
from aws_cdk.aws_cloudfront import ViewerProtocolPolicy

import os

class CDKPythonStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # import aws_cdk.aws_ssm as ssm
        # ssm.StringParameter(self, "MyVpcId", parameter_name="/my/vpc/id", string_value="vpc-xxx")  # -> stack1
        # vpc_id = ssm.StringParameter.value_for_string_parameter(self, "/my/vpc/id") # -> stack2
        # vpc = ec2.Vpc.from_lookup(self, "ImportedVpc", vpc_id=vpc_id)

        # role=iam.Role.from_role_arn(self, "")

        self.sg = ec2.SecurityGroup(self, "cdktest-SecurityGroup", 
                                    description="cdktest-SecurityGroup",
                                    security_group_name="cdktest-SecurityGroup",
                                    security_group_id="sg-cdktest-SecurityGroup",
                                    vpc=vpc,
                                    allow_all_outbound=True,
                                    allow_all_ipv6_outbound=True,
                                    disable_inline_rules=False,
                                    removal_policy=RemovalPolicy.DESTROY,
                    ).add_ingress_rule( 
                                    peer=ec2.Peer.any_ipv4(), 
                                    connection=ec2.Port.tcp(80), 
                                    description="cdktest-SecurityGroup-AllowHTTP",
                                    remote_rule=False
                    ).security_group_id

        # vpc = ec2.Vpc.from_lookup()
        # vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS).subnet_ids
        self.vpc = ec2.Vpc(self, 
                        "cdktest-VPC", 
                        max_azs=2,
                        subnet_configuration= [
                            ec2.SubnetConfiguration(name="cdktest-public", subnet_type=ec2.SubnetType.PUBLIC),
                            ec2.SubnetConfiguration(name="cdktest-private", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
                        ],
                        removal_policy=RemovalPolicy.DESTROY,
                    )

        # self.vpc.add_flow_log("cdktest-FlowLog",
        #                     destination=ec2.FlowLogDestination.to_cloud_watch_logs(),
        #                     traffic_type=ec2.FlowLogTrafficType.ALL,
        #                     max_aggregation_interval=ec2.FlowLogMaxAggregationInterval.TEN_MINUTES,
        #                     log_format=None,
        #                     log_group=None,
        #                     removal_policy=RemovalPolicy.DESTROY,
        #             )

        # ECS
        self.ecs_cluster = ecs.Cluster( self, "cdktest-ECS",
                                    cluster_name="cdktest-ECS",
                                    # vpc=vpc,
                                    container_insights=True,
                                    enable_fargate_capacity_providers=True,
                                    capacity=ecs.CapacityProviderResources.AUTO_SCALE,
                                    removal_policy=RemovalPolicy.DESTROY,
                                )

        # Fargate
        self.fargate_cluster = ecs_patterns.ApplicationLoadBalancedFargateService( 
                                    self, "cdktest-Fargate",
                                    # cluster=ecs_cluster,
                                    # vpc=vpc
                                    task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                        # image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
                                        # image=ecs.ContainerImage.from_ecr_repository(aws_ecr_assets.DockerImageAsset(self, "cdktest-ECR", directory="./src" )
                                        image=ecs.ContainerImage.from_asset(directory="./src")
                                    ),
                                    task_subnets=ec2.SubnetSelection(
                                        subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                                    ),
                                    desired_count=1,
                                    listener_port=80,
                                    public_load_balancer=True,
                                    cpu=256,
                                    memory_limit_mib=512,
                                    runtime_platform=ecs.RuntimePlatform(
                                        operating_system_family=ecs.OperatingSystemFamily.LINUX,
                                        cpu_architecture=ecs.CpuArchitecture.X86_64
                                    ),
                                    removal_policy=RemovalPolicy.DESTROY,
                                )
        cdk.CfnOutput(self, "FargateServiceARN", value=self.fargate_cluster.service.service_arn)
        cdk.CfnOutput(self, "FargateServiceLBDNS", value=self.fargate_cluster.load_balancer.load_balancer_dns_name)

        # Bucket
        self.bucket = s3.Bucket(self, "cdktest-bucket", 
                            versioned=True, 
                            public_read_access=False,
                            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                            encryption=s3.BucketEncryption.S3_MANAGED,
                            enforce_ssl=True,
                            removal_policy=RemovalPolicy.DESTROY,
                    )

        # CloudFront
        self.cf_distribution = cloudfront.Distribution(self, "cdktest-CloudFrontDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                #origin=origins.S3Origin(s3.Bucket.from_bucket_name(self, "XXXXXXXXXXXXXXXXXXXXXXXX", "cdktest-cloudfrontbucket")),
                origin=origins.S3Origin(self.bucket),
                cache_behavior=cloudfront.CacheBehavior.is_default_cache_behavior(),
                viewer_protocol_policy=ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                # allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                # origin_request_policy=cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                # response_headers_policy=cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                # cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD_OPTIONS,
                # compress=False,
                # edge_lambdas=[
                #     cloudfront.EdgeLambda(
                #         function_version=_lambda.Version.from_version_arn(self, "LambdaEdgeVersion", lambda_fn.function_arn),
                #         event_type=cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST
                #     )
                # ]
            )
        )

        # WAF
        self.waf_webacl = waf.CfnWebACL(self, "cdktest-WAF",
            default_action=waf.CfnWebACL.DefaultActionProperty(allow={}),
            scope="CLOUDFRONT",
            visibility_config=waf.CfnWebACL.VisibilityConfigProperty(
                cloud_watch_metrics_enabled=True,
                metric_name="cdktest-WAF",
                sampled_requests_enabled=True
            )
        )

        # Elasticache - Redis
        self.cache_subnet = elasticache.CfnSubnetGroup( self, "cdktest-ElasticacheSubnetGroup",
            description="cdktest-ElasticacheSubnetGroup",
            subnet_ids=vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS).subnet_ids

        self.cache = elasticache.CfnCacheCluster( self, "cdktest-Elasticache",
            cluster_name="cdktest-Elasticache",
            engine="redis",
            # engine_version="7.1",
            cache_node_type="cache.t3.micro",
            num_cache_nodes=1,
            # vpc=vpc,
            cache_subnet_group_name=self.cache_subnet.ref,
            # vpc_security_group_ids=[ec2.SecurityGroup(self, "cdktest-ElasticacheSecurityGroup", vpc=vpc).security_group_id],
            removal_policy=RemovalPolicy.DESTROY,
        )

        # RDS
        self.db_cluster = rds( self, "cdktest-RDS",
            instance_identifier="cdktest-RDS",
            database_name="cdktest-RDS",
            # engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_28),
            # engine_version="8.0.28",
            # port=3306,

            # engine=rds.DatabaseClusterEngine.aurora_postgres(),
            engine=rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.VER_15_3),
            # port=5432
            
            # instance_class=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            # instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            instances=1,
            instance_props= rds.InstanceProps(
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
                vpc=vpc,
                security_groups=[ec2.SecurityGroup(self, "cdktest-RDSSecurityGroup", vpc=vpc)],
            ),
            vpc=vpc,
            # subnet_group=rds.SubnetGroup(self, "cdktest-RDSSubnetGroup", 
            #               vpc=vpc, description="cdktest-RDS Subnet Group", 
            #               vpc_subnets=rds.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)),
            # security_groups=[ec2.SecurityGroup(self, "cdktest-RDSSecurityGroup", vpc=vpc)],
            
            # credentials=rds.Credentials.from_generated_secret("cdktest-RDS"),
            # allocated_storage=20,
            # storage_type=rds.StorageType.GP3,
            # backup_retention=cdk.Duration.days(7),
            # deletion_protection=False,
            # publicly_accessible=False,
            # auto_minor_version_upgrade=True,
            # multi_az=True,
            # enable_performance_insights=True,
            # cloudwatch_logs_exports=["audit", "error", "general", "slowquery"],
            # monitoring_interval=cdk.Duration.seconds(60),
            # monitoring_role=None,
            
            removal_policy=RemovalPolicy.DESTROY,
        )
            
        
app = cdk.App()
CDKPythonStack(app, "SampleCdkStack") # env=cdk.Environment(account='102224384400', region='us-east-2')
app.synth()