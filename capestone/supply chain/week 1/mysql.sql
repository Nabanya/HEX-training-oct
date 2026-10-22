CREATE DATABASE IF NOT EXISTS supply_chain_db;
USE supply_chain_db;

DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) UNIQUE NOT NULL,
    region VARCHAR(50) NOT NULL
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT,
    order_date DATE NOT NULL,
    expected_delivery_date DATE NOT NULL,
    actual_delivery_date DATE NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

CREATE TABLE inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock_level INT NOT NULL,
    reorder_threshold INT NOT NULL,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

INSERT INTO suppliers (supplier_name, contact_email, region) VALUES 
('Apex Logistics', 'apex@supply.com', 'North'),
('Beacon Components', 'beacon@supply.com', 'South'),
('Crestwood Materials', 'crestwood@supply.com', 'East'),
('Delta Freight', 'delta@supply.com', 'West'),
('Echo Electronics', 'echo@supply.com', 'North'),
('Falcon Manufacturing', 'falcon@supply.com', 'South'),
('Global Trade Co', 'global@supply.com', 'East'),
('Horizon Metals', 'horizon@supply.com', 'West'),
('Imperial Plastics', 'imperial@supply.com', 'North'),
('Jupiter Cargo', 'jupiter@supply.com', 'South'),
('Kilo Tech', 'kilo@supply.com', 'East'),
('Lunar Packaging', 'lunar@supply.com', 'West'),
('Matrix Chemical', 'matrix@supply.com', 'North'),
('Nexus Distribution', 'nexus@supply.com', 'South'),
('Omega Resources', 'omega@supply.com', 'East');

INSERT INTO orders (supplier_id, order_date, expected_delivery_date, actual_delivery_date, status) VALUES 
(1, '2026-10-01', '2026-10-05', '2026-10-08', 'Delivered'),
(2, '2026-10-01', '2026-10-05', '2026-10-04', 'Delivered'),
(3, '2026-10-02', '2026-10-06', '2026-10-10', 'Delivered'),
(4, '2026-10-02', '2026-10-06', '2026-10-06', 'Delivered'),
(5, '2026-10-03', '2026-10-07', '2026-10-12', 'Delivered'),
(6, '2026-10-03', '2026-10-07', '2026-10-07', 'Delivered'),
(7, '2026-10-04', '2026-10-08', NULL, 'Pending'),
(8, '2026-10-04', '2026-10-08', '2026-10-09', 'Delivered'),
(9, '2026-10-05', '2026-10-09', '2026-10-09', 'Delivered'),
(10, '2026-10-05', '2026-10-09', '2026-10-14', 'Delivered'),
(11, '2026-10-06', '2026-10-10', '2026-10-10', 'Delivered'),
(12, '2026-10-06', '2026-10-10', NULL, 'Pending'),
(13, '2026-10-07', '2026-10-11', '2026-10-15', 'Delivered'),
(14, '2026-10-07', '2026-10-11', '2026-10-11', 'Delivered'),
(15, '2026-10-08', '2026-10-12', '2026-10-18', 'Delivered');

INSERT INTO inventory (item_name, stock_level, reorder_threshold, supplier_id) VALUES 
('Microcontrollers', 120, 50, 1), ('Steel Rods', 15, 30, 2), ('Copper Wire', 200, 100, 3),
('Plastic Casing', 40, 50, 4), ('LED Panels', 500, 150, 5), ('Aluminum Sheets', 10, 25, 6),
('Cardboard Boxes', 800, 200, 7), ('Lithium Batteries', 25, 40, 8), ('Circuit Boards', 300, 80, 9),
('Rubber Seals', 600, 150, 10), ('Glass Panels', 18, 30, 11), ('Screws & Bolts', 1500, 500, 12),
('Chemical Coolant', 35, 50, 13), ('Packing Tape', 400, 100, 14), ('Solder Wire', 90, 40, 15);

DELIMITER //
CREATE PROCEDURE AutoReorderCheck()
BEGIN
    SELECT 
        i.item_id, i.item_name, i.stock_level, i.reorder_threshold,
        s.supplier_name, s.contact_email,
        (i.reorder_threshold * 2 - i.stock_level) AS suggested_reorder_qty
    FROM inventory i
    JOIN suppliers s ON i.supplier_id = s.supplier_id
    WHERE i.stock_level <= i.reorder_threshold;
END //
DELIMITER ;