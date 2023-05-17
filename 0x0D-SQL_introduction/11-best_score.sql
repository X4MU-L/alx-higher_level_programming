-- list the score and name of users whose score is greater than 10
-- +in second_table ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
