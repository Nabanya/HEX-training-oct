CREATE DATABASE telecom_assessment;
USE telecom_assessment;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    mobile VARCHAR(30),
    email VARCHAR(100)
);
INSERT INTO customers VALUES
(1, '  Arjun Rao ', 'Hyderabad', '98765-43210', ' ARJUN@GMAIL.COM '),
(2, 'SARA KHAN', 'Mumbai', '+91 99887 66554', 'sara@gmail.com'),
(3, 'Rohit Mehta ', 'Delhi', '9988 776 655', ''),
(4, 'Neha Singh', 'Hyderabad', '9876543210', 'neha@yahoo.com'),
(5, 'Imran Ali', 'Bangalore', '98765-AB210', NULL),
(6, 'Priya Nair', 'Pune', '9123456789', 'PRIYA@GMAIL.COM'),
(7, 'Kabir Shah', NULL, '9000011111', 'kabir@mail.com');
CREATE TABLE plans (
    plan_id INT PRIMARY KEY,
    plan_name VARCHAR(50),
    monthly_charge DECIMAL(10,2)
);
INSERT INTO plans VALUES
(101, 'Basic', 399),
(102, 'Standard', 599),
(103, 'Premium', 999),
(104, 'Unlimited', 1499),
(105, 'Business', 1999);
CREATE TABLE subscriptions (
    subscription_id INT PRIMARY KEY,
    customer_id INT,
    plan_id INT,
    start_date DATE,
status VARCHAR(20)
);
INSERT INTO subscriptions VALUES
(1001, 1, 103, '2026-01-01', 'Active'),
(1002, 2, 102, '2026-01-15', 'Active'),
(1003, 3, 101, '2026-02-01', 'Inactive'),
(1004, 4, 104, '2026-02-10', 'Active'),
(1005, 5, 102, '2026-03-01', 'Active'),
(1006, 1, 105, '2026-04-01', 'Active'),
(1007, 6, NULL, '2026-04-15', 'Pending'),
(1008, 20, 103, '2026-05-01', 'Active');
CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    customer_id INT,
    payment_date DATE,
    amount DECIMAL(10,2)
);
INSERT INTO payments VALUES
(501, 1, '2026-01-05', 999),
(502, 2, '2026-01-18', 599),
(503, 1, '2026-02-05', 999),
(504, 3, '2026-02-10', 399),
(505, 4, '2026-02-15', 1499),
(506, 2, '2026-03-18', 599),
(507, 5, '2026-03-20', 599),
(508, 1, '2026-04-05', 1999),
(509, 4, '2026-04-15', 1499),
(510, 5, '2026-05-20', 599),
(511, 2, '2026-05-22', 599),
(512, 1, '2026-06-05', 1999);

-- section a
-- q1
SELECT customer_name,city,email FROM customers;
-- q2
SELECT customer_name,city from customers WHERE city IN("Hyderabad","Mumbai");
-- q3
select customer_name from customers WHERE customer_name LIKE '%a%';
-- q4
INSERT into customers value(8,'Nabanya Sri','Chennai','9500841838','nabbr@gmail.com');
select * from customers;
-- q5
UPDATE customers SET city='Chennai' where customer_id=6;
select * from customers;
-- q6
DELETE from customers where customer_id=8;
-- q7
SELECT customer_name from customers ORDER BY customer_name;

-- section b
-- q8
SELECT COUNT(payment_id) as tot_of_payments,SUM(amount) AS tot_amt FROM payments;
-- q9
SELECT customer_id,SUM(amount)as tot_pay_amt from payments GROUP BY customer_id;
-- q10
SELECT c.customer_id,c.customer_name,SUM(p.amount)as tot_amt from customers c LEFT JOIN
payments p on c.customer_id=p.customer_id GROUP BY c.customer_id HAVING tot_amt>2000;
-- q11
SELECT customer_id,AVG(amount)as avg_pay_amt from payments GROUP BY customer_id;

-- section c
-- q12
SELECT c.customer_name,pl.plan_name,pl.monthly_charge,s.status from customers c JOIN
subscriptions s on c.customer_id=s.customer_id JOIN plans pl on pl.plan_id=s.plan_id;
-- q13
SELECT *,s.status from customers c left JOIN subscriptions s ON c.customer_id=s.customer_id;
-- q14
SELECT * from subscriptions s LEFT JOIN customers c on s.customer_id=c.customer_id LEFT JOIN plans pl
on pl.plan_id=s.plan_id WHERE c.customer_id is NULL or pl.plan_id is NULL;


-- section d
-- q15
-- SELECT customer_id, TRIM(customer_name) as cus_name from customers;
-- SELECT customer_id,LOWER(email) Email FROM customers;
-- SELECT customer_id,NULLIF(trim(email),'') as e_mail from customers;
-- SELECT  customer_id,REGEXP_REPLACE(mobile,'[^0-9]','') as mobile_no from customers;

SELECT customer_id, TRIM(customer_name) as cus_name, 
LOWER(email) AS Email,
NULLIF(LOWER(trim(email)),'') as e_mail,
REGEXP_REPLACE(mobile,'[^0-9]','') as mobile_no from customers;


-- q16
SELECT * FROM customers WHERE mobile REGEXP '[A-Za-z]';







