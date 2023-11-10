from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel , Field 
from typing import Optional

class HiredEmployees(BaseModel):
    id_h_ep: int | None = None
    name_h_ep: Optional[str] = Field(None, max_length=500)
    datetime_h_ep: datetime | None = None
    department_id: int | None = None
    job_id: int

class Departments(BaseModel):
    id_d: int | None = None
    department_name: Optional[str] = Field(None, max_length=200)

class Jobs(BaseModel):
    id_j: int | None = None
    job_name: Optional[str] = Field(None, max_length=200)
