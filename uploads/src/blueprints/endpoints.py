from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from src.commands.mergeinto_command import MergeIntoExec
from src.commands.ping_command import Ping

from typing import Annotated
from fastapi import APIRouter, Header

router = APIRouter()
baseUrl = "/uploadFiles"

@router.get("/who")
async def who():
    return baseUrl

@router.get(baseUrl+"/ping", response_class=PlainTextResponse)
async def ping():
    result = Ping().execute()
    return result


@router.post(baseUrl+"/mergeinto")
async def merge_into():
    result = MergeIntoExec().execute()
    return  result


