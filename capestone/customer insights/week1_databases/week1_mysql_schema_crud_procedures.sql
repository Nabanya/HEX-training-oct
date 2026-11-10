
DROP DATABASE IF EXISTS customer_orders;
CREATE DATABASE customer_orders;
USE customer_orders;

CREATE TABLE customers (
    customer_id   INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email         VARCHAR(100),
    region        VARCHAR(20)
);

CREATE TABLE orders (
    order_id               VARCHAR(10) PRIMARY KEY,
    customer_id            INT NOT NULL,
    order_date             DATE NOT NULL,
    expected_delivery_date DATE NOT NULL,
    delivery_date          DATE NULL,
    delivery_issue         VARCHAR(100) NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- One row per status change, so the latest row = current status
CREATE TABLE delivery_status (
    status_id   INT AUTO_INCREMENT PRIMARY KEY,
    order_id    VARCHAR(10) NOT NULL,
    status      ENUM('PLACED','SHIPPED','OUT_FOR_DELIVERY','DELIVERED','DELAYED') NOT NULL,
    status_date DATE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

CREATE INDEX idx_orders_customer ON orders (customer_id);
CREATE INDEX idx_status_order    ON delivery_status (order_id);

-- 2. CRUD (on orders)
INSERT INTO customers (customer_name, email, region) VALUES
 ('Asha Kumar',  'asha@example.com',  'South'),
 ('Ravi Sharma', 'ravi@example.com',  'North'),
 ('Meena Iyer',  'meena@example.com', 'West');

INSERT INTO orders (order_id, customer_id, order_date, expected_delivery_date, delivery_date, delivery_issue) VALUES
 ('ORD0001', 1, '2026-03-01', '2026-03-06', '2026-03-09', 'Courier delay'),
 ('ORD0002', 1, '2026-03-10', '2026-03-15', '2026-03-14', NULL),
 ('ORD0003', 2, '2026-03-12', '2026-03-18', '2026-03-22', 'Weather'),
 ('ORD0004', 3, '2026-03-15', '2026-03-20', NULL,         NULL);

INSERT INTO delivery_status (order_id, status, status_date) VALUES
 ('ORD0001', 'PLACED',  '2026-03-01'),
 ('ORD0001', 'SHIPPED', '2026-03-02'),
 ('ORD0001', 'DELAYED', '2026-03-09'),
 ('ORD0002', 'PLACED',  '2026-03-10'),
 ('ORD0002', 'DELIVERED', '2026-03-14'),
 ('ORD0003', 'PLACED',  '2026-03-12'),
 ('ORD0003', 'DELAYED', '2026-03-22'),
 ('ORD0004', 'PLACED',  '2026-03-15');

SELECT * FROM orders WHERE customer_id = 1;

SELECT o.order_id, c.customer_name, c.region,
       DATEDIFF(o.delivery_date, o.expected_delivery_date) AS delay_days
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.delivery_date IS NOT NULL;

-- UPDATE
UPDATE orders SET delivery_date = '2026-03-19' WHERE order_id = 'ORD0004';
INSERT INTO delivery_status (order_id, status, status_date) VALUES ('ORD0004', 'DELIVERED', '2026-03-19');

-- DELETE (status rows are removed too because of ON DELETE CASCADE)
DELETE FROM orders WHERE order_id = 'ORD0002';

--  3. STORED PROCEDURE: all delayed deliveries for a customer

DELIMITER $$

CREATE PROCEDURE sp_get_delayed_deliveries(IN p_customer_id INT)
BEGIN
    SELECT o.order_id,
           o.expected_delivery_date,
           o.delivery_date,
           DATEDIFF(o.delivery_date, o.expected_delivery_date) AS delay_days,
           o.delivery_issue
    FROM orders o
    WHERE o.customer_id = p_customer_id
      AND o.delivery_date IS NOT NULL
      AND o.delivery_date > o.expected_delivery_date
    ORDER BY delay_days DESC;
END$$

DELIMITER ;

CALL sp_get_delayed_deliveries(1);
