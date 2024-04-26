SELECT 
    ID, 
    CASE 
        WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
        WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH'
        ELSE 'MEDIUM'
    END AS SIZE
FROM ECOLI_DATA;

-- CASE
--  WHEN 조건식 THEN 값
--  WHEN 조건식 THEN 값
-- END AS 컬럼명 
