
terraform init -backend-config="backend.tfvars"
terraform plan
terraform apply -auto-approve
terraform destroy -auto-approve

terraform init

Claude - AWS:
Create a sample terraform file for a Python 3.13 lambda function that is triggered from a sqs queue. 
The input should take S3 bucket name, SQS queue name and lambda function name. The output should contain S3 bucket name

Claude - GCP:
Create a sample terraform file for a Python 3.13 google cloud function that is triggered from a pubsub topic. 
The input should take cloud storage bucket name, pubsub topic name and function name. The output should contain bucket name