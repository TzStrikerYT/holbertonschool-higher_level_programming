-- Read only for a user
-- crate DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- User
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- privileges
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost';
