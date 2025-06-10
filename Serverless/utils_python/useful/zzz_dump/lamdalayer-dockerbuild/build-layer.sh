#!/bin/bash

# Creates common lambda layer as a zip file for x86_64 lambdas

rm -rf .build && mkdir .build
rm common-lambda-layer.zip

docker build --platform=linux/x86_64 -t common-lambda-layer .
docker run --rm -v ./.build:/opt common-lambda-layer

cd .build || exit
zip -r9 ../common-lambda-layer.zip .

aws s3 cp ../common-lambda-layer.zip s3://<bucket>/common-lambda-layer.zip
aws lambda publish-layer-version --layer-name common-lambda-layer --content S3Bucket=<bucket>,S3Key=common-lambda-layer.zip
