
# https://www.eliasbrange.dev/posts/observability-with-fastapi-aws-lambda-powertools/

from fastapi import FastAPI, HTTPException
import asyncio

from mangum import Mangum
# from . import dynamo, models
import dynamo, models

app = FastAPI()

# from fastapi.responses import JSONResponse
# from starlette.exceptions import ExceptionMiddleware
# import logging
# logger = logging.getLogger()

# app.add_middleware(ExceptionMiddleware, handlers=app.exception_handlers)
# @app.exception_handler(Exception)

# async def unhandled_exception_handler(request, err):
#     logger.exception("Unhandled exception")
#     return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


@app.get("/")
async def get_root():
    return {"message": "Hello World"}


@app.get("/pets", response_model=models.PetListResponse)
async def list_pets(next_token: str = None):
    return dynamo.list_pets(next_token)


@app.get("/pets/{pet_id}", response_model=models.PetResponse)
async def get_pet(pet_id: str):
    try:
        return dynamo.get_pet(pet_id)
    except dynamo.PetNotFoundError:
        raise HTTPException(status_code=404, detail="Pet not found")


@app.post("/pets", status_code=201, response_model=models.PetResponse)
async def post_pet(payload: models.CreatePayload):
    res = dynamo.create_pet(kind=payload.kind, name=payload.name)
    return res


@app.patch("/pets/{pet_id}", status_code=204)
async def update_pet(pet_id: str, payload: models.UpdatePayload):
    try:
        return dynamo.update_pet(
            pet_id=pet_id,
            kind=payload.kind,
            name=payload.name,
        )
    except dynamo.PetNotFoundError:
        raise HTTPException(status_code=404, detail="Pet not found")


@app.delete("/pets/{pet_id}", status_code=204)
async def delete_pet(pet_id: str):
    try:
        dynamo.delete_pet(pet_id)
    except dynamo.PetNotFoundError:
        raise HTTPException(status_code=404, detail="Pet not found")


handler = Mangum(app)