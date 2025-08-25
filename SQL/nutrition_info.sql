DROP DATABASE IF EXISTS `nutrition_info`;
CREATE DATABASE `nutrition_info`;
USE `nutrition_info`;

CREATE TABLE id_fetch (
    item_name VARCHAR(50),
    item_id INT NOT NULL
    PRIMARY KEY (item_name)
);

CREATE TABLE macro_calculator_info (
    item_id INT NOT NULL,
    serv_size FLOAT(10, 2),
    serv_unit VARCHAR(10),
    num_grams INT,
    total_fat INT,
    satur_fat INT,
    trans_fat INT,
    cholesterol INT,
    sodium INT,
    total_carbs INT,
    fiber INT,
    total_sugars INT,
    added_sugars INT,
    protein INT
    PRIMARY KEY (item_id)
);