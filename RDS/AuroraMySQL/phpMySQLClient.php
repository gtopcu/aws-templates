------------------------------------------------------------
EC2 Bootstrap 1 - Connect to RDS MySQL
------------------------------------------------------------

#!/bin/bash
yum update -y
yum install httpd php php-mysql -y
service httpd start
chkconfig httpd on
echo "<?php phpinfo();?>" > /var/www/html/index.php
cd /var/www/html  
wget https://s3.amazonaws.com/acloudguru-production/connect.php

<?php
$username = "usr";
$password = "pass";
$hostname = "rds-dns";
$dbname = "mysqldb";

//connection to the database (update with RDS DNS)
$dbhandle = mysql_connect($hostname, $username, $password) or die("Unable to connect to MySQL");
echo "Connected to MySQL using username - $username, password - $password, host - $hostname<br>";
$selected = mysql_select_db("$dbname",$dbhandle)   or die("Unable to connect to MySQL DB - check the database name a$
?>

http://3.249.128.8/
http://3.249.128.8/connect.php