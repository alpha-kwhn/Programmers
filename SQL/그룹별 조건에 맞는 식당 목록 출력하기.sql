SELECT A.MEMBER_NAME, B.REVIEW_TEXT, DATE_FORMAT(B.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM MEMBER_PROFILE A INNER JOIN REST_REVIEW B ON A.MEMBER_ID = B.MEMBER_ID 
WHERE B.MEMBER_ID IN (SELECT C.MEMBER_ID 
                      FROM REST_REVIEW C
                      GROUP BY C.MEMBER_ID 
                      HAVING COUNT(*) = (
                          SELECT MAX(CNT) 
                          FROM (SELECT COUNT(*) AS CNT
                                  FROM REST_REVIEW
                                  GROUP BY MEMBER_ID) D
                      )) -- 인라인 서브쿼리를 활용해 여러 개의 값을 불러오고 IN 으로 값이 속하는지 체크하도록 함
ORDER BY REVIEW_DATE, B.REVIEW_TEXT;
