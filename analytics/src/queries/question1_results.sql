    SELECT 
        *
    FROM (
    SELECT 
        ID_H_EP,
        DEPARTMENT_NAME AS DEPARTMENT,
        JOB_NAME AS JOB,
        QUARTER_NAME
    FROM {{DATABASE}}.{{SCHEMA}}.{{TABLE}}
    WHERE EXTRACT('YEAR',DATETIME_H_EP) = {{YEAR}} 
    )
    PIVOT ( COUNT(ID_H_EP) FOR QUARTER_NAME IN ('Q1','Q2','Q3','Q4'))
         AS p 
    ORDER BY DEPARTMENT,
             JOB
    ;