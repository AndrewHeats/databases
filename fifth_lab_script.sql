
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


CREATE SCHEMA IF NOT EXISTS flixbus DEFAULT CHARACTER SET utf8 ;
USE flixbus ;




CREATE TABLE IF NOT EXISTS bus (
  id INT NOT NULL AUTO_INCREMENT,
  capacity INT NOT NULL,
  age INT NOT NULL,
  run INT NOT NULL,
  is_own TINYINT NULL DEFAULT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;




CREATE TABLE IF NOT EXISTS driver (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  surname VARCHAR(45) NOT NULL,
  company VARCHAR(45) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;





CREATE TABLE IF NOT EXISTS driver_bus (
  id INT NOT NULL AUTO_INCREMENT,
  driver_id INT NOT NULL,
  bus_id INT NOT NULL,
  PRIMARY KEY (id,  driver_id, bus_id),
  INDEX fk_driver_has_bus_bus1_idx (bus_id ASC) VISIBLE,
  INDEX fk_driver_has_bus_driver_idx ( driver_id ASC) VISIBLE,
  CONSTRAINT fk_driver_has_bus_bus1
    FOREIGN KEY (bus_id)
    REFERENCES flixbus.bus (id),
  CONSTRAINT fk_driver_has_bus_driver
    FOREIGN KEY ( driver_id)
    REFERENCES flixbus.driver (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;





CREATE TABLE IF NOT EXISTS passenger (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  surname VARCHAR(45) NOT NULL,
  date_of_birth DATE NOT NULL,
  phone_number VARCHAR(13) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;




CREATE TABLE IF NOT EXISTS stop (
  id INT NOT NULL AUTO_INCREMENT,
  address VARCHAR(45) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;





CREATE TABLE IF NOT EXISTS route (
  id INT NOT NULL AUTO_INCREMENT,
  distance_of_route INT AS (distance_between_2_stops*(number_of_stops-1)),
  distance_between_2_stops INT NOT NULL,
  number_of_stops INT NOT NULL,
  start_of_the_route INT NOT NULL,
  end_of_the_route INT NOT NULL,
  PRIMARY KEY (id, start_of_the_route, end_of_the_route),
  INDEX fk_route_stop1_idx (start_of_the_route ASC) VISIBLE,
  INDEX fk_route_stop2_idx (end_of_the_route ASC) VISIBLE,
  CONSTRAINT fk_route_stop1
    FOREIGN KEY (start_of_the_route)
    REFERENCES stop (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_route_stop2
    FOREIGN KEY (end_of_the_route)
    REFERENCES stop (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;





CREATE TABLE IF NOT EXISTS route_bus (
  id INT NOT NULL AUTO_INCREMENT,
  bus_id INT NOT NULL,
  route_id INT NOT NULL,
  PRIMARY KEY (id, bus_id, route_id),
  INDEX fk_route_has_bus_bus1_idx (bus_id ASC) VISIBLE,
  INDEX fk_route_has_bus_route1_idx (route_id ASC) VISIBLE,
  CONSTRAINT fk_route_has_bus_bus1
    FOREIGN KEY (bus_id)
    REFERENCES flixbus.bus (id),
  CONSTRAINT fk_route_has_bus_route1
    FOREIGN KEY (route_id)
    REFERENCES route (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;




CREATE TABLE IF NOT EXISTS stop_route (
  id INT NOT NULL AUTO_INCREMENT,
  route_id INT NOT NULL,
  stop_id INT NOT NULL,
  PRIMARY KEY (id, route_id, stop_id),
  INDEX fk_stop_has_route_route1_idx (route_id ASC) VISIBLE,
  INDEX fk_stop_has_route_stop1_idx (stop_id ASC) VISIBLE,
  CONSTRAINT fk_stop_has_route_route1
    FOREIGN KEY (route_id)
    REFERENCES route (id),
  CONSTRAINT fk_stop_has_route_stop1
    FOREIGN KEY (stop_id)
    REFERENCES stop (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;





CREATE TABLE IF NOT EXISTS subroute (
  id INT NOT NULL AUTO_INCREMENT,
  start_of_subroute INT NOT NULL,
  end_of_subroute INT NOT NULL,
  price_of_subroute INT NOT NULL,
  distance_of_subroute INT NOT NULL,
  route_id INT NOT NULL,
  PRIMARY KEY (id, route_id, start_of_subroute, end_of_subroute),
  INDEX fk_subroute_route1_idx (route_id ASC) VISIBLE,
  INDEX fk_subroute_start_idx (start_of_subroute ASC) VISIBLE,
  INDEX fk_subroute_end_idx (end_of_subroute ASC) VISIBLE,
  CONSTRAINT fk_subroute_end
    FOREIGN KEY (end_of_subroute)
    REFERENCES stop (id),
  CONSTRAINT fk_subroute_route1
    FOREIGN KEY (route_id)
    REFERENCES route (id),
  CONSTRAINT fk_subroute_start
    FOREIGN KEY (start_of_subroute)
    REFERENCES stop (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;





CREATE TABLE IF NOT EXISTS ticket (
  id INT NOT NULL AUTO_INCREMENT,
  price FLOAT NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- index section

ALTER TABLE passenger
ADD INDEX idx_passenger_name (name);

ALTER TABLE passenger
ADD INDEX idx_passenger_surname (surname);



ALTER TABLE subroute
ADD INDEX idx_subroute_start_of_subroute (start_of_subroute);

ALTER TABLE subroute
ADD INDEX idx_subroute_end_of_subroute (end_of_subroute);


ALTER TABLE stop
ADD INDEX idx_stop_address (address);


ALTER TABLE route
ADD INDEX idx_route_start_of_route (start_of_the_route);

ALTER TABLE route
ADD INDEX idx_route_end_of_route (end_of_the_route);


-- Create trigger to enforce referential integrity
-- Create the ticket_base table
CREATE TABLE IF NOT EXISTS `Flixbus`.`bus_base` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `bus_id` INT NOT NULL,
  `travel_count` INT ,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;


DELIMITER //
CREATE TRIGGER update_travel_count
BEFORE INSERT ON flixbus.bus_base
FOR EACH ROW
BEGIN 
	SET NEW.travel_count = (
		SELECT COUNT(*)
        FROM flixbus.route_bus
        WHERE route_bus.bus_id = NEW.bus_id
    );
END;
//
DELIMITER ;



DELIMITER //

CREATE TRIGGER before_delete_bus_base
BEFORE DELETE ON Flixbus.bus_base
FOR EACH ROW
BEGIN
    -- Delete related rows in the bus table when a row is deleted in bus_base
    DELETE FROM Flixbus.bus
    WHERE id = OLD.bus_id;
END //

DELIMITER ;
DELIMITER //

CREATE TRIGGER before_update_bus
BEFORE UPDATE ON Flixbus.bus
FOR EACH ROW
BEGIN
    DECLARE bus_base_exists INT;

    -- Check if the referenced id exists in the bus_base table
    SELECT COUNT(*) INTO bus_base_exists
    FROM Flixbus.bus_base
    WHERE bus_id = NEW.id;

    -- If the id does not exist, prevent the update
    IF bus_base_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Referenced id does not exist in the bus_base table';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER `before_insert_on_bus`
BEFORE INSERT ON bus
FOR EACH ROW
BEGIN
    -- Check the condition for the run value
    IF NEW.run RLIKE '^0+'
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Run cannot start from 0';
    END IF;
END //

DELIMITER ;


DELIMITER //

USE flixbus;

DELIMITER //

CREATE TRIGGER `before_insert_on_driver`
BEFORE INSERT ON driver
FOR EACH ROW
BEGIN
   
    IF NEW.name RLIKE 'Oksana' OR NEW.name RLIKE 'Ivan' OR NEW.name RLIKE 'Petya' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'You can`t insert name Oksana Ivan Petya';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER `before_update_on_driver_name`
BEFORE UPDATE ON driver
FOR EACH ROW
BEGIN

	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'You can`t update driver ';
    
END //

DELIMITER ;

DELIMITER //
CREATE TRIGGER `before_insert_bus_base`
BEFORE INSERT ON `Flixbus`.`bus_base`
FOR EACH ROW
BEGIN
  DECLARE bus_exists INT;

  -- Check if the referenced ticket_id exists in the ticket table
  SELECT COUNT(*) INTO bus_exists
  FROM `Flixbus`.`bus`
  WHERE `id` = NEW.bus_id;

  -- If the ticket does not exist, prevent the insertion
  IF bus_exists = 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Referenced bus_id does not exist in the bus table';
  END IF;
END //
DELIMITER ;




-- procedures


DELIMITER //
    CREATE 
	PROCEDURE insert_driver(
		IN nam VARCHAR(45),
		IN surname VARCHAR(45),
		IN company VARCHAR(45))
	BEGIN
		INSERT INTO `flixbus`.`driver` (name, surname, company)
		VALUES (nam, surname, company);
	END;
//

DELIMITER //
	CREATE 
	PROCEDURE insert_driver_bus_dependency_by_name_and_run(
		IN name VARCHAR(45),
		IN run INT
	)
    BEGIN
		DECLARE driver_id INT;
        DECLARE bus_id INT;
        
        SELECT id INTO driver_id
        FROM driver
        WHERE driver.name = name;
        
        SELECT id INTO bus_id
        FROM bus
        WHERE bus.run = run;
        
        INSERT INTO driver_bus(driver_id, bus_id)
        VALUES (driver_id, bus_id);
	END
//

DELIMITER //
    CREATE 
	PROCEDURE insert_data()
	BEGIN
		INSERT INTO `flixbus`.`driver` (name, surname, company)
		VALUES 
        ('Noname1', 'Nosurname1', 'Nocompany1'),
        ('Noname2', 'Nosurname2', 'Nocompany2'),
        ('Noname3', 'Nosurname3', 'Nocompany3'),
        ('Noname4', 'Nosurname4', 'Nocompany4'),
        ('Noname5', 'Nosurname5', 'Nocompany5'),
        ('Noname6', 'Nosurname6', 'Nocompany6'),
        ('Noname7', 'Nosurname7', 'Nocompany7'),
        ('Noname8', 'Nosurname8', 'Nocompany8'),
        ('Noname9', 'Nosurname9', 'Nocompany9'),
        ('Noname10', 'Nosurname10', 'Nocompany10');
	END;
//

DELIMITER //
CREATE FUNCTION make_operation(
    operation VARCHAR(45)
)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE result DECIMAL(10,2) DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(price_of_subroute) INTO result FROM subroute;
    ELSEIF operation = 'max' THEN
        SELECT MAX(price_of_subroute) INTO result FROM subroute;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(price_of_subroute) INTO result FROM subroute;
	ELSEIF operation = 'sum'  THEN
        SELECT SUM(price_of_subroute) INTO result FROM subroute;
    END IF;
    RETURN result;
END;
//

DELIMITER //
CREATE 
PROCEDURE make_operation_subroute(
	operation VARCHAR(45)
)
BEGIN
	DECLARE result DECIMAL(10,2);
    SET result = make_operation(operation);
    SELECT result AS operation_result;
END;
//

DROP PROCEDURE IF EXISTS create_tables_from_column;
DROP VIEW IF EXISTS user_view;

DELIMITER //

CREATE PROCEDURE create_tables_from_column(
    IN custom_column_name VARCHAR(45),
    IN custom_table_name VARCHAR(45)
)
BEGIN
    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 0;
    DECLARE table_name VARCHAR(45);
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE num_columns INT;
    DECLARE column_list VARCHAR(255);
    DECLARE column_name VARCHAR(45);

    DECLARE zxcursor CURSOR FOR SELECT price FROM user_view;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @query = CONCAT('CREATE OR REPLACE VIEW user_view AS SELECT ', custom_column_name, ' AS price FROM ', custom_table_name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN zxcursor;
    my_loop: LOOP
        FETCH zxcursor INTO table_name;
        IF done THEN
            LEAVE my_loop;
        END IF;

        SET num_columns = FLOOR(1 + RAND() * 9);
    SELECT num_columns;
    SET column_list = '';
    WHILE b < num_columns DO
      SET column_name = CONCAT('column_', b + 1);
      SET column_list = CONCAT(column_list, column_name, ' INT ');
      IF b < num_columns - 1 THEN
        SET column_list = CONCAT(column_list, ', ');
      END IF;
      SET b = b + 1;
    END WHILE;
    SET b = 0;

        SET column_list = SUBSTRING(column_list, 1, LENGTH(column_list) - 1);

    SET @sql_query = CONCAT('CREATE TABLE IF NOT EXISTS ', table_name, '_', UNIX_TIMESTAMP(), ' (', column_list, ')');
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

        SET a = a + 1;
    END LOOP my_loop;
  DROP VIEW IF EXISTS user_view;
    CLOSE zxcursor;
END //

DELIMITER ;









-- insert section
INSERT INTO bus(capacity, age, run, is_own)
VALUES 
(50, 15, 19977, 0),
(100, 16, 20400, 0),
(25, 5, 1000, 0),
(122, 1, 10, 1),
(30, 2, 100, 1),
(28, 5, 1562, 1),
(46, 7, 1589, 0),
(44, 7, 12397, 1),
(18, 10, 20051, 0),
(100, 2, 1002, 1);

INSERT INTO driver(name, surname, company)
VALUES
('Iryna','Farion','Flixbus'),
('Petro','Parov','Flixbus'),
('Dua','Lipa','Flixbus'),
('Conan','Gray','astrozeneca'),
('Nelya','Lotoska','Flixbus'),
('Lef','Kolyshchastia','Levy'),
('Melanie','Martinez','Dollhouse'),
('Pirat','Jack','CarribeanBus'),
('Ivonka','Paranyak','Flixbus'),
('Zara','Larson','Flixbus');




INSERT INTO driver_bus(driver_id, bus_id)
VALUES
(1,3),
(10,3),
(2,5),
(4,7),
(6,1),
(5,10),
(8,9),
(9,2),
(7,4);

INSERT INTO passenger(name, surname, date_of_birth,phone_number)
VALUES
('Andriy','Smyk','2005-01-31','0675243216'),
('Andriy','Khoma','2005-06-25','0985622365'),
('Daryna','Bushchak','2005-04-19','0963053031'),
('Sasha','Syrotych','2005-11-11','0677758412'),
('Sasha','Sobran','2005-10-23','0984571200'),
('Sofiya','Khoma','2007-11-17','0982256365'),
('Valentyna','Akhtyrtseva','1950-11-12','0678563505'),
('Pavlo','Dudii','2005-12-02','0986544121'),
('Roman','Varekha','2014-06-27','0639862104'),
('Olya','Volodko','1996-12-31','0578963213');

INSERT INTO stop(address)
VALUES
('Lviv'),
('Kyiv'),
('Zaporizhya'),
('Ratne'),
('Ternopil'),
('Lutsk'),
('Vinnytsia'),
('Briukhovychi'),
('Dnipro'),
('Rivne');

INSERT INTO route(distance_between_2_stops, number_of_stops, start_of_the_route, end_of_the_route)
VALUES
(100, 2, 1, 6),
(50, 10, 1, 2),
(90, 4, 7, 5),
(7, 2, 1, 8),
(30, 5, 10, 8),
(200, 2, 2, 9),
(50, 12, 1, 9),
(26, 4, 1, 4),
(8, 5, 4, 6),
(500, 3, 1, 2),
(280, 9, 1, 9);

INSERT INTO stop_route(route_id,stop_id)
VALUES
(1,6),
(1,2),
(3,2),
(10,2),
(5,10),
(2,2),
(6,9),
(8,2),
(4,8),
(5,1);

INSERT INTO route_bus(route_id,bus_id)
VALUES
(1,6),
(3,2),
(10,2),
(6,9),
(2,2),
(1,2),
(8,2),
(4,8),
(5,10),
(5,1);




INSERT INTO subroute (start_of_subroute, end_of_subroute, price_of_subroute, distance_of_subroute, route_id) 
VALUES
(1, 6, 100, 100, 1),
(10, 7, 60, 75, 2),
(1, 8, 15, 7, 4),
(2, 9, 250, 200, 6),
(10, 5, 156, 132, 3),
(7, 10, 60, 100, 5),
(7, 4, 32, 30, 8),
(1, 7, 300, 250, 9),
(2, 9, 200, 204, 10),
(1, 8, 30, 26, 7);

INSERT INTO ticket(price)
VALUES
(130.50),
(200.62),
(15.00),
(30.15),
(100.00),
(60.00),
(70.32),
(205.62),
(107.15),
(20.10);





