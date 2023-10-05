# Amazon SNS to AWS Lambda

The SAM template deploys a Lambda function, an SNS topic and the IAM permissions required to run the application. SNS invokes the Lambda function when new messages are available. When messages are sent to the SNS topic, they are delivered as a JSON event payload (see above) to the Lambda function.

Learn more about this pattern at  Serverless Land Patterns: https://serverlessland.com/patterns/sns-lambda.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sns-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Example event payload from SNS to Lambda

```
{
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-1:123456789012:patterns-sns-to-lambda-MySnsTopic-1234567890:9c455abd-0da9-4d55-ac43-1234567890",
            "Sns": {
                "Type": "Notification",
                "MessageId": "df90a393-86bb-5f13-8312-1234567890",
                "TopicArn": "arn:aws:sns:us-east-1:123456789012:patterns-sns-to-lambda-MySnsTopic-1JEVSWADZEW1B",
                "Subject": null,
                "Message": "test",
                "Timestamp": "2021-02-10T12:18:09.667Z",
                "SignatureVersion": "1",
                "Signature": "RMgNCIuj1234567890fI/abcd/0i3edr4Uw1234567890XZkW1fU5j7oezS+SPawv1234567890QaUPckgF28iQ6TwO4UlMJgpO0YybegxYTOls5vroO67cmXPc1yP+GDHoxHDmrZflxNssFUVVPUVrogUjN/g8I7eDb4AcLxVSV21234567890g8bURsZKM/4BUc4Y1234567890u5CHmcYGZ2ygYIzrOBdMbpNiQ1234567890yI2Fo5i3PfULQMszBpy1234567890pEZnUr6G9sBR3+WG7CMfCqK6sgVhlYc5SkADtO2NQCjtoa2yMZHkynm3P1eV22XCLiA==",
                "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-123456789012345678901234567890.pem",
                "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:patterns-sns-to-lambda-MySnsTopic-1234567890:1234567890-0da9-4d55-ac43-1234567890",
                "MessageAttributes": {}
            }
        }
    ]
}
```
### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SNS topic and observe the event delivered to the Lambda function:

1. Send the SNS message:

```bash
aws sns publish --topic-arn ENTER_SNS_TOPIC_ARN FROM_OUTPUT --subject testSubject --message testMessage
```
2. Retrieve the logs from the Lambda function:
```bash
sam logs -n ENTER_YOUR_CONSUMER_FUNCTION_NAME
```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0