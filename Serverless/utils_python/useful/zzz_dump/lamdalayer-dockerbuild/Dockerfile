FROM python:3.13

WORKDIR /app

RUN apt-get update && \
    apt-get install -y zip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

CMD pip install \
    --platform manylinux2014_x86_64 \
    --implementation cp \
    --python-version 3.13 \
    --only-binary=:all: \
    -r requirements.txt  -t /opt/python/
