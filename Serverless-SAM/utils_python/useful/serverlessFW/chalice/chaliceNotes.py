
# https://aws.github.io/chalice/index
# https://aws.amazon.com/blogs/developer/aws-chalice-now-supports-yaml-templates/

## Custom Domain Names:
# https://aws.github.io/chalice/tutorials/customdomain.html

# python3 -m venv venv
# source venv/bin/activate
# pip install chalice -U

# https://github.com/TestBoxLab/chalice-spec
# pip install chalice_spec apispec pydantic

# from chalice_spec import ChaliceWithSpec, PydanticPlugin, Operation, Docs
# from apispec import APISpec
# from pydantic import BaseModel, Field

# chalice new-project chalicedemoapp
# chalice deploy
# chalice local -> http://localhost:8000/
# chalice invoke index --log-level debug --raw-json '{"hello": "world"}' --stage dev
# chalice delete
# chalice update-project-config --autogen-policy --no-autogen-policy --autogen-iam --no-autogen-iam
# chalice generate-models

# $ cat .chalice/config.json
# {
#   "version": "2.0",
#   "app_name": "customdomain",
#   "api_gateway_endpoint_type": "REGIONAL",
#   "stages": {
#     "dev": {
#       "api_gateway_stage": "api"
#     }
#   }
# }

# $ curl https://xxxxx.execute-api.us-west-2.amazonaws.com/api/ -> {"hello": "world"}

import json, gzip

from chalice import Chalice, Rate, Cron, Response, CORSConfig
from chalice import NotFoundError
# NotFoundError, BadRequestError, UnauthorizedError, ForbiddenError, ConflictError, UnprocessableEntityError 
# TooManyRequestsError, RequestTimeoutError, InternalServerError, ChaliceViewError, ChaliceDeprecationWarning
# ChaliceUnhandledError, ChaliceViewWarning

# * BadRequestError - return a status code of 400
# * UnauthorizedError - return a status code of 401
# * ForbiddenError - return a status code of 403
# * NotFoundError - return a status code of 404
# * ConflictError - return a status code of 409
# * UnprocessableEntityError - return a status code of 422
# * TooManyRequestsError - return a status code of 429
# * ChaliceViewError - return a status code of 500

# https://aws.github.io/chalice/topics/authorizers.html#
from chalice import IAMAuthorizer, CognitoUserPoolAuthorizer, CustomAuthorizer

app = Chalice(app_name="chalicedemoapp", debug=True, configure_logs=True)
# app.api.cors = True
# app.api.binary_types.append('application/json')
# app.debug = True 

# spec = APISpec(title="chalicedemoapp_api", version="1.0", openapi_version="3.0", plugins=[PydanticPlugin()])
# app = ChaliceWithSpec(app_name="chalicedemoapp", spec=spec)

# https://aws.github.io/chalice/api.html#testing
# from chalice.test import Client
# with Client(app) as client:
#     result = client.http.post("/my-data")

authorizer = IAMAuthorizer()
# authorizer = CognitoUserPoolAuthorizer('MyPool', provider_arns=['arn:aws:cognito:...:userpool/name'])
# authorizer = CustomAuthorizer(
#     'MyCustomAuth', header='Authorization',
#     authorizer_uri=('arn:aws:apigateway:region:lambda:path/2015-03-31'
#                     '/functions/arn:aws:lambda:region:account-id:'
#                     'function:FunctionName/invocations'))

# cors_config = CORSConfig(
#     allow_origin='https://foo.example.com',
#     allow_headers=['X-Special-Header'],
#     max_age=600,
#     expose_headers=['X-Special-Header'],
#     allow_credentials=True
# )

# class MyData(BaseModel):
#     name: str = Field(min_length=1, max_length=10)
#     age: int = Field(ge=0, le=100)

# @app.route('/openapi/{api_no}', methods=["GET"], docs=Docs(
#     post=Operation(request=None, response=MyData) # parameters=[], tags=[], summary='', description='')
# ))
# def openapi():
#     """
#     Retrieve a user object
#     User's can't retrieve other users using this endpoint - only themselves
#     """
#     data = MyData(name='John', age=20)
#     # data:MyData = MyData.model_validate(app.current_request.json_body)
#     return data

@app.route("/") #, cors_config=cors_config)
def index():
    return {"hello": "world"}

@app.route('/cities/{city}', methods=['GET'], authorizer=authorizer)
def get_city(city):
    if city == '1':
        raise NotFoundError("city not found")
    return {'city no': city}

@app.route('/info')
def myview():
    return app.current_request.to_dict()
    # request = app.current_request
    # request.query_params - A dict of the query params
    # request.headers - A dict of the request headers
    # request.uri_params - A dict of the captured URI params
    # request.method - The HTTP method (as a string)
    # request.json_body - The parsed JSON body
    # request.raw_body - The raw HTTP body as bytes
    # request.context - A dict of additional context information
    # request.stage_vars - Configuration for the API Gateway stage

# @app.route('/text')
# def text_response():
#     return Response(body='hello world!',
#                     status_code=200,
#                     headers={'Content-Type': 'text/plain'})

# app.api.binary_types.append('application/json')
# @app.route('/')
# def binary_response():
#     blob = json.dumps({'hello': 'world'}).encode('utf-8')
#     payload = gzip.compress(blob)
#     custom_headers = {
#         'Content-Type': 'application/json',
#         'Content-Encoding': 'gzip'
#     }
#     return Response(body=payload,
#                     status_code=200,
#                     headers=custom_headers)


# @app.schedule(Rate(5, unit=Rate.MINUTES))
# def periodic_task(event):
#     return {"hello": "world"}


# --------------------------------------------------------------------------------------------------
# Events

# app.on_cw_event('my_event', lambda event: print(event))
# app.on_sns_message('my_topic', lambda event: print(event))
# app.on_sqs_message('my_queue', lambda event: print(event))
# app.on_dynamodb_record('my_table', lambda event: print(event))
# app.on_kinesis_record('my_stream', lambda event: print(event))
# app.on_ws_connect(lambda event: print(event))
# app.on_ws_message(lambda event: print(event))
# app.on_ws_disconnect(lambda event: print(event))
# @app.on_s3_event(bucket='mybucket')

# def s3_handler(event):
#     print(event.bucket, event.key, event.metadata, event.src_path)
 
# @app.on_sns_message(topic='MyDemoTopic')
# def handle_sns_message(event):
#     app.log.debug("Received message with subject: %s, message: %s",
#                   event.subject, event.message)

# --------------------------------------------------------------------------------------------------
# WebSockets

# from boto3.session import Session
# from chalice import Chalice

# from chalicelib import Storage
# from chalicelib import Sender
# from chalicelib import Handler

# app = Chalice(app_name="chalice-chat-example")
# app.websocket_api.session = Session()
# app.experimental_feature_flags.update([
#     'WEBSOCKETS'
# ])

# STORAGE = Storage.from_env()
# SENDER = Sender(app, STORAGE)
# HANDLER = Handler(STORAGE, SENDER)

# @app.on_ws_connect()
# def connect(event):
#     STORAGE.create_connection(event.connection_id)

# @app.on_ws_disconnect()
# def disconnect(event):
#     STORAGE.delete_connection(event.connection_id)

# @app.on_ws_message()
# def message(event):
#     HANDLER.handle(event.connection_id, event.body)

# --------------------------------------------------------------------------------------------------