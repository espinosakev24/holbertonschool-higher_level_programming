-- Script that creates a database user
-- Created only for user - all permmisions
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1d_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
