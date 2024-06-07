CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    surname VARCHAR(100),
    email VARCHAR(200) UNIQUE,
    phone VARCHAR(20)
);