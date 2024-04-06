
# https://mangum.io/
# https://www.youtube.com/watch?v=7-CvGFJNE_o
# pip install mangum

"""
- Mangum is an adapter for running ASGI applications in AWS Lambda to handle Function URL, 
API Gateway, ALB, and Lambda@Edge events.

- Compatibility with ASGI application frameworks, such as Starlette, FastAPI, Quart and Django.

- Support for binary media types and payload compression in API Gateway using GZip or Brotli.

- Works with existing deployment and configuration tools, including Serverless Framework and AWS SAM.

- Startup and shutdown lifespan events.

"""
# ----------------------------------------------------------------------------------------------------
# Plain

# from mangum import Mangum

# async def app(scope, receive, send):
#     await send(
#         {
#             "type": "http.response.start",
#             "status": 200,
#             "headers": [[b"content-type", b"text/plain; charset=utf-8"]],
#         }
#     )
#     await send({"type": "http.response.body", "body": b"Hello, world!"})

# handler = Mangum(app, lifespan="off")


# ----------------------------------------------------------------------------------------------------
# Adapter

# handler = Mangum(
#     app,
#     lifespan="auto",
#     api_gateway_base_path=None,
#     custom_handlers=None,
#     text_mime_types=None,
# )

# ----------------------------------------------------------------------------------------------------
# With Fast API

# from fastapi import FastAPI
# from mangum import Mangum

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# handler = Mangum(app, lifespan="off")

# ----------------------------------------------------------------------------------------------------
# Custom event handling

# def handler(event, context):
#     if event.get("some-key"):
#         # Do something or return, etc.
#         return

#     asgi_handler = Mangum(app)
#     response = asgi_handler(event, context) # Call the instance with the event arguments

#     return response

# ----------------------------------------------------------------------------------------------------
# Retrieving the AWS event and context

# from fastapi import FastAPI
# from mangum import Mangum
# from starlette.requests import Request

# app = FastAPI()

# scope['aws.event']
# scope['aws.context']

# @app.get("/")
# def hello(request: Request):
#     return {"aws_event": request.scope["aws.event"]}

# handler = Mangum(app)

# ----------------------------------------------------------------------------------------------------
# GZip Middleware

# from fastapi import FastAPI
# from fastapi.middleware.gzip import GZipMiddleware
# from mangum import Mangum

# app = FastAPI()
# app.add_middleware(GZipMiddleware, minimum_size=1000)


# @app.get("/")
# async def main():
#     return "somebigcontent"

# handler = Mangum(app, TEXT_MIME_TYPES=["application/vnd.some.type"])

# ----------------------------------------------------------------------------------------------------
# Lifespan

# from mangum import Mangum
# from fastapi import FastAPI

# app = FastAPI()


# @app.on_event("startup")
# async def startup_event():
#     pass

# @app.on_event("shutdown")
# async def shutdown_event():
#     pass

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# handler = Mangum(app, lifespan="auto")


