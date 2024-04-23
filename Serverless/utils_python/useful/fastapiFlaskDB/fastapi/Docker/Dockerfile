# https://fastapi.tiangolo.com/deployment/docker/
# https://fastapi.tiangolo.com/deployment/docker/#official-docker-image-with-gunicorn-uvicorn
# https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry

FROM python:3.9

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# docker build -t myimage .
# docker run -d --name mycontainer -p 80:80 myimage
# http://127.0.0.1/items/5?q=somequery
# http://127.0.0.1/docs
# http://127.0.0.1/redocs

# Dockerfile with Poetry:
# FROM python:3.9 as requirements-stage 
# WORKDIR /tmp
# RUN pip install poetry
# COPY ./pyproject.toml ./poetry.lock* /tmp/
# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# FROM python:3.9
# WORKDIR /code
# COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]