
# https://hub.docker.com/_/python
# https://hub.docker.com/layers/library/python/3.12-slim/images/sha256-f0c6bc1ab7b1ab270bbb612a31a67a7938d6171183ddce9121f04984ab3df44e

# docker build -t app .
# docker run -p 8000:8000 app
# docker run -it --rm --name app app

# Run script in Docker directly without dockerfile:
# docker run -it --rm --name running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python script.py

# docker run -it ubuntu bash

# FROM ubuntu:latest        : 140MB
# FROM debian:12(Bookworm)
# FROM python:3.13          : 1.46GB    -> Debian 12(Bookworm)
# FROM python:3.13-slim:    : 205MB     -> Debian 12(Bookworm)
# FROM python:3.13-alpine   : 72MB      -> Alpine Linux(no bash, uses musl instead of glibc)
# FROM python:3.13-bookworm
# FROM python:3.13-bullseye

# -----------------------------------------------------------------

FROM python:3.13
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]

FROM python:3.13
ADD app.py /app/app.py
EXPOSE 8080
ENTRYPOINT ["python", "/app/app.py"]
# ENTRYPOINT [ "/opt/app/run.sh", "--port", "8080" ]

FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]

# -----------------------------------------------------------------

FROM python:3.13
RUN apt update -y
# RUN apt install -y curl
ARG queue_name
ENV QUEUE_NAME=${queue_name}
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# RUN chown -R user:group /var/www
# COPY --chown=user:group source dest
# COPY . ./
COPY . /app/
# ADD http://remotecompressed.gzip /uncompressed
EXPOSE 8080
CMD [ "python3", "process.py" ]
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# Exec form: CMD [“executable”, “parameter1”, “parameter2”]
# Shell form: CMD command parameter1 parameter2

# -----------------------------------------------------------------

