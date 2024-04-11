
# https://www.youtube.com/watch?v=iWS9ogMPOI0
# https://www.youtube.com/watch?v=_Y3uAFVYk5I
# https://www.youtube.com/watch?v=0A_GCXBCNUQ


# pip install fastapi
# pip install "uvicorn[standard]"

# python3 -m venv venv
# source venv/bin/activate

# uvicorn api_fastapi:app --reload
# http://127.0.0.1:8000/docs

from datetime import datetime

from fastapi import FastAPI, Request, status, HTTPException, File, UploadFile
# from fastapi import File, UploadFile, Body, Path, Query, Cookie, Header
# from fastapi.responses import Response, HTMLResponse, JSONResponse
# FileResponse, PlainTextResponse, RedirectResponse,  StreamingResponse
# from fastjsonschema import validate, exceptions
from fastapi.middleware.cors import CORSMiddleware
# from _customRouter import router

from pydantic import BaseModel, Field

class ToDo(BaseModel):
    id: int = Field(default=0)
    title: str = Field(default="", description="Mr/Mrs/Ms")
    updated: datetime = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# FastAPI is async by default (Flask is not)
app = FastAPI()
# app.include_router(router)
# app.add_exception_handler(HTTPException, exceptionHandler, exc: exc.detail)
app.add_middleware( 
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
#     expose_headers=["*"],
#     max_age=3600,
#     # origins=["XXXXXXXXXX"],
)

items = [ToDo(id=1, title="Buy milk"), ToDo(id=2, title="Buy bread")]

@app.get("/")
async def root(request: Request):
    # request.base_url
    # request.path_params
    # request.method
    # request.headers
    # request.auth
    # request.query_params
    return request.base_url
    # return {"message": "Hello World"}

# http://127.0.0.1:8000/items?limit=2
@app.get("/items", response_model=list[ToDo])
async def list_items(request: Request, limit:int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=ToDo)
async def get_item(item_id: int):
    if(item_id < len(items)):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "Not found"})
        # return {"message": "Item not found"}

@app.post("/items", response_model=ToDo, status_code=status.HTTP_201_CREATED, tags=["items"])
async def create_item(request: Request, item: ToDo):
    items.append(item)
    return item

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # print(contents)
    print("File uploaded: ", file.filename)
    return {"filename": file.filename, "size": len(contents)} 

# def main():
#     import uvicorn
