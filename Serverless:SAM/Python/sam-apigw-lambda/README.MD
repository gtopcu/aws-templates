
aws s3 mb s3://gtopcu-sam --region eu-west-1  

sam validate

sam package \
--template-file template.yml \
--output-template-file sam-template.yml \
--s3-bucket gtopcu-sam

sam deploy --guided \
--template-file sam-template.yml \
--stack-name samdemostack \
--capabilities CAPABILITY_IAM

sam sync --watch
sam delete

Invoke:
sam local invoke -e ./events/lambda_event.json samFunction

Start:
sam local start-lambda
sam local start-api
sam local start-api --template-file cloudformation.yml

Generate Event
sam local generate-event sqs ...