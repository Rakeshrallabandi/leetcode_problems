WITH categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)
SELECT c.category, 
       COUNT(a.account_id) AS accounts_count
FROM categories c
LEFT JOIN Accounts a
    ON (c.category = CASE
                        WHEN a.income < 20000 THEN 'Low Salary'
                        WHEN a.income BETWEEN 20000 AND 50000 THEN 'Average Salary'
                        ELSE 'High Salary'
                      END)
GROUP BY c.category
ORDER BY CASE c.category
            WHEN 'High Salary' THEN 1
            WHEN 'Low Salary' THEN 2
            WHEN 'Average Salary' THEN 3
         END;
