
CREATE TABLE patients (
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
age INT,
city VARCHAR(50)
);
INSERT INTO patients VALUES
(1, 'Rohan Das', 34, 'Hyderabad'),
(2, 'Meena Iyer', 46, 'Chennai'),
(3, 'Kabir Khan', 29, 'Hyderabad'),
(4, 'Lakshmi Rao', 61, 'Bangalore'),
(5, 'John Mathew', 38, 'Mumbai'),
(6, 'Ayesha Ali', 25, NULL),
(7, 'Naveen Reddy', 52, 'Pune');



CREATE TABLE doctors (
doctor_id INT PRIMARY KEY,
doctor_name VARCHAR(100),
specialization VARCHAR(50),
consultation_fee DECIMAL(10,2)
);
INSERT INTO doctors VALUES
(101, 'Dr. Sharma', 'Cardiology', 1200),
(102, 'Dr. Farah', 'Dermatology', 800),
(103, 'Dr. Joseph', 'Orthopedics', 1000),
(104, 'Dr. Mehta', 'General Medicine', 600),

(105, 'Dr. Sana', 'Neurology', 1500),
(106, 'Dr. Rao', 'Pediatrics', 700);


CREATE TABLE appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
status VARCHAR(30)
);
INSERT INTO appointments VALUES
(1001, 1, 101, '2026-10-01', 'Completed'),
(1002, 2, 104, '2026-10-01', 'Completed'),
(1003, 3, 102, '2026-10-02', 'Cancelled'),
(1004, 1, 105, '2026-10-03', 'Completed'),
(1005, 4, 101, '2026-10-03', 'Scheduled'),
(1006, 5, 103, '2026-10-04', 'Completed'),
(1007, 3, 104, '2026-10-04', 'Completed'),
(1008, NULL, 102, '2026-10-05', 'Scheduled'),
(1009, 20, 103, '2026-10-05', 'Completed'),
(1010, 2, NULL, '2026-10-06', 'Scheduled');

SELECT a.appointment_id,p.patient_name,d.doctor_name, a.appointment_date FROM 
appointments a, patients p, doctors d;

SELECT d.doctor_name,d.specialization FROM doctors d JOIN appointments a
ON d.doctor_id=a.doctor_id where a.status="Completed";

-- SELECT p.patient_id,p.patient_name,p.city from patients p 
SELECT * from appointments a left JOIN patients p on a.patient_id=p.patient_id
where p.city="Hyderabad";

SELECT * FROM patients p, appointments a;

SELECT * from appointments where patient_id= NULL;

SELECT p.patient_id, p.patient_name, a.appointment_id, a.doctor_id, a.appointment_date,
a.status FROM patients p LEFT JOIN appointments a ON p.patient_id = a.patient_id;

SELECT p.patient_id, p.patient_name FROM patients p LEFT JOIN appointments a 
ON p.patient_id = a.patient_id WHERE a.appointment_id IS NULL;

SELECT d.doctor_id, d.doctor_name, a.appointment_id,a.appointment_date, a.status
FROM doctors d LEFT JOIN appointments a ON d.doctor_id = a.doctor_id;

SELECT d.doctor_id, d.doctor_name FROM doctors d LEFT JOIN appointments a ON
d.doctor_id = a.doctor_id WHERE a.appointment_id IS NULL;

SELECT * FROM appointments a LEFT JOIN patients p ON a.patient_id = p.patient_id
WHERE p.patient_id IS NULL;

SELECT * FROM appointments WHERE doctor_id IS NULL;

SELECT p.patient_name AS `Patient Name`, d.doctor_name AS `Doctor Name`,
d.specialization AS `Specialization`,d.consultation_fee AS `Consultation Fee`,
a.status AS `Appointment Status` FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors  d ON a.doctor_id  = d.doctor_id;

SELECT d.doctor_id, d.doctor_name, COUNT(a.appointment_id) AS total_appointments
FROM doctors d LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.doctor_name;

SELECT d.doctor_id, d.doctor_name, COUNT(a.appointment_id) AS total_appointments
FROM doctors d JOIN appointments a ON d.doctor_id = a.doctor_id GROUP BY d.doctor_id, 
d.doctor_name HAVING COUNT(a.appointment_id) > 1;

SELECT d.specialization, SUM(d.consultation_fee) AS total_value
FROM appointments a JOIN doctors d ON a.doctor_id = d.doctor_id WHERE a.status = 'Completed'
GROUP BY d.specialization ORDER BY total_value DESC LIMIT 1;

SELECT p.patient_id, p.patient_name, COUNT(a.appointment_id) AS total_appointments
FROM patients p LEFT JOIN appointments a ON p.patient_id = a.patient_id
GROUP BY p.patient_id, p.patient_name;

SELECT p.patient_id, p.patient_name, COUNT(DISTINCT a.doctor_id) AS doctors_consulted
FROM patients p JOIN appointments a ON p.patient_id = a.patient_id
GROUP BY p.patient_id, p.patient_name HAVING COUNT(DISTINCT a.doctor_id) > 1;

SELECT DISTINCT p.patient_id, p.patient_name FROM patients p
JOIN appointments a ON p.patient_id = a.patient_id
JOIN doctors d ON a.doctor_id  = d.doctor_id WHERE d.specialization = 'Cardiology';

SELECT a.appointment_id, a.appointment_date, a.status,d.doctor_name, d.consultation_fee
FROM appointments a JOIN doctors d ON a.doctor_id = d.doctor_id 
WHERE d.consultation_fee > 900;

SELECT AVG(d.consultation_fee) AS avg_fee FROM appointments a
JOIN doctors d ON a.doctor_id = d.doctor_id WHERE a.status = 'Completed';

SELECT d.doctor_id, d.doctor_name, COUNT(*) AS completed_count FROM doctors d
JOIN appointments a ON d.doctor_id = a.doctor_id WHERE a.status = 'Completed'
GROUP BY d.doctor_id, d.doctor_name HAVING COUNT(*) = (SELECT MAX(cnt)
FROM (SELECT COUNT(*) AS cnt FROM appointments
WHERE status = 'Completed' AND doctor_id IS NOT NULL GROUP BY doctor_id) t);



