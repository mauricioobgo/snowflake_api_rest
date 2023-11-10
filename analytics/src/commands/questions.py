
from fastapi import status
from fastapi.responses import JSONResponse
from .base_command import BaseCommannd
from src.db import connect2
from jinja2 import Environment, FileSystemLoader
from snowflake.connector import DictCursor




class QuestionSolution(BaseCommannd):
    def __init__(self,question,year):
        self.question = question
        self.year = year
        print("here")
    def execute(self):
        print("tryint to connect")
        conn = connect2()
        print("connected")
        environment = Environment(loader=FileSystemLoader('src/queries'))
        template = environment.get_template(f'question{self.question}_results.sql')
        content = template.render(
                DATABASE = 'HUMAN_RESOURCES',
                SCHEMA = 'EMPLOYEE_HIRING_DATA',
                TABLE = 'VW_DEPARTMENT_JOB_VAULT',
                YEAR = self.year
        )
        try:
            res = conn.cursor(DictCursor).execute(content)
            return JSONResponse(status_code =status.HTTP_200_OK,content={"Query result":res.fetchall()})
        except:
            conn.close()
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"error":"Not valid Requets"})






        
    
    


    

