from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class ServiceBase(BaseModel):
    """
    Base schema for the service, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the service.
        department_id (int): ID of the parent department.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
        - The department_id is required and refers to the parent department.
    """
    name: str = Field(..., max_length=100, description="Official name of the service.")
    department_id: int = Field(..., description="ID of the parent department.")

class ServiceCreate(ServiceBase):
    """
    Schema used for creating a new service.

    Inherits all fields from ServiceBase schema.
    """
    pass

class ServiceUpdate(ServiceBase):
    """
    Schema used when updating an existing service.

    All fields inherited from ServiceBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    department_id: Optional[int] = None

class ServiceRead(ServiceBase):
    """
    Schema used when reading a service in the database.

    Inherits all fields from ServiceBase schema.

    Attributes:
        id_service (int): Unique identifier of the service.
    """
    id_service: int

    model_config = ConfigDict(from_attributes=True)
    