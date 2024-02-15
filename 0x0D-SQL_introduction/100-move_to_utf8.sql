-- Convert a database to UTF8 in your MYSQL database
-- Convert the following 
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
-- convert database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
