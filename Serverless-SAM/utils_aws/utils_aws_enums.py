from enum import Enum, auto

class AWSServices(Enum):
    S3 = "s3"
    DYNAMODB = "dynamodb"
    LAMBDA_TIMEOUT = 30
    APIGW_TIMEOUT = auto()
    #ZERO, ONE = range(2)

def main() -> None:
    print(AWSServices.S3.value)
    print(AWSServices.DYNAMODB.name)

if __name__ == "__main__":
    main()
    

