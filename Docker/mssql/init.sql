CREATE DATABASE contacts_db COLLATE Hebrew_CI_AS;
GO
USE contacts_db;
GO
REATE TABLE contacts (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(80) NOT NULL,
    surname NVARCHAR(100),
    email NVARCHAR(200) UNIQUE,
    phone NVARCHAR(20)
);
GO