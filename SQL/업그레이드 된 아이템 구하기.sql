WITH TEST AS (
    SELECT A.ITEM_ID
    FROM ITEM_TREE A LEFT OUTER JOIN ITEM_INFO B ON A.PARENT_ITEM_ID = B.ITEM_ID
    WHERE A.PARENT_ITEM_ID IS NOT NULL AND B.RARITY = "RARE"
)

SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (SELECT * FROM TEST)
ORDER BY ITEM_ID DESC
