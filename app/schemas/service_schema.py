from pydantic import BaseModel, ConfigDict
from typing import Optional

class ServiceBase(BaseModel):
    name: str
    department_id: int

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    department_id: Optional[int] = None

class ServiceRead(ServiceBase):
    id_service: int

    model_config = ConfigDict(from_attributes=True)
    