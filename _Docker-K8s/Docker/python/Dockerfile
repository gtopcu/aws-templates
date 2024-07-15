
# https://hub.docker.com/_/python
# https://hub.docker.com/layers/library/python/3.12-slim/images/sha256-f0c6bc1ab7b1ab270bbb612a31a67a7938d6171183ddce9121f04984ab3df44e

# FROM debian:12
FROM python:3.12
# FROM python:3.12-slim 
# FROM python:3.12-alpine
# FROM python:3.12-bookworm
# FROM python:3.12-bullseye

RUN apt update -y
# RUN apt install -y curl

ARG queue_name
ENV TASK_QUEUE_NAME=${queue_name}
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

# docker build -t python-app .
# docker run -p 8000:8000 python-app
# docker run -it --rm --name python-app python-app

# Run script in Docker directly without dockerfile:
# docker run -it --rm --name running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python script.py

# docker run -it ubuntu bash

# -----------------------------------------------------------------

FROM python:3.12
ADD application.py /tmp/application.py
EXPOSE 8080
ENTRYPOINT ["python", "/tmp/application.py"]

# -----------------------------------------------------------------

FROM debian:wheezy
ENTRYPOINT ["/bin/ping"]
CMD ["localhost"]

