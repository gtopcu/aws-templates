

# A module is a container for multiple resources that are used together. 
# It as a reusable template or package - Can include multiple resources that are logically grouped
# Allows you to encapsulate and reuse infrastructure patterns

# # Local path
# module "example" {
#   source = "./modules/s3_bucket"
# }
# 
# # Git repository
# module "example" {
#   source = "git::https://github.com/username/repo.git/modules/s3_bucket"
# }
# 
# # Terraform Registry
# module "example" {
#   source  = "terraform-aws-modules/s3-bucket/aws"
#   version = "3.7.0"
# }

module "web_app" {
  source = "./modules/web_app"
  environment = "prod"
  # This module might create:
  # - EC2 instance
  # - Security group
  # - IAM role
  # - S3 bucket
}


module "bootstrap" {
  source = "git::https://github.com/username/repo.git/modules/s3_bucket"
  state_file_aws_region = "us-west-2"
  state_file_bucket_name = "XXXXXXXXXXXXXXXXXXXX"
  state_file_key = "statefiles"
  state_file_profile_name = "main.root"
  env = "dev"
  app = "acme"
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = false

  tags = {
    Terraform = "true"
    Environment = "dev"
  }
}

module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"
  bucket = "mybucketname"
  block_public_policy = true
  versioning = {
    enabled = true
  }
}

module "lambda_function" {
  source        = "terraform-aws-modules/lambda/aws"
  function_name = "my-tf-test-lambda"
  handler       = "exports.handler"
  runtime       = "nodejs12.x"
  environment_variables = {
    BUCKET = module.s3_bucket.s3_bucket_id
  }
}

module "sheduled_fargate_Task" {
  source = "link-to-private-registry"
  cluster_id = aws_ecs_cluster.default.id
  service_name = "crawler"
  image = "amazon/amazon-ecs-sample"
  ram = 512
  schedule = "minute"
}