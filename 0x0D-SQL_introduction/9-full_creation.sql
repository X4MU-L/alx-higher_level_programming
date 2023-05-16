-- create a table second_table and insert these values on creation
-- id = 1, name = 'John', score = 10, id = 2, name = 'Alex' ....
CREATE TABLE IF NOT EXISTS second_table(
       id INT,
       name VARCHAR(256),
       score INT
       );
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8)
