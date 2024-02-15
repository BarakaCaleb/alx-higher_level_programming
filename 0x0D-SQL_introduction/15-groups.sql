-- Lists the number of records with same score in the table second_table of the database
-- Database name will be passed as an argument to the mysql command
-- List should be sorted by the number of records descending
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
