-- create a table in the database of MYSQL server
-- Database will be passsed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (
    id,
    name,
    score)
VALUES(1, 'John', 10),
      (2, 'Alex', 3),
      (3, 'Bob', 14),
      (4, 'George', 8);
