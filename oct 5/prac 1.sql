USE shop_db;

SHOW tables;


desc products;

CREATE TABLE products (
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2),
    StockQuantity INT
);

select * from products;

SELECT ProductName, Price
FROM products;


UPDATE products
SET Price = 60000.00
WHERE ProductID = 1;

UPDATE products
SET Price = Price * 1.10
WHERE Category = 'Electronics';

UPDATE products
SET StockQuantity = StockQuantity - 1
WHERE ProductID = 2;

UPDATE products
SET Category = 'Electronics'
WHERE ProductID = 6;

SELECT *
FROM products
WHERE Price > 1000;

SELECT *
FROM products
WHERE StockQuantity < 10;


SELECT *
FROM products
WHERE Category = 'Electronics';

SELECT *
FROM products
ORDER BY Price DESC;

DELETE FROM products
WHERE ProductID = 5;

DELETE FROM products
WHERE StockQuantity = 0;

SELECT *
FROM products;