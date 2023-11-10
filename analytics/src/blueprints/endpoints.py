from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from src.commands.questions import QuestionSolution
from src.commands.ping_command import Ping

from typing import Annotated
from fastapi import APIRouter, Header

router = APIRouter()
baseUrl = "/analytics"

@router.get("/who")
async def who():
    return baseUrl

@router.get(baseUrl+"/ping", response_class=PlainTextResponse)
async def ping():
    result = Ping().execute()
    return result


@router.get(baseUrl+"/jobDepartment/{year}",response_class=PlainTextResponse)
async def job_by_department(year:str, question:int = 1 ):
    result = QuestionSolution(question,year).execute()
    return  result

@router.get(baseUrl+"/DepartmentHired/{year}",response_class=PlainTextResponse)
async def department_hired(year: str, question:int = 2 ):
    result = QuestionSolution(question,year).execute()
    return  result


