
# docker run -it ubuntu bash
# docker run -it python:3.13 bash
# docker run -it python:3.13-slim bash
# docker run -it python:3.13-alpine

# docker build -t my-python-slim .
# docker tag my-python-slim gtopcu/my-python-slim
# docker run my-python-slim 
# docker run my-python-slim -dp 8080:8080
# docker run -it my-python-slim bash

# runs as root - no need for sudo!
# apt list search show install reinstall remove autoremove update upgrade full-upgrade edit-sources satisfy

# shows OS release
# cat /etc/os-release 

# FROM python:3.13          : 1.46GB    -> Debian 12(Bookworm)
# FROM python:3.13-slim:    : 205MB     -> Debian 12(Bookworm)
# FROM python:3.13-alpine   : 72MB      -> Alpine Linux(no bash, uses musl instead of glibc)

# /usr/local/lib/python3.13/site-packages
FROM python:3.13-slim
RUN apt update && apt upgrade -y
WORKDIR /app
COPY . /app
# RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]