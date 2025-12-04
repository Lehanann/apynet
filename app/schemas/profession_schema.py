from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Any



class ProfessionBase(BaseModel):
    """
    Base schema for the profession, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the profession.
        default_account_allowed (bool) : Indicates whether the profession requires an account.
        default_material_allowed (bool) : Indicates whether the profession requires materials.
        default_material (dict[str, Any]) : Contains a list of materials required by the profession.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
        - Default value for account allowed is False..
        - Default value for material allowed is False.
        - By default, materials are empty; this is managed by the database.
    """
    name: str = Field(..., max_length=100, description="Official name of the profession.")
    default_account_allowed: bool = Field(..., description="Allow or deny an account for the profession.")
    default_material_allowed: bool = Field(..., description="Allow or deny material for the profession.")
    default_material: dict[str, Any] = Field(..., description="Material by default, for the profession.")

class ProfessionCreate(ProfessionBase):
    """
    Schema used for creating a new profession.

    Inherits all fields from ProfessionBase schema.
    """
    pass

class ProfessionUpdate(ProfessionBase):
    """
    Schema used when updating an existing profession.

    All fields inherited from ProfessionBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    default_account_allowed: Optional[bool] = None
    default_material_allowed: Optional[bool] = None
    default_material: Optional[dict[str, Any]] = None

class ProfessionRead(ProfessionBase):
    """
    Schema used when reading a profession in the database.

    Inherits all fields from ProfessionBase schema.

    Attributes:
        id_profession (int): Unique identifier of the profession.
    """
    id_profession: int

    model_config = ConfigDict(from_attributes=True)