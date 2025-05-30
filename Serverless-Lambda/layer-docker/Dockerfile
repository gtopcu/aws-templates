# Use the official Python runtime as the base image
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Install any necessary dependencies
RUN apt-get update && \
    apt-get install -y zip && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python packages listed in requirements.txt
CMD pip install \
    --platform manylinux2014_x86_64 \
    --implementation cp \
    --python-version 3.13 \
    --only-binary=:all: \
    -r requirements.txt  -t /opt/python/
