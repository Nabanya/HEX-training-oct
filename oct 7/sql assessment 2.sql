CREATE DATABASE airline_assessment;
USE airline_assessment;

CREATE TABLE flights (
flight_id INT PRIMARY KEY,
airline VARCHAR(50),
source_city VARCHAR(50),
destination_city VARCHAR(50),
ticket_price DECIMAL(10,2)
);
INSERT INTO flights VALUES
(201, 'SkyJet', 'Hyderabad', 'Delhi', 6500),
(202, 'AirWorld', 'Mumbai', 'Bangalore', 7200),
(203, 'SkyJet', 'Delhi', 'Mumbai', 5800),
(204, 'FlyHigh', 'Hyderabad', 'Dubai', 18000),
(205, 'AirWorld', 'Bangalore', 'Delhi', 6900),
(206, 'FlyHigh', 'Mumbai', 'Singapore', 22000),
(207, 'SkyJet', 'Hyderabad', 'Mumbai', 5200);

CREATE TABLE passengers (
passenger_id INT PRIMARY KEY,
passenger_name VARCHAR(100),
city VARCHAR(50),
email VARCHAR(100)
);
INSERT INTO passengers VALUES
(1, 'Aman Verma', 'Hyderabad', ' AMAN@MAIL.COM '),
(2, 'Sara Ali', 'Mumbai', 'sara@gmail.com'),
(3, 'Rakesh Rao', 'Delhi', ''),
(4, 'Meena Shah', 'Bangalore', 'MEENA@YAHOO.COM'),
(5, 'Farah Khan', 'Hyderabad', NULL),
(6, 'John Mathew', 'Pune', 'john@gmail.com'),
(7, 'Priya Das', NULL, 'priya@mail.com');


CREATE TABLE bookings (
booking_id INT PRIMARY KEY,
passenger_id INT,
flight_id INT,
booking_date DATE,
seats INT,
status VARCHAR(20)
);
INSERT INTO bookings VALUES
(1001, 1, 201, '2026-06-01', 1, 'Confirmed'),
(1002, 2, 202, '2026-06-02', 2, 'Confirmed'),
(1003, 1, 204, '2026-06-03', 1, 'Confirmed'),
(1004, 3, 203, '2026-06-04', 1, 'Cancelled'),
(1005, 4, 205, '2026-06-05', 3, 'Confirmed'),
(1006, 5, 207, '2026-06-06', 2, 'Confirmed'),
(1007, 2, 206, '2026-06-07', 1, 'Confirmed'),
(1008, 20, 201, '2026-06-08', 1, 'Confirmed'),
(1009, 6, NULL, '2026-06-09', 2, 'Pending');

CREATE TABLE airline_staff (
employee_id INT PRIMARY KEY,
employee_name VARCHAR(100),
manager_id INT,
department VARCHAR(50),
salary DECIMAL(10,2)
);

INSERT INTO airline_staff VALUES
(1, 'Raj Kumar', NULL, 'Management', 200000),
(2, 'Meera Rao', 1, 'Operations', 140000),
(3, 'Imran Khan', 1, 'Sales', 135000),
(4, 'Aman Shah', 2, 'Operations', 90000),
(5, 'Priya Singh', 2, 'Operations', 85000),
(6, 'Rohit Das', 3, 'Sales', 75000),
(7, 'Farah Ali', 3, 'Sales', 78000),
(8, 'Vikas Rao', 4, 'Support', 60000);


-- section a
SELECT * FROM flights;
SELECT * from bookings;
SELECT * from passengers;
-- q1
SELECT * FROM flights where source_city="Hyderabad";
-- q2
SELECT * FROM flights where ticket_price BETWEEN 6000 AND 20000;
-- q3
SELECT * from flights where destination_city NOT IN ('Hyderabad','Mumbai','Bangalore','Delhi')
AND ticket_price>15000;
-- q4
UPDATE flights set ticket_price=0.05*ticket_price+ticket_price WHERE airline='SkyJet';
SELECT * FROM flights;
-- q5
SELECT * from flights ORDER BY ticket_price desc LIMIT 3;

-- secction b
-- q6
SELECT airline,AVG(ticket_price) as avg_price FROM flights GROUP BY airline;
-- q7
SELECT flight_id ,SUM(seats) as seats_booked FROM bookings where flight_id is not null GROUP by flight_id; 
-- q8
SELECT airline, AVG(ticket_price) as avgprice from flights GROUP BY airline HAVING avgprice>8000;
-- q9
SELECT f.airline,sum(b.seats*f.ticket_price) as tot_book_val from flights f LEFT JOIN bookings b 
on f.flight_id=b.flight_id GROUP BY f.airline;

-- section c
-- q10

SELECT p.passenger_name,f.airline,f.source_city,f.destination_city,b.status from bookings b
JOIN passengers p on p.passenger_id=b.passenger_id JOIN flights f on b.flight_id=f.flight_id;

-- q11
SELECT * FROM passengers p left JOIN bookings b on p.passenger_id=b.passenger_id;
-- q12
SELECT * FROM bookings b LEFT JOIN passengers p ON b.passenger_id=p.passenger_id WHERE
p.passenger_id is NULL OR b.flight_id is NULL;
-- q13
SELECT p.passenger_id,p.passenger_name ,SUM(f.ticket_price * b.seats) as tot_booking_val FROM 
passengers p LEFT JOIN bookings b on b.passenger_id=p.passenger_id left join flights f on f.flight_id=b.flight_id
GROUP BY p.passenger_id;

-- q14
SELECT p.passenger_id,p.passenger_name,sum(b.seats * f.ticket_price) as tot_price from passengers p 
JOIN bookings b on b.passenger_id=p.passenger_id JOIN flights f on f.flight_id=b.flight_id 
WHERE b.status='Confirmed' GROUP by p.passenger_id HAVING tot_price>10000;
