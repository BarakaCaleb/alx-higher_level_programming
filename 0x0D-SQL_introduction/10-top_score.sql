-- Lists all records of the table of the database in nysql server
-- Records should be ordered by score
-- Database name will be passed as an argument
SELECT score, name
FROM second_table
ORDER BY score DESC;
