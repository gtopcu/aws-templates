
import boto3

dynamodb = boto3.client('dynamodb')

table1 = 'table1'
table2 = 'table2'

# Step 1: Scan table1
paginator = dynamodb.get_paginator('execute_statement')
scan_stmt = f"SELECT * FROM \"{table1}\""

for page in paginator.paginate(Statement=scan_stmt):
    for item in page['Items']:
        # Step 2: Insert into table2 using PartiQL
        insert_stmt = f"INSERT INTO \"{table2}\" VALUE ?"
        dynamodb.execute_statement(Statement=insert_stmt, Parameters=[item])
