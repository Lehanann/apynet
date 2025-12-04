from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class PositionBase(BaseModel):
    """
    Base schema for the position, shared by create, update, read operations and inherited by other schemas.

    Attriubtes:
        name (str): Official name of the position.
        description (str): Description of the position.

    Notes:
        - The name is required.
        - The name must be 100 characters max.
        - The description is required. 
        - For the description,the default value is empty string ''.

    """
    name: str = Field(..., max_length=100, description="The official name of the position.")
    description: str = Field(..., description="The description of the position")

class PositionCreate(PositionBase):
    """
    Schema used for creating a new position.

    Inherits all fields from PositionBase schema.
    """

class PositionUpdate(PositionBase):
    """
    Schema used when updating an existing position.

    All fields inherited from PositionBase become optional.
    Only fields provided in the request will be updated.
    """

    name: Optional[str] = None
    description: Optional[str] = None

class PositionRead(PositionBase):
    """
    Schema used when reading a position on the database.

    Inherits all fields from PositionBase schema.

    Attributes:
        - id_position (int): Unique identifier of the position. 
    """

    id_position: int

    model_config = ConfigDict(from_attributes=True)