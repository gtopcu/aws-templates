
# modules/web_server/outputs.tf
output "instance_id" {
  value       = aws_instance.web.id
  description = "ID of the created EC2 instance"
}

output "public_ip" {
  value       = aws_instance.web.public_ip
  description = "Public IP of the created EC2 instance"
}

output "security_group_id" {
  value       = aws_security_group.web.id
  description = "ID of the created security group"
}