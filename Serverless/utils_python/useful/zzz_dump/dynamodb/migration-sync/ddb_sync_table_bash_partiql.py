
"""
Export - outputs items(no metadata) as DDB JSON:

aws dynamodb scan \
  --table-name table1 \
  --output json \
  --query "Items" > dump.json

--------------------------------------------------------------------------------------------------------------------
# Import - 1
sudo apt install jq / brew install jq
  
#!/bin/bash
TABLE_NAME="table2"

for row in $(jq -c '.[]' dump.json); do
  aws dynamodb put-item \
    --table-name "$TABLE_NAME" \
    --item "$row"
done

--------------------------------------------------------------------------------------------------------------------
# Import - 2
# Using batch-write - 25 items max

sudo apt install jq / brew install jq

#!/bin/bash
INPUT_FILE="dump.json"
TABLE_NAME="table2"
BATCH_FILE="batch.json"

# Install jq if not available
command -v jq >/dev/null 2>&1 || { echo >&2 "jq is required but not installed. Aborting."; exit 1; }

# Split the items into chunks of 25
TOTAL=$(jq length "$INPUT_FILE")
INDEX=0

echo "Importing $TOTAL items into $TABLE_NAME..."

while [ $INDEX -lt $TOTAL ]; do
  BATCH=$(jq ".[$INDEX:$((INDEX+25))] | map({ PutRequest: { Item: . } })" "$INPUT_FILE")
  echo "{ \"$TABLE_NAME\": $BATCH }" > "$BATCH_FILE"

  aws dynamodb batch-write-item --request-items file://"$BATCH_FILE"

  INDEX=$((INDEX + 25))
done

echo "Import complete."
rm "$BATCH_FILE"


"""

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
