CREATE DATABASE sql_practice_pack;
USE sql_practice_pack;
CREATE TABLE menu_items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    available_qty INT
);
 
INSERT INTO menu_items VALUES
(1, 'Chicken Biryani', 'Main Course', 320, 25),
(2, 'Paneer Tikka', 'Starter', 240, 15),
(3, 'Masala Dosa', 'Breakfast', 120, 30),
(4, 'Veg Burger', 'Fast Food', 180, 10),
(5, 'Cold Coffee', 'Beverage', 150, 20),
(6, 'Chicken Burger', 'Fast Food', 220, 8),
(7, 'Idli', 'Breakfast', 80, 40),
(8, 'Fresh Lime', 'Beverage', 90, 0);

SELECT * FROM menu_items;

SELECT item_name, price FROM menu_items;

INSERT INTO menu_items VALUES (9, 'Veg Pizza', 'Main Course', 250, 12);
SELECT * FROM menu_items;


UPDATE menu_items SET price = 350 WHERE item_name = 'Chicken Biryani';
SELECT * FROM menu_items;

UPDATE menu_items SET price = price * 1.10 WHERE category = 'Fast Food';
SELECT * FROM menu_items;

UPDATE menu_items SET available_qty = available_qty - 2 WHERE item_name = 'Veg Burger';
SELECT * FROM menu_items;

DELETE FROM menu_items WHERE available_qty = 0;
SELECT * FROM menu_items;

SELECT * FROM menu_items WHERE price > 200;

SELECT * FROM menu_items WHERE price BETWEEN 100 AND 250;

SELECT * FROM menu_items WHERE category = 'Breakfast';

SELECT * FROM menu_items WHERE category IN ('Breakfast', 'Beverage');

SELECT * FROM menu_items WHERE item_name LIKE '%Chicken%';

SELECT * FROM menu_items ORDER BY price DESC;

SELECT * FROM menu_items ORDER BY price DESC LIMIT 3;

SELECT * FROM menu_items WHERE available_qty < 15;


-- set 2
CREATE TABLE food_orders (
    order_id INT PRIMARY KEY,
    restaurant VARCHAR(100),
    city VARCHAR(50),
    food_type VARCHAR(50),
    order_amount DECIMAL(10,2),
    delivery_partner VARCHAR(50),
    order_date DATE
);

INSERT INTO food_orders VALUES
(101, 'Spice Hub', 'Hyderabad', 'Indian', 850, 'Ravi', '2026-09-01'),
(102, 'Burger Zone', 'Hyderabad', 'Fast Food', 520, 'Kiran', '2026-09-01'),
(103, 'Pizza Point', 'Mumbai', 'Fast Food', 1100, 'Ravi', '2026-09-02'),
(104, 'Curry House', 'Bangalore', 'Indian', 760, 'Aman', '2026-09-02'),
(105, 'Spice Hub', 'Hyderabad', 'Indian', 1250, 'Kiran', '2026-09-03'),
(106, 'Sushi World', 'Mumbai', 'Japanese', 1800, 'Aman', '2026-09-03'),
(107, 'Pizza Point', 'Mumbai', 'Fast Food', 900, 'Ravi', '2026-09-04'),
(108, 'Curry House', 'Bangalore', 'Indian', 640, 'Kiran', '2026-09-04'),
(109, 'Burger Zone', 'Hyderabad', 'Fast Food', 430, 'Aman', '2026-09-05'),
(110, 'Sushi World', 'Mumbai', 'Japanese', 2100, 'Ravi', '2026-09-05'),
(111, 'Spice Hub', 'Hyderabad', 'Indian', 950, 'Aman', '2026-09-06'),
(112, 'Curry House', 'Bangalore', 'Indian', 880, 'Ravi', '2026-09-06');

SELECT COUNT(*) AS total_orders FROM food_orders;

SELECT SUM(order_amount) AS total_revenue FROM food_orders;

SELECT AVG(order_amount) AS average_order FROM food_orders;

SELECT MAX(order_amount) AS highest_order FROM food_orders;

SELECT MIN(order_amount) AS lowest_order FROM food_orders;

SELECT restaurant, COUNT(*) AS total_orders FROM food_orders GROUP BY restaurant;

SELECT food_type, AVG(order_amount) AS average_order FROM food_orders
GROUP BY food_type;

SELECT delivery_partner, SUM(order_amount) AS total_revenue FROM food_orders
GROUP BY delivery_partner;

SELECT city, COUNT(*) AS total_orders FROM food_orders
GROUP BY city HAVING COUNT(*) > 3;

SELECT restaurant, SUM(order_amount) AS total_revenue FROM food_orders
GROUP BY restaurant HAVING SUM(order_amount) > 2000;

SELECT delivery_partner, AVG(order_amount) AS average_order FROM food_orders
GROUP BY delivery_partner HAVING AVG(order_amount) > 800;

SELECT food_type, SUM(order_amount) AS total_revenue FROM food_orders
GROUP BY food_type HAVING SUM(order_amount) > 2500;

SELECT city, SUM(order_amount) AS total_revenue FROM food_orders
GROUP BY city ORDER BY total_revenue DESC;

SELECT restaurant, SUM(order_amount) AS total_revenue FROM food_orders
GROUP BY restaurant ORDER BY total_revenue DESC LIMIT 1;

-- set 3
CREATE TABLE students (
student_id INT PRIMARY KEY,
student_name VARCHAR(100),
city VARCHAR(50)
);
INSERT INTO students VALUES
(1, 'Arun', 'Hyderabad'),
(2, 'Megha', 'Mumbai'),
(3, 'Zaid', 'Hyderabad'),
(4, 'Pooja', 'Pune'),
(5, 'Rohan', 'Delhi'),
(6, 'Sana', NULL),
(7, 'Vijay', 'Bangalore');

SELECT * FROM students;

CREATE TABLE courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(100),
fee DECIMAL(10,2)
);

INSERT INTO courses VALUES
(101, 'Python', 15000),
(102, 'Data Engineering', 25000),
(103, 'Power BI', 12000),
(104, 'Cloud Computing', 20000),
(105, 'Cyber Security', 22000),
(106, 'Machine Learning', 28000);
SELECT * FROM courses;


CREATE TABLE enrollments (
enrollment_id INT PRIMARY KEY,
student_id INT,
course_id INT,
enrollment_date DATE
);
INSERT INTO enrollments VALUES
(1001, 1, 101, '2026-09-01'),
(1002, 1, 102, '2026-09-03'),
(1003, 2, 103, '2026-09-04'),
(1004, 3, 102, '2026-09-05'),
(1005, 4, 104, '2026-09-06'),
(1006, 2, 101, '2026-09-07'),
(1007, 3, 105, '2026-09-08'),
(1008, 20, 102, '2026-09-09'),
(1009, 5, NULL, '2026-09-10');
SELECT * FROM enrollments;

-- 1
SELECT s.student_name, c.course_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON e.course_id = c.course_id;
-- 2
SELECT s.student_name, s.city, c.course_name, c.fee
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON e.course_id = c.course_id;
-- 3
SELECT s.student_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_name = 'Data Engineering';
-- 4
SELECT s.student_name, c.course_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
LEFT JOIN courses c
ON e.course_id = c.course_id;
-- 5
SELECT s.student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;
-- 6
SELECT c.course_name, s.student_name
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
LEFT JOIN students s
ON e.student_id = s.student_id;
-- 7
SELECT c.course_name
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
WHERE e.course_id IS NULL;
-- 8
SELECT e.*
FROM enrollments e
LEFT JOIN students s
ON e.student_id = s.student_id
WHERE s.student_id IS NULL;
-- 9
SELECT e.*
FROM enrollments e
LEFT JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_id IS NULL;
-- 10
SELECT s.student_name, COUNT(e.course_id) AS total_courses
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name;
-- 11
SELECT s.student_name, SUM(c.fee) AS total_fees
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON e.course_id = c.course_id
GROUP BY s.student_id, s.student_name;
-- 12
SELECT s.student_name, COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name
HAVING COUNT(e.course_id) > 1;
-- 13
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
HAVING COUNT(e.student_id) > 1;
-- 14
SELECT c.course_name, SUM(c.fee) AS total_revenue
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;
-- 15
SELECT c.course_name, SUM(c.fee) AS total_revenue
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY total_revenue DESC
LIMIT 1;