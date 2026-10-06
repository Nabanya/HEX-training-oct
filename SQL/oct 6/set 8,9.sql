CREATE TABLE insurance_claims (
claim_id INT PRIMARY KEY,
customer_name VARCHAR(100),
insurance_type VARCHAR(50),
claim_amount DECIMAL(12,2),
branch VARCHAR(50)
);
INSERT INTO insurance_claims VALUES
(1, 'Ajay Kumar', 'Health', 75000, 'Hyderabad'),
(2, 'Meena Shah', 'Motor', 45000, 'Mumbai'),
(3, 'Rohit Jain', 'Health', 125000, 'Hyderabad'),

(4, 'Sara Ali', 'Travel', 30000, 'Delhi'),
(5, 'Vikas Rao', 'Motor', 85000, 'Mumbai'),
(6, 'Nisha Singh', 'Health', 60000, 'Delhi'),
(7, 'Imran Khan', 'Travel', 55000, 'Hyderabad'),
(8, 'Pooja Patel', 'Motor', 40000, 'Delhi'),
(9, 'Karan Mehta', 'Health', 150000, 'Mumbai'),
(10, 'Farah Ahmed', 'Travel', 35000, 'Hyderabad');

WITH claim_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claim
    FROM insurance_claims GROUP BY insurance_type
)
SELECT * FROM claim_total;

WITH branch_total AS (
    SELECT branch, SUM(claim_amount) AS total_claim
    FROM insurance_claims
    GROUP BY branch
)
SELECT * FROM branch_total;

WITH claim_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claim
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT * FROM claim_total WHERE total_claim > 200000;

WITH avg_claim AS (
    SELECT AVG(claim_amount) AS average_amount FROM insurance_claims
)
SELECT * FROM insurance_claims WHERE claim_amount > (SELECT average_amount FROM avg_claim);

WITH claim_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claim
    FROM insurance_claims GROUP BY insurance_type
)
SELECT *,RANK() OVER(ORDER BY total_claim DESC) AS claim_rank FROM claim_total;

WITH type_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claim
    FROM insurance_claims
    GROUP BY insurance_type
),
branch_total AS (
    SELECT branch, SUM(claim_amount) AS total_claim
    FROM insurance_claims
    GROUP BY branch
)
SELECT * FROM type_total;

SELECT * FROM branch_total;

-- correlated subquery

SELECT *
FROM insurance_claims c
WHERE claim_amount > (
SELECT AVG(c2.claim_amount)FROM insurance_claims c2 WHERE c2.insurance_type = c.insurance_type);

SELECT *
FROM insurance_claims c
WHERE claim_amount > (
SELECT AVG(c2.claim_amount)FROM insurance_claims c2 WHERE c2.branch = c.branch);

SELECT *
FROM insurance_claims c
WHERE claim_amount = (SELECT MAX(c2.claim_amount)
FROM insurance_claims c2 WHERE c2.insurance_type = c.insurance_type
);

SELECT customer_name, claim_amount, branchFROM insurance_claims c
WHERE claim_amount > (
SELECT AVG(c2.claim_amount) FROM insurance_claims c2 WHERE c2.branch = c.branch
);

-- set 9

CREATE TABLE staff_hierarchy (
employee_id INT PRIMARY KEY,
employee_name VARCHAR(100),
manager_id INT,
designation VARCHAR(100)
);
INSERT INTO staff_hierarchy VALUES
(1, 'Raj Malhotra', NULL, 'CEO'),
(2, 'Meera Shah', 1, 'CTO'),
(3, 'Vikram Rao', 1, 'Sales Director'),

(4, 'Aman Khan', 2, 'Engineering Manager'),
(5, 'Sara Ali', 2, 'Data Manager'),
(6, 'Rohit Das', 4, 'Developer'),
(7, 'Priya Singh', 4, 'Developer'),
(8, 'Kabir Ahmed', 5, 'Data Engineer'),
(9, 'Neha Rao', 5, 'Data Analyst'),
(10, 'Imran Sheikh', 3, 'Sales Manager'),
(11, 'Pooja Jain', 10, 'Sales Executive');

select * from staff_hierarchy;

SELECT * FROM staff_hierarchy WHERE manager_id IS NULL;

SELECT * FROM staff_hierarchy WHERE manager_id = 1;

SELECT * FROM staff_hierarchy WHERE manager_id = 2;

WITH RECURSIVE hierarchy AS (
    SELECT employee_id, employee_name, manager_id, designation
    FROM staff_hierarchy
    WHERE manager_id IS NULL

    UNION ALL

    SELECT s.employee_id, s.employee_name, s.manager_id, s.designation
    FROM staff_hierarchy s
    JOIN hierarchy h
    ON s.manager_id = h.employee_id
)
SELECT *
FROM hierarchy;

WITH RECURSIVE hierarchy AS (
    SELECT employee_id, employee_name, manager_id, designation, 1 AS level
    FROM staff_hierarchy
    WHERE manager_id IS NULL

    UNION ALL

    SELECT s.employee_id, s.employee_name, s.manager_id,
           s.designation, h.level + 1
    FROM staff_hierarchy s
    JOIN hierarchy h
    ON s.manager_id = h.employee_id
)
SELECT *
FROM hierarchy;

WITH RECURSIVE hierarchy AS (
    SELECT employee_id, employee_name, manager_id
    FROM staff_hierarchy
    WHERE employee_id = 2

    UNION ALL

    SELECT s.employee_id, s.employee_name, s.manager_id
    FROM staff_hierarchy s
    JOIN hierarchy h
    ON s.manager_id = h.employee_id
)
SELECT *
FROM hierarchy
WHERE employee_id <> 2;

WITH RECURSIVE hierarchy AS (
    SELECT employee_id, employee_name, manager_id
    FROM staff_hierarchy
    WHERE employee_id = 4

    UNION ALL

    SELECT s.employee_id, s.employee_name, s.manager_id
    FROM staff_hierarchy s
    JOIN hierarchy h
    ON s.manager_id = h.employee_id
)
SELECT *
FROM hierarchy
WHERE employee_id <> 4;

SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m
ON e.manager_id = m.employee_id;

WITH RECURSIVE hierarchy AS (
    SELECT employee_id, manager_id, 1 AS level
    FROM staff_hierarchy
    WHERE manager_id IS NULL
    UNION ALL
    SELECT s.employee_id, s.manager_id, h.level + 1
    FROM staff_hierarchy s
    JOIN hierarchy h
    ON s.manager_id = h.employee_id
)
SELECT level, COUNT(*) AS total_employees
FROM hierarchy
GROUP BY level;

WITH RECURSIVE hierarchy AS (
SELECT employee_id, employee_name, manager_id, designation, 1 AS level
FROM staff_hierarchy WHERE manager_id IS NULL
UNION ALL
SELECT s.employee_id, s.employee_name, s.manager_id,s.designation, h.level + 1
FROM staff_hierarchy s JOIN hierarchy h ON s.manager_id = h.employee_id )
SELECT * FROM hierarchy ORDER BY level, employee_id;