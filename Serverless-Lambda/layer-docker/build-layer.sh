#!/bin/bash
# This script creates the common lambda layer as a zip, specifically for the
# x86_64 variant of lambdas. Must then be uploaded to AWS as the lambda layer

rm -rf .build && mkdir .build
rm lambda-layer.zip

docker build --platform=linux/x86_64 -t lambda-layer .
docker run --rm -v ./.build:/opt lambda-layer

cd .build || exit
zip -r9 ../lambda-layer.zip .

aws s3 cp ../lambda-layer.zip s3://<url>-eu-west-2/lambda-layers/lambda-layer.zip
aws lambda publish-layer-version --layer-name lambda-layer --content S3Bucket=<url>-eu-west-2-lambda-layers,S3Key=lambda-layer.zip
