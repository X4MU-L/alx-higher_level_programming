-- create database hbtn_0d_usa and create table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
       state_id INT NOT NULL FOREIGN KEY REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL
       );
