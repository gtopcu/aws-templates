
# https://www.youtube.com/watch?v=iWS9ogMPOI0

# pip install fastapi
# pip install "uvicorn[standard]"

# python3 -m venv venv
# source venv/bin/activate

# uvicorn app:app --reload
# http://127.0.0.1:8000/docs

from datetime import datetime

from fastapi import FastAPI, Request, status, HTTPException #, Depends, Form, File, status
# from fastapi import File, UploadFile, Body, Path, Query, Cookie, Header
# from fastapi.responses import Response, HTMLResponse, JSONResponse
# FileResponse, PlainTextResponse, RedirectResponse,  StreamingResponse
# from fastjsonschema import validate, exceptions


from pydantic import BaseModel, Field

class ToDo(BaseModel):
    id: int = Field(default=0)
    title: str = Field(default="", description="Mr/Mrs/Ms")
    updated: datetime = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# FastAPI is async by default (Flask is not)
app = FastAPI()

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

@app.post("/items", response_model=ToDo)
async def create_item(request: Request, item: ToDo):
    items.append(item)
    return item

# def main():
#     import uvicorn
