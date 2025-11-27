from pydantic import BaseModel, ConfigDict
from typing import Optional


class CompanyBase(BaseModel):
    name: str
    corporate_id: int

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    corporate_id: Optional[int] = None

class CompanyRead(CompanyBase):
    id_company: int

    model_config = ConfigDict(from_attributes=True)