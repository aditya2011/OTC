resource "aws_instance" "web" {
  ami                         = "ami-0b419c3a4b01d1859"
  instance_type               = "t2.micro"
  key_name                    = "3tierkeypair"
  monitoring                  = true
  vpc_security_group_ids      = ["${aws_security_group.sg.id}"]
  subnet_id                   = aws_subnet.private_subnet.id
  private_ip                  = "10.0.1.11"
  associate_public_ip_address = false
  tags =  {
  Name = "3-tier-mysql"
  }
  # user_data = file(install_php_mysql.sh)
}