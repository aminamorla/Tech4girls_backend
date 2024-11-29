USE Tech4Girls_DB;

-- Creating the Posts table
CREATE TABLE IF NOT EXISTS Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- Foreign key referencing Users.id
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)  -- Establishing the foreign key constraint
);


-- Inserting sample data into Posts table, establishing a one-to-many relationship
INSERT INTO Posts (user_id, title, content) 
VALUES  (1, 'Amina\'s First Post', 'This is the content of Amina\'s first post.'),
        (1, 'Amina\'s Second Post', 'This is the content of Amina\'s second post.'),
        (2, 'Abena\'s First Post', 'This is the content of Abena\'s first post.'),
        (3, 'Adjoa\'s First Post', 'This is the content of Adjoa\'s first post.');

SELECT * FROM Posts;