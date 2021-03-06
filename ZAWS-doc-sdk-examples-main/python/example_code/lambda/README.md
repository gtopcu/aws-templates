# AWS Lambda examples

## Purpose

Shows how to use the AWS SDK for Python (Boto3) to create, deploy, and invoke 
AWS Lambda functions. Learn to accomplish the following tasks:

* Create and deploy Lambda functions that can be invoked in different ways:
    * By an invoke call through Boto3
    * By Amazon API Gateway as the target of a REST request
    * By Amazon EventBridge on a schedule
* Create and deploy a REST API on Amazon API Gateway. The REST API targets a 
Lambda function to handle REST requests.
* Create a scheduled rule on Amazon EventBridge that targets a Lambda function.

These examples show how to use the low-level Boto3 client APIs to accomplish tasks
like creating a REST API and setting an event schedule. You can also use
[AWS Chalice](https://github.com/aws/chalice)
to achieve similar results more easily and with additional features. 

*Lambda lets you run code without provisioning or managing servers. Upload your code 
and Lambda takes care of everything required to run and scale your code with high 
availability.*

## Code examples

### Cross-service examples

* [Use scheduled EventBridge events to invoke a function](scheduled_lambda.py)
* [Use API Gateway to invoke a function](api_gateway_rest.py)

### Scenario examples

* [Deploy and invoke a function](lambda_basics.py)

### API examples

* [Create a function](lambda_basics.py)
(`CreateFunction`)
* [Delete a function](lambda_basics.py)
(`DeleteFunction`)
* [Invoke a function](lambda_basics.py)
(`Invoke`)

## ⚠ Important

- As an AWS best practice, grant this code least privilege, or only the 
  permissions required to perform a task. For more information, see 
  [Grant Least Privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 
  in the *AWS Identity and Access Management 
  User Guide*.
- This code has not been tested in all AWS Regions. Some AWS services are 
  available only in specific Regions. For more information, see the 
  [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
  on the AWS website.
- Running this code might result in charges to your AWS account.

## Running the code

### Prerequisites

- You must have an AWS account, and have your default credentials and AWS Region
  configured as described in the [AWS Tools and SDKs Shared Configuration and
  Credentials Reference Guide](https://docs.aws.amazon.com/credref/latest/refdocs/creds-config-files.html).
- Python 3.8.5 or later
- Boto3 1.15.4 or later
- PyTest 5.3.5 or later (to run unit tests)
- Requests 2.23.0 or later

### Command

There are three demonstrations in this set of examples. The first creates a
Lambda function and invokes it through Boto3. The second creates an 
Amazon API Gateway REST API and makes the Lambda function the target of REST 
requests. The third creates an Amazon EventBridge rule that invokes the Lambda 
function on a schedule.

#### Boto3 invocation 

Run this example at a command prompt with the following command:

```
python lambda_basics.py
``` 

#### REST API target

Run this example at a command prompt with the following command:

```
python api_gateway_rest.py
``` 

#### Scheduled event target

Run this example at a command prompt with the following command:

```
python scheduled_lambda.py
``` 

### Example structure

The examples are divided into the following files:

**api_gateway_rest.py**

Shows how to create and use an Amazon API Gateway REST API that targets a 
Lambda function.

* Deploys a Lambda function.
* Creates an Amazon API Gateway REST API.
* Creates a REST resource that targets the Lambda function.
* Grants permission to let Amazon API Gateway invoke the Lambda function.
* Uses the Requests package to send requests to the REST API.
* Cleans up all resources created during the demo. 

**lambda_basics.py**

Shows how to deploy and invoke a Lambda function with Boto3.

* Deploys a Lambda function.
* Invokes the function using Boto3 API calls.
* Cleans up all resources created during the demo. 

**lambda_handler_basic.py**

A Lambda function that handles invocation from Boto3.  

**lambda_handler_rest.py**

A Lambda function that handles invocation as a REST API target from Amazon
API Gateway.

**lambda_handler_scheduled.py**

A Lambda function that handles scheduled invocation from Amazon EventBridge.

**scheduled_lambda.py**

Shows how to register a Lambda function as the target of a scheduled Amazon
EventBridge event.

* Deploys a Lambda function.
* Creates an Amazon EventBridge scheduled event and makes the function the target.
* Grants permission to let Amazon EventBridge invoke the Lambda function.
* Prints the latest Amazon CloudWatch logs to show the result of the scheduled 
  invocations.
* Cleans up all resources created during the demo.

## Running the tests

The unit tests in this module use the botocore Stubber. This captures requests before 
they are sent to AWS, and returns a mocked response. To run all of the tests, 
run the following in your [GitHub root]/python/example_code/lambda 
folder.

```    
python -m pytest
```

## Additional information

- [Boto3 Lambda service reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html)
- [Boto3 Amazon API Gateway service reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html)
- [Amazon EventBridge service reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html)
- [Amazon CloudWatch Logs service reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html)
- [AWS Chalice](https://github.com/aws/chalice)
---
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
