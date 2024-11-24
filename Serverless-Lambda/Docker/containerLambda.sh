----------------------------------------------------------------------------------------------------------------------
https://aws.amazon.com/blogs/compute/introducing-the-amazon-linux-2023-runtime-for-aws-lambda/

FROM public.ecr.aws/lambda/python:3.13
# Copy function code
COPY lambda_handler.py ${LAMBDA_TASK_ROOT}

----------------------------------------------------------------------------------------------------------------------

# Use the Amazon Linux 2023 Lambda base image
FROM public.ecr.aws/lambda/provided.al2023

# Install the required Python version
RUN dnf install -y python3

----------------------------------------------------------------------------------------------------------------------

https://aws.amazon.com/blogs/aws/amazon-linux-2023-a-cloud-optimized-linux-distribution-with-long-term-support/
https://aws.amazon.com/blogs/compute/python-3-12-runtime-now-available-in-aws-lambda/

FROM public.ecr.aws/lambda/python:3.12
COPY lambda_handler.py ${LAMBDA_TASK_ROOT}

----------------------------------------------------------------------------------------------------------------------

FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.12
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" --no-cache-dir

COPY . ${LAMBDA_TASK_ROOT}
CMD ["app.lambda_handler"]

----------------------------------------------------------------------------------------------------------------------

SAM:
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello-world/
      Handler: my.bootstrap.file
      Runtime: provided.al2023

