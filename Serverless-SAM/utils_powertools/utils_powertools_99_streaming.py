# https://docs.powertools.aws.dev/lambda/python/2.29.1/utilities/streaming/#background
from typing import Dict
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.streaming.s3_object import S3Object
from aws_lambda_powertools.utilities.streaming.transformations import ZipTransform


def lambda_handler(event: Dict[str, str], context: LambdaContext):
    
    s3 = S3Object(bucket=event["bucket"], key=event["key"], is_gzip=True, is_csv=True)
    # data = s3.transform([GzipTransform(), CsvTransform()]) - transforming later
    for line in s3:
        print(line)

    # zip_reader = s3object.transform(ZipTransform())
    # with zip_reader.open("filename.txt") as f:
    #     for line in f:
    #         print(line)