from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class DepartmentBase(BaseModel):
    """
    Base schema for the department, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the department.
        company_id (int): ID of the parent company.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
        - The company_id is required and refers to the parent company.
    """
    name: str = Field(..., max_length=100, description="Official name of the department.")
    company_id: int = Field(..., description="ID of the parent company.")

class DepartmentCreate(DepartmentBase):
    """
    Schema used for creating a new department.

    Inherits all fields from DepartmentBase schema.
    """
    pass

class DepartmentUpdate(DepartmentBase):
    """
    Schema used when updating an existing department.

    All fields inherited from DepartmentBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    company_id: Optional[int] = None

class DepartmentRead(DepartmentBase):
    """
    Schema used when reading a department in the database.

    Inherits all fields from DepartmentBase schema.

    Attributes:
        id_department (int): Unique identifier of the department.
    """
    id_department: int

    model_config = ConfigDict(from_attributes=True)