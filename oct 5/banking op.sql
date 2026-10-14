-- Q1
-- CALL GetAllAccounts();

-- Q2
-- DELIMITER //
-- CREATE PROCEDURE GetSavingsAccounts()
-- BEGIN
--     SELECT *
--     FROM accounts
--     WHERE account_type = 'Savings';
-- END //
-- DELIMITER ;

-- CALL GetSavingsAccounts();

-- Q3
-- DELIMITER //

-- CREATE PROCEDURE GetAccountsByCity(IN p_city VARCHAR(50))
-- BEGIN
--     SELECT *
--     FROM accounts
--     WHERE city = p_city;
-- END //

-- DELIMITER ;

-- CALL GetAccountsByCity('Hyderabad')


-- Q4
-- DELIMITER //

-- CREATE PROCEDURE GetAccountsAboveBalance(IN p_balance DECIMAL(10,2))
-- BEGIN
--     SELECT *
--     FROM accounts
--     WHERE balance > p_balance;
-- END //

-- DELIMITER ;

-- CALL GetAccountsAboveBalance(45000);


-- Q5
-- DELIMITER //

-- CREATE PROCEDURE UpdateAccountBalance(
--     IN p_account_id INT,
--     IN p_new_balance DECIMAL(10,2)
-- )
-- BEGIN
--     UPDATE accounts
--     SET balance = p_new_balance
--     WHERE account_id = p_account_id;
-- END //

-- DELIMITER ;

-- CALL UpdateAccountBalance(101, 60000);

-- CALL GetAllAccounts();

-- Q6

-- DELIMITER //

-- CREATE PROCEDURE DepositAmount(
--     IN p_account_id INT,
--     IN p_deposit DECIMAL(10,2)
-- )
-- BEGIN
--     UPDATE accounts
--     SET balance = balance + p_deposit
--     WHERE account_id = p_account_id;
-- END //
-- DELIMITER ;

-- CALL DepositAmount(101, 5000);
-- CALL GetAllAccounts();

-- Q7
-- DELIMITER //

-- CREATE PROCEDURE WithdrawAmount(
--     IN p_account_id INT,
--     IN p_withdrawal DECIMAL(10,2)
-- )
-- BEGIN
--     UPDATE accounts
--     SET balance = balance - p_withdrawal
--     WHERE account_id = p_account_id;
-- END //

-- DELIMITER ;

-- CALL WithdrawAmount(101, 2000);
CALL GetAllAccounts();


