-- Creates a database hbtn_0d_2 and a user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_od_2'@'localhost';
