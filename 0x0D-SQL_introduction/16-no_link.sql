-- lists all records of the second_Table, don't list rows without a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
