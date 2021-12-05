
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
# gokhantopcu-test
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('/Users/hukanege/Google Drive/VSCode/AWS-Templates/boto3/vesika.jpg', 'rb')
s3.Bucket('gokhantopcu-test').put_object(Key='vesika.jpg', Body=data)

