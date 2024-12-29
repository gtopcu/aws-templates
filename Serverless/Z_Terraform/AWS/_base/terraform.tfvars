
# terraform apply -var-file="dev.tfvars"

# Add *.tfvars to .gitignore if they contain sensitive information
# Use terraform.tfvars or *.auto.tfvars for values that are automatically loaded
# Keep environment-specific values in separate files (e.g., dev.tfvars, prod.tfvars)

project_id = "your-project-id"
region = "us-east-1"
bucket_name = "my-function-code-bucket"
sqs_queue_name = "my-sqs_queue_name"
function_name = "my-python-lambda"

# dev.tfvars
environment = "dev"
instance_type = "t2.micro"
instance_count = 1

# prod.tfvars
environment = "prod"
instance_type = "t2.large"
instance_count = 3

# secrets.tfvars
db_password = "your-sensitive-password"
api_key = "your-api-key"