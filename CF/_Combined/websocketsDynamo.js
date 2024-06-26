{
  "Resources": {
    "ChaliceChatTable": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "AttributeDefinitions": [
          {
            "AttributeName": "PK",
            "AttributeType": "S"
          },
          {
            "AttributeName": "SK",
            "AttributeType": "S"
          }
        ],
        "KeySchema": [
          {
            "AttributeName": "PK",
            "KeyType": "HASH"
          },
          {
            "AttributeName": "SK",
            "KeyType": "RANGE"
          }
        ],
        "GlobalSecondaryIndexes": [
          {
            "IndexName": "ReverseLookup",
            "KeySchema": [
              {
                "AttributeName": "SK",
                "KeyType": "HASH"
              },
              {
                "AttributeName": "PK",
                "KeyType": "RANGE"
              }
            ],
            "Projection": {
              "ProjectionType": "ALL"
            },
            "ProvisionedThroughput": {
              "ReadCapacityUnits": 1,
              "WriteCapacityUnits": 1
            }
          }
        ],
        "ProvisionedThroughput": {
          "ReadCapacityUnits": 1,
          "WriteCapacityUnits": 1
        },
        "TableName": "ChaliceChat"
      }
    },
    "WebsocketConnect": {
      "Properties": {
        "Environment": {
          "Variables": {
            "TABLE": {
              "Ref": "ChaliceChatTable"
            }
          }
        }
      }
    },
    "WebsocketMessage": {
      "Properties": {
        "Environment": {
          "Variables": {
            "TABLE": {
              "Ref": "ChaliceChatTable"
            }
          }
        }
      }
    },
    "WebsocketDisconnect": {
      "Properties": {
        "Environment": {
          "Variables": {
            "TABLE": {
              "Ref": "ChaliceChatTable"
            }
          }
        }
      }
    },
    "DefaultRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "lambda.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Policies": [
          {
            "PolicyName": "DefaultRolePolicy",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                  ],
                  "Resource": "arn:aws:logs:*:*:*"
                },
                {
                  "Effect": "Allow",
                  "Action": [
                    "execute-api:ManageConnections"
                  ],
                  "Resource": "arn:aws:execute-api:*:*:*/@connections/*"
                },
                {
                  "Effect": "Allow",
                  "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:PutItem",
                    "dynamodb:GetItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:Query",
                    "dynamodb:Scan"
                  ],
                  "Resource": [
                    {
                      "Fn::Sub": "arn:aws:dynamodb:${AWS::Region}:${AWS::AccountId}:table/${ChaliceChatTable}"
                    },
                    {
                      "Fn::Sub": "arn:aws:dynamodb:${AWS::Region}:${AWS::AccountId}:table/${ChaliceChatTable}/index/ReverseLookup"
                    }
                  ]
                }
              ]
            }
          }
        ]
      }
    }
  }
}