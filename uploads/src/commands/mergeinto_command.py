
from fastapi import status
from fastapi.responses import JSONResponse
from .base_command import BaseCommannd
from src.db import connect2
from jinja2 import Environment, FileSystemLoader
from snowflake.connector import DictCursor
import os




class MergeIntoExec(BaseCommannd):
    def __init__(self):
        pass
    def execute(self):
        conn = connect2()
        environment = Environment(loader=FileSystemLoader('src/queries'))
        template = environment.get_template('merge_into_uploadfiles.sql')
        content = template.render(
                DATABASE = os.environ['DATABASE'],
                SCHEMA = os.environ['SCHEMA'],
                SCHEMA2 = os.environ['SCHEMA2'],
                TABLE1 = os.environ['TABLE1'],
                TABLE2 = os.environ['TABLE2'],
                TABLE3 = os.environ['TABLE3']
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





        
    
    


    

