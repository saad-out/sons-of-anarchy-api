-- Create database & user for the SOA API project
DROP DATABASE IF EXISTS `SOA`;
CREATE DATABASE IF NOT EXISTS `SOA`;
CREATE USER IF NOT EXISTS 'soa'@'localhost' IDENTIFIED BY '${MYSQL_USER_PASSWORD}';
GRANT ALL PRIVILEGES ON `SOA`.* TO 'soa'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'soa'@'localhost';
FLUSH PRIVILEGES;