
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