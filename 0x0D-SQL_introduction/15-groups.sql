-- a script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(1) AS number FROM second_table GROUP BY score;
