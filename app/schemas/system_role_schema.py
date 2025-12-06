from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class SystemRoleBase(BaseModel):
    """
    Base schema for the SystemRole, shared by create, update, read operations and inherited by other schemas.

    Attriubtes:
        name (str): Official name of the system role.
        description (Optional[str]): Description of the system role.
        permission_level (int): Permission level of the system role.

    Notes:
        - The name and permission level are required.
        - The name must be 50 characters max.
    """

    name: str = Field(..., max_length=50, description="The name of the system role.")
    description: Optional[str] = Field(None, description="Description of the system role.")
    permission_level: int = Field(1, description="Permission level of the system role.")

class SystemRoleCreate(SystemRoleBase):
    """
    Schema used for creating a new system role.

    Inherits all fields from SystemRoleBase schema.
    """
    pass

class SystemRoleUpdate(SystemRoleBase):
    """
    Schema used when updating an existing system role.

    All fields inherited from SystemRoleBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    permission_level: Optional[int] = None

class SystemRoleRead(SystemRoleBase):
    """
    Schema used when reading a system role on the database.

    Inherits all fields from SystemRoleBase schema.

    Attributes:
        - id_system_role (int): Unique identifier of the system role. 
    """

    id_system_role: int

    model_config = ConfigDict(from_attributes=True)