resource "aws_subnet" "private_subnet1" {

  vpc_id = aws_vpc.vpc.id

  cidr_block = "10.0.2.0/24"

  availability_zone = "ap-southeast-1c"

  tags = {

    Name = "3-tier-privatesubnet1"

  }

}

resource "aws_route_table" "private_route_table1" {

  vpc_id = aws_vpc.vpc.id

  tags = {

    Name = "3-tier-private_route1"

  }

}

resource "aws_route_table_association" "private_subnet_association1" {

  subnet_id = aws_subnet.private_subnet1.id

  route_table_id = aws_route_table.private_route_table1.id

}

