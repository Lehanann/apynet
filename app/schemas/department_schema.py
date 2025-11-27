from pydantic import BaseModel, ConfigDict
from typing import Optional

class DepartmentBase(BaseModel):
    name: str
    company_id: int

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    company_id: Optional[int] = None

class DepartmentRead(DepartmentBase):
    id_department: int

    model_config = ConfigDict(from_attributes=True)