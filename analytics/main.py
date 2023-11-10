from fastapi import FastAPI, Request,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.blueprints.endpoints import router as endpoints

app = FastAPI()
app.include_router(endpoints)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=""
    )