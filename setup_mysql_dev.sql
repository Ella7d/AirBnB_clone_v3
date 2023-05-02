-- Creates the database hbnb_dev_db with parameters
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Set password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grant privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush Privileges
FLUSH PRIVILEGES;
