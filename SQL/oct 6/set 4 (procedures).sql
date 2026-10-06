CREATE TABLE vehicles (
vehicle_id INT PRIMARY KEY,
vehicle_name VARCHAR(100),
vehicle_type VARCHAR(50),
daily_rate DECIMAL(10,2),
available_status VARCHAR(20)
);
INSERT INTO vehicles VALUES
(1, 'Honda City', 'Car', 2500, 'Available'),
(2, 'Toyota Innova', 'Car', 3500, 'Available'),
(3, 'Royal Enfield', 'Bike', 1200, 'Rented'),
(4, 'Activa', 'Scooter', 700, 'Available'),
(5, 'Mahindra Thar', 'SUV', 4500, 'Rented'),
(6, 'Hyundai Creta', 'SUV', 3200, 'Available'),
(7, 'KTM Duke', 'Bike', 1500, 'Available');

SELECT * from vehicles;
-- 1
DELIMITER //
CREATE PROCEDURE GetAllVehicles()
BEGIN
    SELECT * FROM vehicles;
END //
DELIMITER ;
call GetAllVehicles();

-- 2
DELIMITER //

CREATE PROCEDURE GetVehiclesByType(IN v_type VARCHAR(50))
BEGIN
    SELECT * FROM vehicles WHERE vehicle_type = v_type;
END //

DELIMITER ;
-- 3
DELIMITER //

CREATE PROCEDURE GetVehiclesByType(IN v_type VARCHAR(50))
BEGIN
    SELECT *
    FROM vehicles
    WHERE vehicle_type = v_type;
END //

DELIMITER ;
CALL GetVehiclesByType('Car');
-- 4
DELIMITER //

CREATE PROCEDURE GetVehiclesByMaxRate(IN max_rate DECIMAL(10,2))
BEGIN
    SELECT *
    FROM vehicles
    WHERE daily_rate <= max_rate;
END //

DELIMITER ;

-- 5
DELIMITER //

CREATE PROCEDURE UpdateVehicleRate(
    IN v_id INT,
    IN new_rate DECIMAL(10,2)
)
BEGIN
    UPDATE vehicles
    SET daily_rate = new_rate
    WHERE vehicle_id = v_id;
END //

DELIMITER ;

-- 6
DELIMITER //

CREATE PROCEDURE ChangeVehicleStatus(
    IN v_id INT,
    IN new_status VARCHAR(20)
)
BEGIN
    UPDATE vehicles
    SET available_status = new_status
    WHERE vehicle_id = v_id;
END //

DELIMITER ;

-- 7
DELIMITER //

CREATE PROCEDURE IncreaseRate(IN percentage DECIMAL(5,2))
BEGIN
    UPDATE vehicles
    SET daily_rate = daily_rate + (daily_rate * percentage / 100);
END //

DELIMITER ;

-- 8
DELIMITER //

CREATE PROCEDURE DeleteVehicle(IN v_id INT)
BEGIN
    DELETE FROM vehicles
    WHERE vehicle_id = v_id;
END //

DELIMITER ;

-- 9
DELIMITER //

CREATE PROCEDURE GetVehiclesBetweenRates(
    IN min_rate DECIMAL(10,2),
    IN max_rate DECIMAL(10,2)
)
BEGIN
    SELECT *
    FROM vehicles
    WHERE daily_rate BETWEEN min_rate AND max_rate;
END //

DELIMITER ;

-- 10
DELIMITER //

CREATE PROCEDURE CountVehiclesByType(IN v_type VARCHAR(50))
BEGIN
    SELECT COUNT(*) AS total_vehicles
    FROM vehicles
    WHERE vehicle_type = v_type;
END //

DELIMITER ;
