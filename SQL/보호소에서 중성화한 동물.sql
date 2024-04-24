SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_OUTS A
WHERE A.SEX_UPON_OUTCOME NOT LIKE 'Intact%' AND A.ANIMAL_ID IN (SELECT ANIMAL_ID
                                                             FROM ANIMAL_INS B
                                                             WHERE B.SEX_UPON_INTAKE LIKE 'Intact%')
ORDER BY A.ANIMAL_ID
