from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class CorporateBase(BaseModel):
    """
    Base schema for the corporate, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the corporate.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
    """
    name: str = Field(..., max_length=100, description="Official name of the corporate.")

class CorporateCreate(CorporateBase):
    """
    Schema used for creating a new corporate.

    Inherits all fields from CorporateBase schema.
    """
    pass

class CorporateUpdate(BaseModel):
    """
    Schema used when updating an existing corporate.

    All fields are optional. Only provided fields will be updated.

    Attributes:
        name (Optional[str]): Updated name of the corporate.
    
    Notes:
        - The name must be 100 characters max.
    """
    name: Optional[str] = Field(None,max_length=100, description="Updated name of the corporate.")


class CorporateRead(CorporateBase):
    """
    Schema used when reading a corporate in the database.

    Inherits all attributes from CorporateBase.

    Attributes:
        id_corporate: Unique identifier of the corporate.
    """
    id_corporate: int

    model_config = ConfigDict(from_attributes=True)