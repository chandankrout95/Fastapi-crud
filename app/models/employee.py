from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Employee(BaseModel):
    name: str
    email: str
    password: str
    department: str
    created_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))
    updated_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))


class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    department: Optional[str] = None

