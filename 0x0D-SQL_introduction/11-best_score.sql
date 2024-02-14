-- Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
-- Records should be ordered by score 
-- The database name should be passed as an argument
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
