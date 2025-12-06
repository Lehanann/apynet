from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class MaterialBase(BaseModel):
    """
    Base schema for the material, shared by create, update, read operations and inherited by other schemas.

    Attriubtes:
        name (str): Official name of the material.
        type (str): Official type of the material.
        description (Optional[str]): Description of the material.

    Notes:
        - The name and type are required.
        - The name must be 100 characters max.
        - The type must be 50 characters max.
    """    
    name: str = Field(..., max_length=100, description="Official name of the material.")
    type: str = Field(..., max_length=50, description="Official type of the material.")
    description: str = Field(None, description="Description of the material.")

class MaterialCreate(MaterialBase):
    """
    Schema used for creating a new material.

    Inherits all fields from MaterialBase schema.
    """
    pass

class MaterialUpdate(MaterialBase):
    """
    Schema used when updating an existing material.

    All fields inherited from PositionBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None

class MaterialRead(MaterialBase):
    """
    Schema used when reading a material on the database.

    Inherits all fields from PositionBase schema.

    Attributes:
        - id_material (int): Unique identifier of the material. 
    """
    id_material: int

    model_config = ConfigDict(from_attributes=True)