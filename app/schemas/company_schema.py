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

class CompanyUpdate(CompanyBase):
    """
    Schema used when updating an existing company.

    All fields inherited from CompanyBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    corporate_id: Optional[int] = None

class CompanyRead(CompanyBase):
    """
    Schema used when reading a company from the database.

    Inherits all fields from CompanyBase schema.

    Attributes:
        id_company (int): Unique identifier of the company.
    """
    id_company: int

    model_config = ConfigDict(from_attributes=True)