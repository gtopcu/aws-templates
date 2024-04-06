

//https://medium.com/@engin.linux/how-to-build-a-serverless-backend-api-via-aws-lambda-dynamodb-api-gateway-in-15-minutes-level-24fcff3f113d

/*

{
  "resource": "/meals",
  "path": "/meals",
  "httpMethod": "GET"
}

*/

import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, ScanCommand } from '@aws-sdk/lib-dynamodb';

// Create the DynamoDB client
const ddbClient = new DynamoDBClient({ region: 'eu-central-1' });

// Create the DynamoDB Document client
const docClient = DynamoDBDocumentClient.from(ddbClient);

// The handler function is exported using ES Modules syntax
export async function handler() {
    // Define the parameters for the scan operation
    const params = {
        TableName: 'Meals',
    };
    
    try {
        // Use the ScanCommand to get all items from the DynamoDB table
        const data = await docClient.send(new ScanCommand(params));

        // Successful response with the items
        return {
            statusCode: 200,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: 'Retrieved all meals successfully!',
                meals: data.Items,
            }),
        };
    } catch (error) {
        console.error('Error retrieving meals:', error);
        // Error response
        return {
            statusCode: 500,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: 'Failed to retrieve meals',
                error: error.message,
            }),
        };
    }
}