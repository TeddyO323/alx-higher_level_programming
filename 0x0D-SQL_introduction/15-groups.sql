-- PRINT the score and number of participants that have each score
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY NUMBER DESC;