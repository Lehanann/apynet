from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class CompanyBase(BaseModel):
    """
    Base schema for the company, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the company.
        corporate_id (int): ID of the parent corporate.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
        - The corporate_id is required and refers to the parent corporate.
    """
    name: str = Field(..., max_length=100, description="Official name of the company.")
    corporate_id: int = Field(...,  description="ID of the parent corporate.")

class CompanyCreate(CompanyBase):
    """
    Schema used when creating a new company.

    Inherits all fields from CompanyBase schema.
    """
    pass

class CompanyUpdate(BaseModel):
    """
    Schema used when updating an existing company.

    All fields are optional. Only provided fields will be updated.

    Attributes:
        name (Optional[str]): Updated name of the company.
        corporate_id (Optional[int]): Updated parent corporate ID.

    Notes:
    - The name, if provided, must be a string with a maximum length of 100 characters.
    - The corporate_id, if provided, should refer to the updated parent corporate.
    """
    name: Optional[str] = Field(None, max_length=100, description="Updated name of the company.")
    corporate_id: Optional[int] = Field(None, description="Updated parent corporate ID.")

class CompanyRead(CompanyBase):
    """
    Schema used when reading a company from the database.

    Inherits all fields from CompanyBase schema.

    Attributes:
        id_company (int): Unique identifier of the company.
    """
    id_company: int

    model_config = ConfigDict(from_attributes=True)