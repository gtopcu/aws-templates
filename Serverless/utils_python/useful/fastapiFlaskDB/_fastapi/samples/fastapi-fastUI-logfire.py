
# https://www.youtube.com/watch?v=gkHSIOxh60s

# pip install -U fastapi uvicorn[standard] fastui pydantic 
# pip install python-multipart # -> for File/UploadFile

# uvicorn fastapi-fastUI-logfire:app --reload
# http://127.0.0.1:8000/docs

from typing import Annotated
from fastapi import FastAPI, APIRouter, Request, status, HTTPException
from fastapi.responses import Response, HTMLResponse, RedirectResponse
from contextlib import asynccontextmanager
from pydantic import BaseModel
import uvicorn

from fastui import FastUI, AnyComponent, components as c, events
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent
from fastui.forms import fastui_form

# from .db import Database
# from .page import demo_page
# from . import images
# settings = Settings()

class AnimalModel(BaseModel): 
    animal: str

# router = APIRouter()
app = FastAPI()
# app = FastAPI(lifespan=lifespan)
# app.include_router(router, prefix='/api')

# uvicorn fastapi-fastUI-logfire:app --reload
def main(): 
    import uvicorn 
    uvicorn.run(app, port=8000, log_level="debug", reload=True, access_log=True, use_colors=True) 

if __name__ == "__main__":
    main()


@app.get('/')
async def home():
    return Response("Welcome to FastAPI!")

@app.get('/favicon.ico')
async def favicon():
    return RedirectResponse(url='https://smokeshow.helpmanual.io/favicon.ico')

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with Database.create(settings.pg_dsn, True, settings.create_database) as db:
#         app.state.db = db
#         openai = AsyncClient()
#         app.state.openai = openai
#         yield

# @app.get('/{path:path}')
# async def html_landing() -> HTMLResponse:
#     """Simple HTML page which serves the React app, comes last as it matches all"""
#     return HTMLResponse(prebuilt_html(title='Logfire Cat Bacon'))

# @router.get(path='/', response_model=FastUI, response_model_exclude_none=True)
# async def generate_image() -> list[AnyComponent]:
#     return demo_page(
#         c.Heading(text='Generate Image', level=2),
#         c.Paragraph(text='Generate an image of an animal in the style of Francis Bacon'),
#         c.ModelForm(
#             model=AnimalModel,
#             display_mode='page',
#             submit_url='/api/generate/',
#             loading=[c.Spinner(text='Generating Image...')],
#         ),
#     )

# @router.post(path='/generate/', response_model=FastUI, response_model_exclude_none=True)
# async def login_form_post(form: Annotated[AnimalModel, fastui_form(AnimalModel)], db: Database):
#     async with db.acquire() as conn:
#         image_id = await images.create_image(conn, request.app.state.openai, form.animal)
#         return [c.FireEvent(event=GoToEvent(url=f'/images/{image_id}/'))]


# @router.get(path='/images/', response_model=FastUI, response_model_exclude_none=True)
# async def images_table_view(db: Database, page: int = 1) -> list[AnyComponent]:
#     async with db.acquire() as conn:
#         image_list, count = await images.list_images(conn, page)
    
#     return demo_page(
#         c.Heading(text='List of Images', level=2),
#         c.Table(
#             data=image_list,
#             data_model=images.Image,
#             columns=[
#                 DisplayLookup(field='prompt', on_click=GoToEvent(url='/images/{id}/')),
#                 DisplayLookup(field='ts', mode=DisplayMode.datetime),
#             ],
#         ),
#         c.Pagination(page=page, page_size=images.PAGE_LIMIT, total=count)
#     )

# @router.get(path='/images/{image_id:int}/', response_model=FastUI, response_model_exclude_none=True)
# async def image_view(db: Database, image_id: int) -> list[AnyComponent]:
#     async with db.acquire() as conn:
#         image = await images.get_image(conn, image_id)