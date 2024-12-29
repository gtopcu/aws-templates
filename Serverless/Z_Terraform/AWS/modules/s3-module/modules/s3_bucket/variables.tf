
# --------- modules/s3_bucket/variables.tf ---------

variable "bucket_name" {
  type        = string
  description = "Name of the S3 bucket"
}

variable "environment" {
  type        = string
  description = "Environment (e.g., dev, prod)"
}

variable "enable_versioning" {
  type        = bool
  description = "Enable versioning on the bucket"
  default     = false
}

variable "additional_tags" {
  type        = map(string)
  description = "Additional tags for the bucket"
  default     = {}
}
