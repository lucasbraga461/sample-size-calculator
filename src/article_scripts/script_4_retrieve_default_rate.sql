-- Script 4: Query to retrieve default rate per week.
SELECT
    branch_id,
    date_trunc(transaction_date, week) AS week_of_order,
    SUM(transaction_value) AS sum_disbursed_gmv,
    SUM(CASE WHEN is_completed THEN transaction_value ELSE 0 END) AS sum_collected_gmv,
    1-(SUM(CASE WHEN is_completed THEN transaction_value ELSE 0 END)/SUM(transaction_value)) AS default_rate,
FROM `project.dataset.credit_transactions`
WHERE transaction_date BETWEEN '2024-02-01' AND '2024-04-30'
    AND branch_id = 'Germany'
GROUP BY 1,2
ORDER BY 1,2
;