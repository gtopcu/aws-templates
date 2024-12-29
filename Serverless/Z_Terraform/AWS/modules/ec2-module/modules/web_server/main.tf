
# modules/web_server/main.tf
resource "aws_security_group" "web" {
  name = "${var.environment}-${var.app_name}-sg"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.ssh_allowed_cidr_blocks
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    var.common_tags,
    {
      Name = "${var.environment}-${var.app_name}-sg"
    }
  )
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  security_groups = [aws_security_group.web.name]
  
  user_data = templatefile("${path.module}/user_data.sh", {
    environment = var.environment
    app_name    = var.app_name
  })

  tags = merge(
    var.common_tags,
    {
      Name = "${var.environment}-${var.app_name}"
    }
  )
}