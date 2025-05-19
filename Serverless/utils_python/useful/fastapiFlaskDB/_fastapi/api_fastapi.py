
# https://www.youtube.com/watch?v=C-bie4ZY_o0
# https://www.youtube.com/watch?v=iWS9ogMPOI0
# https://www.youtube.com/watch?v=_Y3uAFVYk5I
# https://www.youtube.com/watch?v=0A_GCXBCNUQ
# https://fastapi.tiangolo.com/tutorial/response-model/

# pip install fastapi
# pip install python-multipart # -> for File/UploadFile
# pip install "uvicorn[standard]"

# python3 -m venv .venv
# source venv/bin/activate

# uvicorn api_fastapi:app --reload
# http://127.0.0.1:8000/docs

"""
check launch.json for debugging

"""

from datetime import datetime
import time
from typing import Any

from typing import Annotated
from fastapi import FastAPI, APIRouter, Request, status, HTTPException
from fastapi.responses import Response, HTMLResponse, JSONResponse, PlainTextResponse
from fastapi import File, UploadFile, Body, Path, Query, Cookie, Header


# FileResponse, PlainTextResponse, RedirectResponse,  StreamingResponse
# from fastjsonschema import validate, exceptions
# from fastapi.exceptions import RequestValidationError
# from fastapi.exception_handlers import (
#     http_exception_handler,
#     request_validation_exception_handler,
# )
# from starlette.exceptions import HTTPException as StarletteHTTPException
# from fastapi.encoders import jsonable_encoder

# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory="static"), name="static")

# from _customRouter import router
# app.include_router(router)

# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware( 
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# #     expose_headers=["*"],
# #     max_age=3600,
# #     # origins=["XXXXXXXXXX"],
# )

from pydantic import BaseModel, Field
class ToDo(BaseModel):
    id: int = Field(default=0)
    title: str = Field(default="", description="Mr/Mrs/Ms")
    updated: datetime = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# FastAPI is async by default (Flask is not)
app = FastAPI()

items = [ToDo(id=1, title="Buy milk"), ToDo(id=2, title="Buy bread")]

# app.add_exception_handler(HTTPException, exceptionHandler, exc: exc.detail)

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )

# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)


@app.get("/") # response_model=None, response_model_exclude_unset=True
async def root(request: Request) -> Any: # background_tasks: BackgroundTasks
    # request.base_url
    # request.path_params
    # request.method
    # request.headers
    # request.auth
    # request.query_params
    # await some_async_func()
    return str(request.base_url)
    # return {"message": "Hello World"}
    # return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # return JSONResponse(content={"message": "Here's your interdimensional portal."})
    # background_tasks.add_task(write_notification, email, message="some notification")

# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)

# @app.get("/items/{item_id}")
# async def get_item(item_id: int, query_str: str = None) -> Any:
#     return {"item_id": item_id, "query_str": query_str}

# http://127.0.0.1:8000/items?limit=2
@app.get("/items", response_model=list[ToDo])
async def list_items(request: Request, limit:int = 10): #skip: int | None) -> Any:
    return items[0:limit]

@app.get("/items/{item_id}", response_model=ToDo)
async def get_item(item_id: int) -> Any:
    if(item_id < len(items)):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "Not found"})
        # return {"message": "Item not found"}

@app.post("/items", response_model=ToDo, status_code=status.HTTP_201_CREATED, tags=["items"])
async def create_item(request: Request, item: ToDo) -> Any:
    items.append(item)
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["items"])
async def delete_item(request: Request, item_id: int) -> None:
    items = [item for item in items if item.id is not item_id]
    

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)) -> Any:
    contents = await file.read()
    # print(contents)
    print("File uploaded: ", file.filename)
    return {"filename": file.filename, "size": len(contents)} 

def main(): 
    import uvicorn 
    uvicorn.run(app, port=8000, log_level="debug", reload=False, access_log=False, use_colors=True) 

if __name__ == "__main__":
    main()
