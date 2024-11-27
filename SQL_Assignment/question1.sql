-- Create the database Tech4Girls_DB
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

-- Use the newly created database
USE Tech4Girls_DB;

-- Create the Users table with specified columns
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL, unique=True
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert the sample data into the Users table
INSERT INTO Users (username, email) VALUES
('Amina', 'amina@example.com'),
('Abena', 'abena@example.com'),
('Adjoa', 'adjoa@example.com');
