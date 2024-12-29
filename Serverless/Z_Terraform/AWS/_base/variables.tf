
# var.aws_region

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "default_tags" {
  type        = map(string)
  description = "Default tags for the bucket"
  default     = { "app":"myapp" }
}

variable "allowed_cidr_blocks" {
  type        = list(string)
  default     = ["0.0.0.0/0"]
  description = "List of CIDR blocks allowed to access HTTP"
}

variable "ec2_instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3-micro"
}

variable "ec2_ami" {
  description = "Amazon Machine Image for EC2"
  type        = string
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket to store Lambda code"
  type        = string
}

variable "enable_versioning" {
  type        = bool
  description = "Enable versioning on the bucket"
  default     = false
}

variable "sqs_queue_name" {
  description = "Name of the SQS queue"
  type        = string
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
}