
# https://www.youtube.com/watch?v=P3VN8oC_t00

provider "aws" {
  region = "us-west-2"
}

provider "aws" {
  region     = "us-west-2"
  access_key = "your_access_key"
  secret_key = "your_secret_key"
}

provider "aws" {
  region  = "us-west-2"
  profile = "my-profile"
}

--------------------------------------------------------------------------------------------------------------
https://dev.to/aws-builders/switching-to-the-terraform-s3-backend-with-native-state-file-locks-3h44

provider "aws" {
  region = "us-west-2"
}

terraform {
  backend "s3" {
    encrypt        = true
    bucket         = "tfstate-lock-test-0bhfxn8x1"
    region         = "us-west-2"
    key            = "example/terraform-state-lock-test.tfstate"
    dynamodb_table = "tfstate-lock-test"
    use_lockfile   = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.82.2"
    }

  # This sets the version constraint to a minimum of 1.10 for native state file locking support
  required_version = "~> 1.10"
}

--------------------------------------------------------------------------------------------------------------

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
