#!/bin/bash
# This script creates the common lambda layer as a zip, specifically for the
# x86_64 variant of lambdas. These must then be uploaded to AWS as the lambda layer
# secr-py-common-dependencies-layer
# variables.tf must then be updated with the new version arn


rm -rf .build && mkdir .build
rm common-lambda-layer.zip

docker build --platform=linux/x86_64 -t common-lambda-layer .
docker run --rm -v ./.build:/opt common-lambda-layer

cd .build || exit
zip -r9 ../common-lambda-layer.zip .

aws s3 cp ../common-lambda-layer.zip s3://<bucket>/common-lambda-layer.zip
aws lambda publish-layer-version --layer-name common-lambda-layer --content S3Bucket=<bucket>,S3Key=common-lambda-layer.zip
