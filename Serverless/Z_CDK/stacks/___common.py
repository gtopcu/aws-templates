
import aws_cdk as cdk

from aws_cdk import (
    Stack,
    Construct,
    RemovalPolicy,
    aws_iam as iam,
    aws_ssm as ssm,
    aws_secretsmanager as sm,
    aws_cloudwatch as cloudwatch,
    aws_sns as sns,
    aws_sns_subscriptions,
    CfnParameter
)
from constructs import Construct
import queue
from aws_cdk import aws_iam


class CommonStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # self.account
        # self.region
        # self.node
        # self.stack_id
        # self.stack_name
        # self.environment # aws://account/region
        # Stack.of(lambda_fn)
        # Stack.export_value(123, name="exported_value")  # Create a CloudFormation Export for a string value.
        #                                                 # Returns a string representing of Fn.importValue()
        # path = my_construct.node.path # Stack1/MyBucket

        # from aws_cdk.aws_s3_assets import Asset
        #api_definition = Asset(self, "ApiDefinitionAsset", path="./openapi/apiDefinition.yaml")  # deploy_time=False bundling=DOCKET

        # ------------------------------------------------------------------------------------------
        # Context variables
        # https://docs.aws.amazon.com/cdk/v2/guide/get_context_var.html
        # cdk.json/context, cdk.context.json 
        # construct.node.setContext() 

        # Setting during synth:
        # cdk synth -c bucket_name=mygroovybucket

        # Setting during deploy:
        # cdk deploy -c environment=production -c instanceType=t2.micro

        # Setting using cdk.json:
        # {
        #     "context": {
        #         "bucket_name": "myotherbucket"
        #     }
        # }

        # Retrieving within a Context/Stage (when self is available):
        # bucket_name = self.node.try_get_context("bucket_name")

        # Retrieving outside a Context/Stage (when self is not available):
        # app = cdk.App()
        # bucket_name = app.node.try_get_context("bucket_name")

        # Context methods (looks up from AWS account & caches in cdk.context.json if necessary)
        # HostedZone.fromLookup -> Gets the hosted zones in your account.
        # stack.availabilityZones -> Gets the supported Availability Zones.
        # StringParameter.valueFromLookup -> Gets a value from the current Region's Amazon EC2 Systems Manager Parameter Store.
        # Vpc.fromLookup -> Gets the existing Amazon Virtual Private Clouds in your accounts.
        # LookupMachineImage -> Looks up a machine image for use with a NAT instance in an Amazon Virtual Private Cloud.

        # ------------------------------------------------------------------------------------------
        
        # CloudFormation Parameters
        # Can provide CF params with cdk deploy command, or by specifying parameter values in your CDK project’s stack file:

        # cdk deploy --parameters uploadBucketName=uploadbucket -> if single stack
        # cdk deploy stack-logical-id --parameters stack-name:parameter-name=parameter-value -> if multi-stack

        # https://docs.aws.amazon.com/cdk/v2/guide/get_cfn_param.html
        # param_bucket_name = CfnParameter(self, "bucketName", type="String", default="my-bucket" description="S3 bucket name")

        # A CfnParameter instance exposes its value to your CDK app via a token. The parameter's token is resolved at 
        # synthesis time. But it resolves to a reference to the parameter defined in the AWS CloudFormation template 
        # (which will be resolved at deploy time), rather than to a concrete value.
        
        # You can retrieve the token as an instance of the Token class, or in string, string list, or numeric encoding. 
        # Your choice depends on the kind of value required by the class or method that you want to use the parameter with.

        # value	            Token class instance
        # value_as_list	    The token represented as a string list
        # value_as_number	The token represented as a number
        # value_as_string	The token represented as a string

        # bucket = Bucket(self, "amzn-s3-demo-bucket", bucket_name=param_bucket_name.value_as_string)

        # ------------------------------------------------------------------------------------------

        # Getting SysMgr ParamStore value during deployment - produces a token
        # https://docs.aws.amazon.com/cdk/v2/guide/get_ssm_value.html

        # aws ssm put-parameter --overwrite --name "parameter-name" --type "String" --value "parameter-value"
        # aws ssm put-parameter --overwrite --name "secure-parameter-name" --type "SecureString" --value "secure-parameter-value"

        # ssm.StringParameter.value_for_string_parameter(self, param_name)
        # ssm.StringParameter.value_for_string_parameter(self, param_name, version)
        # ssm.StringParameter.value_for_secure_string_parameter(self, param_name, version)

        # Getting SysMgr ParamStore value during synthesis
        # CF template will always use the same value instead of resolving the value during deployment
        # Only plain Systems Manager strings may be retrieved. Secure strings cannot be retrieved. 
        # The latest version will always be returned. Specific versions cannot be requested.

        # ssm.StringParameter.value_from_lookup(self, "my-plain-parameter-name")

        # ------------------------------------------------------------------------------------------

        # Getting secrets manager value
        # https://docs.aws.amazon.com/cdk/v2/guide/get_secrets_manager_value.html

        # aws secretsmanager create-secret --name ImportedSecret --secret-string mygroovybucket

        # sm.Secret.from_secret_attributes(self, "ImportedSecret",
        #     secret_complete_arn="arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>-<random-6-characters>",
        #         # If the secret is encrypted using a KMS-hosted CMK, either import or reference that key:
        #         # encryption_key=....
        #     )

        # ------------------------------------------------------------------------------------------    

        # SNS - using existing topics
        # topic = sns.Topic.from_topic_arn(self, "MyTopic", "XXX")
        # topic = sns.Topic.from_topic_attributes( self, "MyTopic", topic_arn="XXX")

        # SNS - creating new topics
        # topic = sns.Topic(self, "MyTopic",
        #     display_name="MyTopic",
        #     topic_name="MyTopic",   
        #     fifo=False,
        #     # content_based_deduplication=False,
        #     # enforce_ssl=False,
        #     # master_key=None,
        #     # signature_version="1",
        #     # logging_configs=None,
        #     # tracing_config=sns.TracingConfig.PASS_THROUGH, # sns.TracingConfig.ACTIVE
        # )
        # topic.apply_removal_policy(RemovalPolicy.DESTROY)
        
        # topic.grant_publish(iam.ServicePrincipal("events.amazonaws.com"))
        # topic.grant_subscribe(lambda_fn)
        # topic.add_to_resource_policy(aws_iam.PolicyStatement(
        #     actions=["sns:Publish"],
        #     principals=[iam.ServicePrincipal("events.amazonaws.com")],
        #     resources=[topic.topic_arn]
        # )

        # topic.add_logging_config(
        #         protocol=sns.LoggingProtocol.SQS,
        #         failure_feedback_role=role,
        #         success_feedback_role=role,
        #         success_feedback_sample_rate=50
        # )

        # topic.add_subscription(sns.Subscription(
        #     endpoint="XXX",
        #     protocol=sns.SubscriptionProtocol.HTTPS,
        #     raw_message_delivery=False,
        #     dead_letter_queue=None,
        #     filter_policy=None,
        #     subscription_role_arn=None
        # ))

        # topic.add_subscription(aws_sns_subscriptions.SqsSubscription(
        #     queue=queue,
        #     raw_message_delivery=False,
        #     dead_letter_queue=None,
        #     filter_policy=None
        # ))

        # topic.add_subscription(aws_sns_subscriptions.LambdaSubscription(
        #     function=lambda_fn,
        #     dead_letter_queue=None,
        #     filter_policy=None
        # )

        # ------------------------------------------------------------------------------------------
        
        # Creating a CW alarm
        # https://docs.aws.amazon.com/cdk/v2/guide/how_to_set_cw_alarm.html

        # Use an existing metric:
        # metric = queue.metric("ApproximateNumberOfMessagesVisible")

        # Create a custom metric:
        # metric = cloudwatch.Metric(
        #     namespace="MyNamespace",
        #     metric_name="MyMetric",
        #     dimensionsMap=dict(MyDimension="MyDimensionValue")
        # )

        # # Create the alarm from metric:
        # alarm = metric.create_alarm(self, "Alarm",
        #     alarm_description="Number of pending messages in the queue",
        #     threshold=100,
        #     evaluation_periods=3,
        #     datapoints_to_alarm=2,
        #     # actions_enabled=True,,
        #     # comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD, # LESS_THAN_THRESHOLD
        #     # evaluate_low_sample_count_percentile=cloudwatch.EvaluateLowSampleCountPercentile.DISABLED,
        #     treat_missing_data=cloudwatch.TreatMissingData.NOT_BREACHING,
        # )
        # alarm.add_alarm_action(cloudwatch.AlarmAction(sns.Topic.from_topic_arn(self, "MyTopic", "XXX")))
        # alarm.add_ok_action(cloudwatch.AlarmAction(sns.Topic.from_topic_arn(self, "MyTopic", "XXX")))
        # alarm.add_insufficient_data_action(cloudwatch.AlarmAction(sns.Topic.from_topic_arn(self, "MyTopic", "XXX")))

        # Create the alarm manually:
        # alarm = cloudwatch.Alarm(self, "Alarm",
        #     metric=metric,
        #     threshold=100,
        #     evaluation_periods=3,
        #     datapoints_to_alarm=2
        # )

        # ------------------------------------------------------------------------------------------

        # Create a log group, metric filter & alarm

        # log_group = cloudwatch.LogGroup(self, "LogGroup")

        # mf = cloudwatch.MetricFilter(self, "MetricFilter",
        #     log_group=log_group,
        #     metric_namespace="MyApp",
        #     metric_name="Latency",
        #     filter_pattern=cloudwatch.FilterPattern.exists("$.latency"),
        #     metric_value="$.latency",
        #     dimensions={
        #         "ErrorCode": "$.errorCode"
        #     },
        #     unit=cloudwatch.Unit.MILLISECONDS
        # )

        # # expose a metric from the metric filter
        # metric = mf.metric()

        # you can use the metric to create a new alarm
        # alarm = cloudwatch.Alarm(self, "Alarm from metric filter",
        #     alarm_description="Integration latency on the API GW alarm",
        #     metric=metric,
        #     threshold=100,
        #     evaluation_periods=3,
        #     datapoints_to_alarm=2,
        #     # comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD, # LESS_THAN_THRESHOLD
        #     # evaluate_low_sample_count_percentile=cloudwatch.EvaluateLowSampleCountPercentile.DISABLED,
        #     # treat_missing_data=cloudwatch.TreatMissingData.NOT_BREACHING,
        # )
        # alarm.add_alarm_action(cloudwatch.AlarmAction(sns.Topic.from_topic_arn(self, "MyTopic", "XXX")))
        # alarm.add_ok_action(cloudwatch.AlarmAction(sns.Topic.from_topic_arn(self, "MyTopic", "XXX")))
        # alarm.add_insufficient_data_action(cloudwatch.AlarmAction(sns.Topic.from_topic_arn(self, "MyTopic", "XXX")))


        # ------------------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------