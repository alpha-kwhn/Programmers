SELECT A.DR_NAME, A.DR_ID, A.MCDP_CD, DATE_FORMAT(A.HIRE_YMD, '%Y-%m-%d') as HIRE_YMD
FROM DOCTOR A
WHERE A.MCDP_CD = 'CS' OR A.MCDP_CD = 'GS'
ORDER BY A.HIRE_YMD DESC, A.DR_NAME;
