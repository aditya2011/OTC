#!/bin/bash
yum update -y
sudo amazon-linux-extras install epel -y
sudo yum update -y
sudo amazon-linux-extras install -y php7.2
sudo yum install httpd -y
service start httpd
yum install git -y
cd /var/www/html/
## here just for example I have taken phpcode, it can be any other app server and we can connect with the database accordingly
git clone https://github.com/phpcode
cd phpcodelogin/
mv * /var/www/html/
yum install wget -y
yum install mysql -y
yum install mysql-server -y
service mysqld restart
systemctl restart httpd
cd /var/www/html/

# We can connect with mysql or any other database which is required to connect our backend application.

# mysql -h hostname -u username -pmypassword -D wordpress_db < table.sql
