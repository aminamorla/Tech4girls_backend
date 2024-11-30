USE Tech4Girls_DB;

-- Create the Courses table
CREATE TABLE IF NOT EXISTS Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- Create the Users table with specified columns
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the User_Courses intermediate table to establish a many-to-many relationship
CREATE TABLE IF NOT EXISTS User_Courses (
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, course_id)
);

-- Insert sample data into the Courses table
INSERT INTO Courses (course_name)
VALUES
    ('Introduction to SQL'),
    ('Advanced Python Programming'),
    ('Web Development Basics'),
    ('Data Science with R');

-- Insert sample data into the User_Courses table to demonstrate many-to-many relationship
-- Example users: 1, 2, 3
-- Assuming Users table has at least 3 users with ids 1, 2, and 3

INSERT INTO User_Courses (user_id, course_id)
VALUES
    (1, 1),  -- User 1 enrolls in 'Introduction to SQL'
    (1, 2),  -- User 1 enrolls in 'Advanced Python Programming'
    (2, 2),  -- User 2 enrolls in 'Advanced Python Programming'
    (2, 3),  -- User 2 enrolls in 'Web Development Basics'
    (3, 1),  -- User 3 enrolls in 'Introduction to SQL'
    (3, 4);  -- User 3 enrolls in 'Data Science with R'

-- Sample query to retrieve all users and their enrolled courses
SELECT u.id AS user_id, u.username AS user_name, c.course_name
FROM Users u
JOIN User_Courses uc ON u.id = uc.user_id
JOIN Courses c ON uc.course_id = c.id
ORDER BY u.id, c.course_name;
