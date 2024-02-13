-- lists the number of records with the same socre in the second_table
SELECT DISTINCT score, COUNT(*) as number FROM second_table GROUP BY score
