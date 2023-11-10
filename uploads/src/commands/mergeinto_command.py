
from fastapi import status
from fastapi.responses import JSONResponse
from .base_command import BaseCommannd
from src.db import connect2
from jinja2 import Environment, FileSystemLoader
from snowflake.connector import DictCursor




class MergeIntoExec(BaseCommannd):
    def __init__(self):
        pass
    def execute(self):
        conn = connect2()
        environment = Environment(loader=FileSystemLoader('src/queries'))
        template = environment.get_template('merge_into_uploadfiles.sql')
        content = template.render(
                DATABASE = 'HUMAN_RESOURCES',
                SCHEMA = 'EMPLOYEE_HIRING_DATA',
                SCHEMA2 = 'PUBLIC',
                TABLE1 = 'TBL_HIRED_EMPLOYEES',
                TABLE2 = 'TBL_DEPARTMENTS',
                TABLE3 = 'TBL_JOBS'
        )
        content = f"""
            execute immediate $$  
            begin  
                {content} 
            end; 
            $$"""
        try:
            res = conn.cursor(DictCursor).execute(content)
            if res.fetchall():
                return JSONResponse(status_code =status.HTTP_200_OK,content={"results":"Merge succeeded"})
            else:
                return JSONResponse(status_code =status.HTTP_200_OK,content={"results":"No new rows inserted"})
        except:
            conn.close()
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"error":"Not valid Requets"})





        
    
    


    

