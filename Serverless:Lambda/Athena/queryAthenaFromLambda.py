#
# https://www.youtube.com/watch?v=a_Og1t3ULOI
#
# IAM Permissions
# ------------------------------------
# athena:StartQueryExecution
# athena:GetQueryExecution
# athena:GetQueryResults
# glue:GetTable
#

import json
import boto3
import time

def lambda_handler(event, context):
    
    client = boto3.client("athena")

    # Setup and perform query
    queryStart = client.start_query_execution(
        QueryString = "SELECT * FROM athena_simplified_athena_demo LIMIT 10;",
        QueryExecutionContext = {
            "Database" : "default"
        },
        ResultConfiguration = {
            "OutputLocation" : "s3://aws-simplified-results/"
        }
    )

    # Start the query
    queryId = queryStart["queryExecutionId"]

    # Athena executes the query async, give some time
    time.sleep(15)

    # Check the results
    results = client.get_query_results(QueryExecutionId = queryId)
    for row in results["ResultSet"]["Rows"]:
        print(row)






