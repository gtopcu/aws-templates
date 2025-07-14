
from datetime import datetime

# Monitor concurrency usage
def check_concurrency_metrics():
    cloudwatch = boto3.client('cloudwatch')
    
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Lambda',
        MetricName='ConcurrentExecutions',
        Dimensions=[],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Maximum']
    )
    
    return response['Datapoints']

