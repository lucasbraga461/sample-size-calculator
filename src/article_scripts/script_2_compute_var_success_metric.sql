-- Script 2: Query to compute the variance of the success metric and average over all weeks.
WITH customer_spending AS (
    SELECT
        branch_id,
        FORMAT_DATE('%G-%V', DATE(transaction_timestamp)) AS week_of_year,
        customer_id,
        SUM(transaction_value) AS total_amount_spent_eur
    FROM `project.dataset.credit_transactions`
    WHERE 1=1
        AND transaction_date BETWEEN '2024-05-01' AND '2024-07-31'
        AND branch_id LIKE 'Germany'
    GROUP BY branch_id, week_of_year, customer_id
)
, agg_per_week AS (
    SELECT
        branch_id,
        week_of_year,
        ROUND(AVG(total_amount_spent_eur), 1) AS avg_amount_spent_eur_per_customer,
    FROM customer_spending
    GROUP BY branch_id, week_of_year
)
SELECT
    ROUND(AVG(avg_amount_spent_eur_per_customer),1) AS avg_amount_spent_eur_per_customer_per_week,
    ROUND(VAR_POP(avg_amount_spent_eur_per_customer),1) AS variance_avg_amount_spent_eur_per_customer
FROM agg_per_week
ORDER BY 1,2
;