# Directory Structure
# modules/
#   └── s3_bucket/
#       ├── main.tf
#       ├── variables.tf
#       └── outputs.tf
# main.tf
# terraform.tfvars

# --------- Root main.tf (how to use the module) ---------


module "logs_bucket" {
  source = "./modules/s3_bucket"

  bucket_name       = "my-app-logs-${var.environment}"
  environment      = var.environment
  enable_versioning = true
  additional_tags  = {
    Project     = "MyApp"
    Department  = "Engineering"
  }
}

module "assets_bucket" {
  source = "./modules/s3_bucket"

  bucket_name       = "my-app-assets-${var.environment}"
  environment      = var.environment
  enable_versioning = false
  additional_tags  = {
    Project     = "MyApp"
    Department  = "Marketing"
  }
}

output "logs_bucket_arn" {
  value = module.logs_bucket.bucket_arn
}