#!/bin/bash

# wait for the AppSync API to be deployed
sleep 30

# Set the AWS region
REGION="eu-west-2"  # Replace with your desired region

# Retrieve the current AppSync API ID
API_ID=$(aws appsync list-graphql-apis --region $REGION --query 'graphqlApis[0].apiId' --output text)

# Check if API_ID is retrieved
if [ -z "$API_ID" ]; then
  echo "No AppSync API found."
  exit 1
fi

echo "AppSync API ID: $API_ID"

# Retrieve the current API name
API_NAME=$(aws appsync list-graphql-apis --region $REGION --query 'graphqlApis[0].name' --output text)

# Check if API_NAME is retrieved
if [ -z "$API_NAME" ]; then
  echo "No AppSync API name found."
  exit 1
fi

echo "AppSync API Name: $API_NAME"

# Retrieve the current schema
aws appsync get-introspection-schema --api-id $API_ID --region $REGION --format SDL schema.graphql

# Update the schema with a trivial but noticeable change (adding a comment)
echo "# Updated on $(date)" >> schema.graphql

# Update the API with the modified schema
aws appsync start-schema-creation --api-id $API_ID --region $REGION --definition file://schema.graphql

echo "AppSync API schema updated successfully."
