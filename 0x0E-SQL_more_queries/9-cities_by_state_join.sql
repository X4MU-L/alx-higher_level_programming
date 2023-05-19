-- list all cities in the table
SELECT c.id, c.name, s.name
FROM cities as c
LEFT JOIN states as s
ON c.state_id = s.id;
