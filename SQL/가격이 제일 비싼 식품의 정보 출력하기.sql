SELECT A.PRODUCT_ID, A.PRODUCT_NAME, A.PRODUCT_CD, A.CATEGORY, A.PRICE
FROM FOOD_PRODUCT A
WHERE A.PRICE = (SELECT MAX(B.PRICE)
                FROM FOOD_PRODUCT B)
