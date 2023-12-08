import json
from typing import Any, Dict, Optional

from aws_lambda_powertools.utilities.typing import LambdaContext


def generate_context() -> LambdaContext:
    context = LambdaContext()
    context._aws_request_id = "111111"
    context._function_name = "func"
    context.memory_limit_in_mb = 128
    return context

def generate_api_gw_rest_event(
        body: Optional[Dict[str, Any]] = None, 
        authorized: Optional[bool] = True
    ) -> Dict[str, Any]:
    
    return {
        "version": "1.0",
        "resource": "/my/path",
        "path": "/my/path",
        "httpMethod": "POST",
        "headers": {"Header1": "value1", "Header2": "value2"},
        "multiValueHeaders": {
            "Header1": ["value1"],
            "Header2": ["value1", "value2"],
        },
        "queryStringParameters": {
            "parameter1": "value1",
            "parameter2": "value",
        },
        "multiValueQueryStringParameters": {
            "parameter1": ["value1", "value2"],
            "parameter2": ["value"],
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "id",
            "authorizer": {
                "claims": {"sub": "123"} if authorized else None,
                "scopes": None,
            },
            "domainName": "id.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "id",
            "extendedRequestId": "request-id",
            "httpMethod": "POST",
            "identity": {
                "accessKey": None,
                "accountId": None,
                "caller": None,
                "cognitoAuthenticationProvider": None,
                "cognitoAuthenticationType": None,
                "cognitoIdentityId": None,
                "cognitoIdentityPoolId": None,
                "principalOrgId": None,
                "sourceIp": "192.168.0.1/32",
                "user": None,
                "userAgent": "user-agent",
                "userArn": None,
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT",
                    },
                },
            },
            "path": "/my/path",
            "protocol": "HTTP/1.1",
            "requestId": "id=",
            "requestTime": "04/Mar/2020:19:15:17 +0000",
            "requestTimeEpoch": 1583349317135,
            "resourceId": None,
            "resourcePath": "/my/path",
            "stage": "$default",
        },
        "pathParameters": None,
        "stageVariables": None,
        "body": "Hello from Lambda!" if body is None else json.dumps(body),
        "isBase64Encoded": False,
    }
