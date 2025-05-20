-- Script 3: Query to calculate the average weekly volume of distinct customers.
WITH customer_volume AS (
SELECT
    branch_id,
    FORMAT_DATE('%G-%V', DATE(transaction_timestamp)) AS week_of_year,
    COUNT(DISTINCT customer_id) AS cntd_customers
FROM `project.dataset.credit_transactions`
WHERE 1=1
    AND transaction_date BETWEEN '2024-05-01' AND '2024-07-31'
    AND branch_id LIKE 'Germany'
GROUP BY branch_id, week_of_year
)
SELECT
    ROUND(AVG(cntd_customers),1) AS avg_cntd_customers
FROM customer_volume
;