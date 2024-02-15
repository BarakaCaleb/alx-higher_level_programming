-- Lists all records of the table of the database
-- Records should be listed in descending order
-- Rows without a name value wont be listed
-- Database name will be passed as an argument of the mysql command
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
