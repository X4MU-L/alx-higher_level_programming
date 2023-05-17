-- create user_0d_1 and grand all privileges and set password to user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.*
