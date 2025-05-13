DROP DATABASE IF EXISTS army_ops;
CREATE DATABASE army_ops;
USE army_ops;

CREATE TABLE division (
  division_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE battalion (
  battalion_id INT AUTO_INCREMENT PRIMARY KEY,
  division_id INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  CONSTRAINT fk_battalion_division FOREIGN KEY (division_id)
    REFERENCES division(division_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

CREATE TABLE soldier (
  soldier_id INT AUTO_INCREMENT PRIMARY KEY,
  battalion_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  rank VARCHAR(30),
  CONSTRAINT fk_soldier_battalion FOREIGN KEY (battalion_id)
    REFERENCES battalion(battalion_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE TABLE mission (
  mission_id INT AUTO_INCREMENT PRIMARY KEY,
  mission_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE assignment (
  assignment_id INT AUTO_INCREMENT PRIMARY KEY,
  soldier_id INT NOT NULL,
  mission_id INT NOT NULL,
  status VARCHAR(20) NOT NULL,
  CONSTRAINT fk_assignment_soldier FOREIGN KEY (soldier_id)
    REFERENCES soldier(soldier_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_assignment_mission FOREIGN KEY (mission_id)
    REFERENCES mission(mission_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);