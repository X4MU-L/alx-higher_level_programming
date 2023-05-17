-- create a table unique_id and default to 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id(
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
       );
