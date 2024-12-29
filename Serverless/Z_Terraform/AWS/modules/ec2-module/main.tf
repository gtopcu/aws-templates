# Directory Structure
# modules/
#   └── webserver/
#       ├── main.tf
#       ├── variables.tf
#       └── outputs.tf
# main.tf
# terraform.tfvars

# --------- Root main.tf  ---------

module "web_server_prod" {
  source = "./modules/web_server"

  environment            = "prod"
  app_name              = "myapp"
  ami_id                = "ami-0735c191cf914754d"
  instance_type         = "t2.small"
  ssh_allowed_cidr_blocks = ["10.0.0.0/16"]  # VPN CIDR
  
  common_tags = {
    Project     = "MyWebApp"
    Department  = "Engineering"
    Environment = "Production"
  }
}

module "web_server_staging" {
  source = "./modules/web_server"

  environment            = "staging"
  app_name              = "myapp"
  ami_id                = "ami-0735c191cf914754d"
  instance_type         = "t2.micro"
  ssh_allowed_cidr_blocks = ["10.0.0.0/16"]
  
  common_tags = {
    Project     = "MyWebApp"
    Department  = "Engineering"
    Environment = "Staging"
  }
}