
from datetime import datetime, timezone, timedelta
import boto3


# Monitor concurrency usage
def check_concurrency_metrics():
    cloudwatch = boto3.client('cloudwatch')
    
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Lambda',
        MetricName='ConcurrentExecutions',
        Dimensions=[],
        StartTime=datetime.now(timezone.utc) - timedelta(minutes=5),
        EndTime=datetime.now(timezone.utc),
        Period=300,
        Statistics=['Maximum']
    )
    
    return response['Datapoints']


# Set reserved concurrency for critical functions
def set_reserved_concurrency(function_name, reserved_concurrency):
    lambda_client = boto3.client('lambda')
    
    lambda_client.put_reserved_concurrency_setting(
        FunctionName=function_name,
        ReservedConcurrencyLimit=reserved_concurrency
    )