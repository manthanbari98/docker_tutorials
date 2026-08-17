USE demo_db;

Create table users (
    id INT NOT NULL AUTO_INCREMENT,
    city VARCHAR(100) NOT NULL,
    temperature FLOAT NOT NULL,
    PRIMARY KEY (id)
);