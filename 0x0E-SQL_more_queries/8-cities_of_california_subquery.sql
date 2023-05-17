-- select all California cities in cities table
SELECT id, name FROM cities WHERE cities.state_id = table2.id AND
table2.name = 'California' IN (SELECT * FROM states) AS table2;
