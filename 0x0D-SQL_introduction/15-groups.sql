-- Select group
SELECT score COUNT(score) AS number
FROM second_table second_table
GROUP BY score
ORDER BY score DESC;
