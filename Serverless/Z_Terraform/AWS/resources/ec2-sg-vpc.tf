
# Creates a VPC with a CIDR block of 10.0.0.0/16
# Sets up a public subnet with a CIDR block of 10.0.1.0/24
# Creates an Internet Gateway and appropriate routing
#
# Configures a security group that: 
# Allows inbound SSH (port 22) traffic
# Allows all outbound IPv4 and IPv6 traffic
# 
# Launches a t2.micro EC2 instance in the public subnet
# Outputs the public IP address of the instance


# Provider configuration
provider "aws" {
  region = "us-west-2"  # Change to your desired region
}


resource "aws_instance" "web" {
  ami           = "ami-0735c191cf914754d"
  instance_type = "t2.micro"
  
  security_groups = [aws_security_group.ec2_web_sg.name]
  
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              EOF

  tags = {
    Name = "web-server"
    Environment = "production"
  }
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "main-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main-igw"
  }
}

# Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-west-2a"  # Change this according to your region
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

# Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "public-rt"
  }
}

# Route Table Association
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# Security Group
resource "aws_security_group" "ec2_web_sg" {
  # name        = "ec2-security-group"
  name          = "${var.environment}-${var.app_name}-sg"
  description   = "Security group for EC2 instance"
  vpc_id        = aws_vpc.main.id

  # Inbound SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # All outbound IPv4 traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # All outbound IPv6 traffic
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "ec2-security-group"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0735c191cf914754d"  # Amazon Linux 2023 AMI - change according to your region
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]
  key_name = "your-key-pair-name"  # Change this to your key pair name

  tags = {
    Name = "web-server"
  }
}

# Output the public IP of the instance
output "instance_public_ip" {
  value = aws_instance.web.public_ip
}