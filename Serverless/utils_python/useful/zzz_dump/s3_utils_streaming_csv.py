
import os
import boto3
import orjson

from aws_lambda_powertools import Logger

logger = Logger()

class S3Utils:
    def __init__(self):
        self.s3 = boto3.client("s3")
        self.S3_BUCKET = os.environ["DATA_BUCKET_NAME"]
        self.S3_CACHE_KEY = "data.json"

    def s3_handlerf(self):

        try:
            self.s3.delete_object(Bucket=self.S3_BUCKET, Key=self.S3_CACHE_KEY)
            logger.info(f"Cleared S3 cache: {self.S3_CACHE_KEY}.")
        except self.s3.exceptions.NoSuchKey:
            logger.info("File does not exist in S3")
        except Exception as e:
            logger.exception(f"Failed to delete file in S3: {e}")
            raise

        s3_data = self.s3.get_object(Bucket=self.S3_BUCKET, Key=self.S3_CACHE_KEY)
        body = s3_data["Body"].read()  # Read S3 Data
        
        cached_data = orjson.loads(body)  # Fastest JSON Parsing
        # print(type(cached_data))
        if not isinstance(cached_data, list):
            raise ValueError("Unexpected JSON format: Expected a list")  # Fail fast if not list

        for item in cached_data:
            print(item)

        self.s3.put_object(
                Bucket=self.S3_BUCKET,
                Key=self.S3_CACHE_KEY,
                Body=cached_data,  
                ContentType="application/json",
            )

def s3_stream(bucket_name: str, bucket_key: str):
    from aws_lambda_powertools.utilities.streaming import S3Object
    from aws_lambda_powertools.utilities.streaming.transformations import CsvTransform
    
    s3_obj = S3Object(bucket=bucket_name, key=bucket_key, is_csv=True, is_gzip=True) # streamable S3 object
    # line: bytes = s3_obj.readline()
    # print(line)

    # csv_reader = s3_obj.transform(CsvTransform(encoding="utf-8-sig"), in_place=True)
    csv_reader = s3_obj.transform(CsvTransform(encoding="utf-8", newline="\r\n"))
    for row in csv_reader:
        print(row)
    