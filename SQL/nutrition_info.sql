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
    serving_size FLOAT(10, 2),
    serving_unit VARCHAR(10),
    calories INT,
    protein INT, 
    carbs INT,
    fat INT,
    sugar INT,
    saturated_fat INT,
    PRIMARY KEY (item_id)
);

INSERT INTO id_fetch (item_name, item_id)
VALUES
('Heinz Ketchup: Sugar Free', 0);

INSERT INTO macro_calculator_info(item_id, serving_size, serving_unit, calories, protein, carbs, fat, sugar, saturated_fat)
VALUES
(0, 1, "Tbsp", 10, 0, 1, 0, 0, 0);