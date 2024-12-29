
# modules/web_server/variables.tf
variable "environment" {
  type        = string
  description = "Environment name (e.g., dev, staging, prod)"
}

variable "app_name" {
  type        = string
  description = "Application name"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "EC2 instance type"
}

variable "ami_id" {
  type        = string
  description = "AMI ID for the EC2 instance"
}

variable "allowed_cidr_blocks" {
  type        = list(string)
  default     = ["0.0.0.0/0"]
  description = "List of CIDR blocks allowed to access HTTP"
}

variable "ssh_allowed_cidr_blocks" {
  type        = list(string)
  description = "List of CIDR blocks allowed to access SSH"
}

variable "common_tags" {
  type        = map(string)
  default     = {}
  description = "Common tags for all resources"
}
