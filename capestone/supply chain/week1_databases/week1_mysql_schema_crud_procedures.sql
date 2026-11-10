
DROP DATABASE IF EXISTS supply_chain;
CREATE DATABASE supply_chain;
USE supply_chain;

-- 1. SCHEMA

CREATE TABLE suppliers (
    supplier_id   VARCHAR(10)  PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    lead_time_days INT DEFAULT 7
);

CREATE TABLE inventory (
    product_id     INT AUTO_INCREMENT PRIMARY KEY,
    product_name   VARCHAR(100) NOT NULL,
    supplier_id    VARCHAR(10)  NOT NULL,
    stock_qty      INT NOT NULL DEFAULT 0,
    reorder_level  INT NOT NULL DEFAULT 50,
    reorder_qty    INT NOT NULL DEFAULT 200,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE orders (
    order_id               VARCHAR(10) PRIMARY KEY,
    supplier_id            VARCHAR(10) NOT NULL,
    product_id             INT NOT NULL,
    quantity               INT NOT NULL,
    order_date             DATE NOT NULL,
    expected_delivery_date DATE NOT NULL,
    delivery_date          DATE NULL,
    status                 ENUM('PLACED','SHIPPED','DELIVERED','CANCELLED') DEFAULT 'PLACED',
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (product_id)  REFERENCES inventory(product_id)
);

CREATE INDEX idx_orders_supplier_date ON orders (supplier_id, order_date);

-- 2. CRUD
-- CREATE
INSERT INTO suppliers (supplier_id, supplier_name, contact_email, lead_time_days) VALUES
 ('S001', 'Alpha Metals',    'sales@alphametals.example', 7),
 ('S002', 'Beta Components', 'info@betacomp.example',     10),
 ('S003', 'Gamma Packaging', 'hello@gammapack.example',   5);

INSERT INTO inventory (product_name, supplier_id, stock_qty, reorder_level, reorder_qty) VALUES
 ('Steel Rods',     'S001', 120, 50, 200),
 ('Circuit Boards', 'S002',  40, 60, 150),
 ('Packaging Box',  'S003', 300, 100, 500);

INSERT INTO orders (order_id, supplier_id, product_id, quantity, order_date, expected_delivery_date, delivery_date, status) VALUES
 ('O0001', 'S001', 1, 100, '2026-01-05', '2026-01-12', '2026-01-14', 'DELIVERED'),
 ('O0002', 'S002', 2,  80, '2026-01-08', '2026-01-18', '2026-01-17', 'DELIVERED'),
 ('O0003', 'S003', 3, 250, '2026-01-10', '2026-01-15', NULL,         'SHIPPED');

-- READ
SELECT * FROM orders WHERE status = 'SHIPPED';

SELECT o.order_id, s.supplier_name, o.quantity,
       DATEDIFF(o.delivery_date, o.expected_delivery_date) AS delay_days
FROM orders o
JOIN suppliers s ON s.supplier_id = o.supplier_id
WHERE o.delivery_date IS NOT NULL;

-- UPDATE
UPDATE orders
SET status = 'DELIVERED', delivery_date = '2026-01-16'
WHERE order_id = 'O0003';

-- DELETE
DELETE FROM orders WHERE order_id = 'O0003';

-- 3. STORED PROCEDURE: auto reorder

DELIMITER $$

CREATE PROCEDURE sp_auto_reorder()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE v_product_id INT;
    DECLARE v_supplier_id VARCHAR(10);
    DECLARE v_qty INT;
    DECLARE v_lead INT;

    DECLARE low_stock CURSOR FOR
        SELECT i.product_id, i.supplier_id, i.reorder_qty, s.lead_time_days
        FROM inventory i
        JOIN suppliers s ON s.supplier_id = i.supplier_id
        WHERE i.stock_qty < i.reorder_level;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN low_stock;
    reorder_loop: LOOP
        FETCH low_stock INTO v_product_id, v_supplier_id, v_qty, v_lead;
        IF done = 1 THEN
            LEAVE reorder_loop;
        END IF;

        INSERT INTO orders (order_id, supplier_id, product_id, quantity,
                            order_date, expected_delivery_date, status)
        VALUES (CONCAT('AUTO', LPAD(FLOOR(RAND() * 99999), 5, '0')),
                v_supplier_id, v_product_id, v_qty,
                CURDATE(), DATE_ADD(CURDATE(), INTERVAL v_lead DAY), 'PLACED');
    END LOOP;
    CLOSE low_stock;
END$$

DELIMITER ;

DELIMITER $$
CREATE TRIGGER trg_inventory_low_stock
AFTER UPDATE ON inventory
FOR EACH ROW
BEGIN
    IF NEW.stock_qty < NEW.reorder_level AND OLD.stock_qty >= OLD.reorder_level THEN
        INSERT INTO orders (order_id, supplier_id, product_id, quantity,
                            order_date, expected_delivery_date, status)
        VALUES (CONCAT('TRG', LPAD(FLOOR(RAND() * 99999), 5, '0')),
                NEW.supplier_id, NEW.product_id, NEW.reorder_qty,
                CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'PLACED');
    END IF;
END$$
DELIMITER ;

CALL sp_auto_reorder();
SELECT * FROM orders WHERE order_id LIKE 'AUTO%';
