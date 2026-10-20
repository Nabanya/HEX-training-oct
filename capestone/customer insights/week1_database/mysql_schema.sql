CREATE DATABASE IF NOT EXISTS customer_orders_db;
USE customer_orders_db;

DROP TABLE IF EXISTS delivery_status;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

-- Create Tables
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    region VARCHAR(50) NOT NULL
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE delivery_status (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    expected_delivery_date DATE NOT NULL,
    actual_delivery_date DATE NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Seed Data (15 Records)
INSERT INTO customers (name, email, region) VALUES 
('Alice Smith', 'alice@example.com', 'North'),
('Bob Jones', 'bob@example.com', 'South'),
('Charlie Brown', 'charlie@example.com', 'East'),
('Diana Prince', 'diana@example.com', 'West'),
('Evan Wright', 'evan@example.com', 'North'),
('Fiona Gallagher', 'fiona@example.com', 'South'),
('George Clark', 'george@example.com', 'East'),
('Hannah Abbott', 'hannah@example.com', 'West'),
('Ian Malcolm', 'ian@example.com', 'North'),
('Julia Roberts', 'julia@example.com', 'South'),
('Kevin Bacon', 'kevin@example.com', 'East'),
('Laura Croft', 'laura@example.com', 'West'),
('Michael Scott', 'michael@example.com', 'North'),
('Nina Nina', 'nina@example.com', 'South'),
('Oscar Martinez', 'oscar@example.com', 'East');

INSERT INTO orders (customer_id, order_date) VALUES 
(1, '2026-10-01'), (2, '2026-10-01'), (3, '2026-10-02'), (4, '2026-10-02'),
(5, '2026-10-03'), (1, '2026-10-03'), (6, '2026-10-04'), (7, '2026-10-04'),
(8, '2026-10-05'), (9, '2026-10-05'), (10, '2026-10-06'), (11, '2026-10-06'),
(12, '2026-10-07'), (13, '2026-10-07'), (14, '2026-10-08');

INSERT INTO delivery_status (order_id, expected_delivery_date, actual_delivery_date, status) VALUES 
(1, '2026-10-05', '2026-10-08', 'Delivered'),
(2, '2026-10-05', '2026-10-04', 'Delivered'),
(3, '2026-10-06', '2026-10-10', 'Delivered'),
(4, '2026-10-06', '2026-10-06', 'Delivered'),
(5, '2026-10-07', '2026-10-12', 'Delivered'),
(6, '2026-10-07', '2026-10-07', 'Delivered'),
(7, '2026-10-08', NULL, 'Pending'),
(8, '2026-10-08', '2026-10-09', 'Delivered'),
(9, '2026-10-09', '2026-10-09', 'Delivered'),
(10, '2026-10-09', '2026-10-14', 'Delivered'),
(11, '2026-10-10', '2026-10-10', 'Delivered'),
(12, '2026-10-10', NULL, 'Pending'),
(13, '2026-10-11', '2026-10-15', 'Delivered'),
(14, '2026-10-11', '2026-10-11', 'Delivered'),
(15, '2026-10-12', '2026-10-18', 'Delivered');

-- Stored Procedure
DELIMITER //
CREATE PROCEDURE GetDelayedDeliveriesByCustomer(IN p_customer_id INT)
BEGIN
    SELECT 
        c.customer_id,
        c.name,
        o.order_id,
        ds.expected_delivery_date,
        ds.actual_delivery_date,
        ds.status,
        DATEDIFF(COALESCE(ds.actual_delivery_date, CURDATE()), ds.expected_delivery_date) AS delay_days
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN delivery_status ds ON o.order_id = ds.order_id
    WHERE c.customer_id = p_customer_id
      AND (
          (ds.actual_delivery_date IS NOT NULL AND ds.actual_delivery_date > ds.expected_delivery_date)
          OR 
          (ds.actual_delivery_date IS NULL AND ds.expected_delivery_date < CURDATE())
      );
END //
DELIMITER ;