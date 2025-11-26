from datetime import datetime

from pydantic import BaseModel, ConfigDict
from typing import Optional


class CorporateBase(BaseModel):
    """
    Docstring for CorporateBase
    Default schema for corporate
    """
    name: str

class CorporateCreate(CorporateBase):
    """
    Docstring for CorporateCreate
    """
    pass

class CorporateUpdate(BaseModel):
    """
    Docstring for CorporateUpdate
    """
    name: Optional[str]=None


class CorporateRead(CorporateBase):
    """
    Docstring for CorporateRead
    """
    id_corporate: int

    model_config=ConfigDict(from_attributes=True)