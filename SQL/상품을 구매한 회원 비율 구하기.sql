SELECT 
YEAR(A.SALES_DATE) AS YEAR, 
MONTH(A.SALES_DATE) AS MONTH, 
COUNT(DISTINCT(A.USER_ID)) AS PUCHASED_USERS, 
ROUND(COUNT(DISTINCT(A.USER_ID)) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED)='2021'), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE A
WHERE A.USER_ID IN (SELECT USER_ID
                   FROM USER_INFO
                   WHERE YEAR(JOINED) = 2021)
GROUP BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE)
ORDER BY YEAR, MONTH;
