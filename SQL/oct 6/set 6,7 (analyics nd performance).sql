CREATE TABLE call_performance (
call_id INT PRIMARY KEY,
agent_name VARCHAR(100),
team VARCHAR(50),
calls_handled INT,
customer_rating DECIMAL(3,2),
performance_date DATE
);
INSERT INTO call_performance VALUES
(1, 'Aman', 'Alpha', 42, 4.50, '2026-09-01'),
(2, 'Sara', 'Alpha', 38, 4.70, '2026-09-01'),
(3, 'Ravi', 'Beta', 50, 4.20, '2026-09-01'),
(4, 'Neha', 'Beta', 45, 4.80, '2026-09-01'),
(5, 'Aman', 'Alpha', 48, 4.60, '2026-09-02'),
(6, 'Sara', 'Alpha', 44, 4.50, '2026-09-02'),
(7, 'Ravi', 'Beta', 46, 4.30, '2026-09-02'),
(8, 'Neha', 'Beta', 52, 4.90, '2026-09-02'),
(9, 'Kabir', 'Alpha', 41, 4.40, '2026-09-01'),
(10, 'Kabir', 'Alpha', 49, 4.60, '2026-09-02'),
(11, 'Pooja', 'Beta', 45, 4.70, '2026-09-01'),
(12, 'Pooja', 'Beta', 50, 4.80, '2026-09-02');

SELECT *,SUM(calls_handled) OVER() AS total_calls FROM call_performance;

SELECT *,SUM(calls_handled) OVER(PARTITION BY team) AS team_total_calls FROM call_performance;

SELECT *,AVG(calls_handled) OVER(PARTITION BY team) AS team_avg_calls FROM call_performance;

SELECT *,AVG(customer_rating) OVER(PARTITION BY team) AS team_avg_rating FROM call_performance;

SELECT *,SUM(calls_handled) OVER(PARTITION BY agent_name ORDER BY performance_date) AS cumulative_calls FROM call_performance;

SELECT *,SUM(calls_handled) OVER( PARTITION BY team
ORDER BY performance_date) AS cumulative_team_calls FROM call_performance;

SELECT *, calls_handled -AVG(calls_handled) OVER(PARTITION BY team) AS difference FROM call_performance;

SELECT *,LAG(calls_handled) OVER(PARTITION BY agent_name
ORDER BY performance_date ) AS previous_calls FROM call_performance;

SELECT *,calls_handled - LAG(calls_handled) OVER(PARTITION BY agent_name
ORDER BY performance_date) AS call_difference FROM call_performance;

SELECT *,SUM(calls_handled) OVER(PARTITION BY agent_name) AS total_agent_calls FROM call_performance;

-- set 7

SELECT *,RANK() OVER(ORDER BY calls_handled DESC) AS call_rankFROM call_performance;

SELECT *,ROW_NUMBER() OVER(ORDER BY calls_handled DESC) AS row_num FROM call_performance;

SELECT *, RANK() OVER(ORDER BY calls_handled DESC) AS ranking FROM call_performance;

SELECT *, DENSE_RANK() OVER(ORDER BY calls_handled DESC) AS dense_ranking FROM call_performance;

SELECT *,ROW_NUMBER() OVER(ORDER BY calls_handled DESC) AS row_num,
RANK() OVER(ORDER BY calls_handled DESC) AS rank_num,
DENSE_RANK() OVER(ORDER BY calls_handled DESC) AS dense_rank_num
FROM call_performance;

SELECT *,RANK() OVER(
PARTITION BY team ORDER BY calls_handled DESC) AS team_rank
FROM call_performance;

SELECT *, RANK() OVER(ORDER BY customer_rating DESC) AS rating_rank FROM call_performance;

SELECT *FROM (
    SELECT *,RANK() OVER(PARTITION BY team
    ORDER BY calls_handled DESC) AS rnk
    FROM call_performance
) x WHERE rnk <= 3;

SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY agent_name
    ORDER BY calls_handled DESC) AS rn
    FROM call_performance
) x
WHERE rn = 1;

SELECT agent_name,SUM(calls_handled) AS total_calls,
RANK() OVER(ORDER BY SUM(calls_handled) DESC) AS agent_rank
FROM call_performance GROUP BY agent_name;


