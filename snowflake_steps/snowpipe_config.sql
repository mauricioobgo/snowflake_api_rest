
--arn:aws:iam::738200422943:role/snowflake_role

CREATE OR REPLACE STORAGE INTEGRATION S3_role_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = "srn of role"
  STORAGE_ALLOWED_LOCATIONS = ("s3://<bucket>");



desc integration S3_role_integration;

create or replace stage HUMAN_RESOURCES.public.S3_stage
  url = ('s3://<bucket>')
  storage_integration = S3_role_integration;
  

CREATE OR REPLACE TABLE HUMAN_RESOURCES.PUBLIC.TBL_HIRED_EMPLOYEES_RAW(
    ID_H_EP INTEGER,
    NAME_H_EP VARCHAR(500),
    DATETIME_H_EP TIMESTAMP,
    DEPARTMENT_ID INTEGER,
    JOB_ID INTEGER,
    ETL_DATETIME TIMESTAMP 

);
CREATE OR REPLACE TABLE HUMAN_RESOURCES.PUBLIC.TBL_DEPARTMENTS_RAW(
    ID_D INTEGER,
    DEPARTMENT_NAME VARCHAR(200),
    ETL_DATETIME TIMESTAMP 
);

CREATE OR REPLACE TABLE HUMAN_RESOURCES.PUBLIC.TBL_JOBS_RAW(
    ID_J INTEGER,
    JOB_NAME VARCHAR(200),
    ETL_DATETIME TIMESTAMP 
);



  create or replace pipe HUMAN_RESOURCES.public.HiredEmployees_pipe 
  auto_ingest=TRUE as
  copy into HUMAN_RESOURCES.PUBLIC.TBL_HIRED_EMPLOYEES_RAW
  from (
  SELECT
      t.$1::INTEGER,
      t.$2::STRING,
      TO_TIMESTAMP(t.$3::STRING, 'YYYY-MM-DDTHH24:MI:SSZ'),
      t.$4::INTEGER,
      t.$5::INTEGER,
      CURRENT_TIMESTAMP()
  FROM @HUMAN_RESOURCES.public.S3_stage t
  )
  PATTERN = '.*hired_employees.*'
  FILE_FORMAT = (type = 'CSV' ,
  FIELD_OPTIONALLY_ENCLOSED_BY='"',
  FIELD_DELIMITER = ',',
  SKIP_BLANK_LINES=true);

  create or replace pipe HUMAN_RESOURCES.public.Departments_pipe 
  auto_ingest=TRUE as
  copy into HUMAN_RESOURCES.PUBLIC.TBL_DEPARTMENTS_RAW
  from (
  SELECT
      t.$1::INTEGER,
      t.$2::STRING,
      CURRENT_TIMESTAMP()
  FROM @HUMAN_RESOURCES.public.S3_stage t
  )
  PATTERN = '.*departments.*'
  FILE_FORMAT = (type = 'CSV' ,
  FIELD_OPTIONALLY_ENCLOSED_BY='"',
  FIELD_DELIMITER = ',',
  SKIP_BLANK_LINES=true);

  
  create or replace pipe HUMAN_RESOURCES.public.Jobs_pipe 
  auto_ingest=TRUE as
  copy into HUMAN_RESOURCES.PUBLIC.TBL_JOBS_RAW
  from (
  SELECT
      t.$1::INTEGER,
      t.$2::STRING,
      CURRENT_TIMESTAMP()
  FROM @HUMAN_RESOURCES.public.S3_stage t
  )
  PATTERN = '.*jobs.*'
  FILE_FORMAT = (type = 'CSV' ,
  FIELD_OPTIONALLY_ENCLOSED_BY='"',
  FIELD_DELIMITER = ',',
  SKIP_BLANK_LINES=true);


show pipes;

select SYSTEM$PIPE_STATUS('HUMAN_RESOURCES.public.HiredEmployees_pipe');

ALTER PIPE HUMAN_RESOURCES.public.HiredEmployees_pipe REFRESH;


-- Grant Object Access and Insert Permission
grant usage on database HUMAN_RESOURCES to role DATA_API_ROLE;
grant usage on schema HUMAN_RESOURCES.public to role DATA_API_ROLE;
grant usage on schema HUMAN_RESOURCES.EMPLOYEE_HIRING_DATA to role DATA_API_ROLE;

grant insert, select on HUMAN_RESOURCES.EMPLOYEE_HIRING_DATA.TBL_HIRED_EMPLOYEES to role DATA_API_ROLE;
grant insert, select on HUMAN_RESOURCES.EMPLOYEE_HIRING_DATA.TBL_JOBS to role DATA_API_ROLE;
grant insert, select on HUMAN_RESOURCES.EMPLOYEE_HIRING_DATA.TBL_DEPARTMENTS to role DATA_API_ROLE;


grant insert, select,truncate on HUMAN_RESOURCES.public.TBL_JOBS_RAW to role DATA_API_ROLE;
grant insert, select,truncate on HUMAN_RESOURCES.public.TBL_HIRED_EMPLOYEES_RAW to role DATA_API_ROLE;
grant insert, select,truncate on HUMAN_RESOURCES.public.TBL_DEPARTMENTS_RAW to role DATA_API_ROLE;

grant insert, select on HUMAN_RESOURCES.EMPLOYEE_HIRING_DATA.VW_DEPARTMENT_JOB_VAULT to role DATA_API_ROLE;



grant usage on stage HUMAN_RESOURCES.public.S3_stage to role DATA_API_ROLE;

-- Bestow S3_pipe Ownership
grant ownership on pipe HUMAN_RESOURCES.public.HiredEmployees_pipe to role DATA_API_ROLE;
grant ownership on pipe HUMAN_RESOURCES.public.Departments_pipe to role DATA_API_ROLE;
grant ownership on pipe HUMAN_RESOURCES.public.Jobs_pipe to role DATA_API_ROLE;
grant ownership on pipe HUMAN_RESOURCES.public.HiredEmployees_pipe to role accountadmin;

-- Grant S3_role and Set as Default
grant role S3_role to user <username>;
alter user <username> set default_role = S3_role;

ALTER PIPE HUMAN_RESOURCES.PUBLIC.HIREDEMPLOYEES_PIPE SET PIPE_EXECUTION_PAUSED=false;

SELECT *
FROM HUMAN_RESOURCES.PUBLIC.TBL_HIRED_EMPLOYEES_RAW ;

select *
from table(HUMAN_RESOURCES.information_schema.copy_history(TABLE_NAME=>'HUMAN_RESOURCES.PUBLIC.TBL_HIRED_EMPLOYEES_RAW', START_TIME=> DATEADD(hours, -1, CURRENT_TIMESTAMP())));
  