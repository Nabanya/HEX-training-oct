CREATE TABLE registrations (
registration_id INT PRIMARY KEY,
full_name VARCHAR(100),
email VARCHAR(100),
mobile VARCHAR(40),
city VARCHAR(50),
postal_code VARCHAR(20)
);
INSERT INTO registrations VALUES
(1, ' rohit sharma ', ' ROHIT@GMAIL.COM ', '+91-98765-43210', 'hyderabad','401010'),
(2, 'SARA KHAN', 'sara@yahoo.com', '99887 66554', ' MUMBAI ', '400001'),
(3, ' amit patel ', '', '(040)99887766', 'Hyderabad', '500 032'),
(4, 'Neha Singh ', NULL, '9876543210', 'BANGALORE', '560001'),
(5, 'imran ali', 'IMRAN@MAIL.COM ', '91 9988772211', NULL, '500084'),
(6, 'Priya Rao', 'priya@gmail', '98765-AB210', 'Pune', '411001');

SELECT TRIM(full_name) AS name FROM registrations;

SELECT UPPER(TRIM(full_name)) AS name FROM registrations;

SELECT LOWER(TRIM(email)) AS email FROM registrations;

SELECT NULLIF(TRIM(email), '') AS email FROM registrations;

SELECT REPLACE(REPLACE(mobile, ' ', ''), '-', '') AS mobile FROM registrations;

SELECT REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile FROM registrations;

SELECT UPPER(TRIM(city)) AS city FROM registrations;

SELECT * FROM registrations WHERE city IS NULL;

SELECT * FROM registrations WHERE email IS NULL OR TRIM(email) = '';

SELECT * FROM registrations WHERE email REGEXP '^[A-Za-z0-9._%+-]+@gmail\\.com$';

SELECT * FROM registrations WHERE email IS NOT NULL
AND email <> '' AND email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';

SELECT REGEXP_REPLACE(postal_code, '[^0-9]', '') AS postal_code FROM registrations;

SELECT * FROM registrations WHERE mobile REGEXP '[A-Za-z]';

SELECT UPPER(TRIM(full_name)) AS name,
NULLIF(LOWER(TRIM(email)), '') AS email,
REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile,
UPPER(TRIM(city)) AS city FROM registrations;

CREATE TABLE cleaned_registrations AS
SELECT registration_id,
UPPER(TRIM(full_name)) AS full_name,
NULLIF(LOWER(TRIM(email)), '') AS email,
REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile,
UPPER(TRIM(city)) AS city,
REGEXP_REPLACE(postal_code, '[^0-9]', '') AS postal_code FROM registrations;

SELECT * from cleaned_registrations;
