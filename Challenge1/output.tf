
output "eip" {
  description = "The Public IPV4 Address of Elastic IP"
  value       = aws_eip.eip.public_ip
}