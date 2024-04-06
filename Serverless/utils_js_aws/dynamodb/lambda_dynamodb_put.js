

// https://medium.com/@engin.linux/how-to-build-a-serverless-backend-api-via-aws-lambda-dynamodb-api-gateway-in-15-minutes-level-24fcff3f113d
/*

{
  "body": "{\"mealName\": \"Chicken Salad Sandwich\"}",
  "resource": "/meal",
  "path": "/meal",
  "httpMethod": "POST"
}
*/

import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';
import { randomUUID } from 'crypto';

// Create the DynamoDB client
const ddbClient = new DynamoDBClient({ region: 'eu-central-1' });

// Create the DynamoDB Document client
const docClient = DynamoDBDocumentClient.from(ddbClient);

// The handler function is exported using ES Modules syntax
export async function handler(event) {
    // Parse the JSON object from the event body
    const requestBody = JSON.parse(event.body);
    const mealName = requestBody.mealName;

    // Generate a UUIDv4 and an ISO8601 UTC timestamp
    const id = randomUUID();
    const creationTimestamp = new Date().toISOString();

    // Define the DynamoDB table entry to be created
    const params = {
        TableName: 'Meals',
        Item: {
            'id': id,
            'mealName': mealName,
            'creationTimestamp': creationTimestamp,
        },
    };
    
    // Put new entry on the DynamoDB table
    await docClient.send(new PutCommand(params));
    
    // Successful response
    return {
        statusCode: 201,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: 'Meal added successfully!',
            mealId: id,
        }),
    };
}