from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class PhoneAssignmentBase(BaseModel):
    """
    Base schema for the phone assignment, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        phone_id (int): Identifier of the parent phone number .
        assigned_id (int): ID of the parent 'employee' or 'service' or 'meeting_room'
        assignment_type (str): Type assignment phone 'employee','service','meeting_room'.

    Notes:
        - The phone_id, assigned_id and assignment_type is required.
    """
    phone_id: int = Field(..., description="Identifier of the parent phone number.")
    assigned_id: int = Field(..., nullable=False, description="Identifier of the parent 'employee' or 'service' or 'meeting_room'.")
    assigned_type: str = Field(..., max_length=30, nullable=False, description="The type assignment phone 'employe', 'service', 'meeting_room'.")

class PhoneAssignmentCreate(PhoneAssignmentBase):
    """
    Schema used for creating a new phone assignment.

    Inherits all fields from PhoneAssignmentBase schema.
    """
    pass

class PhoneAssignmentUpdate(PhoneAssignmentBase):
    """    
    Schema used when updating an existing phone assignment.

    All fields inherited from PhoneAssignmentBase become optional.
    Only fields provided in the request will be updated.

    """
    phone_id: Optional[int] = None
    assigned_id: Optional[int] = None
    assigned_type: Optional[str] = None

class PhoneAssignmentRead(PhoneAssignmentBase):
    """
    Schema used when reading a phone assignment in the database.

    Inherits all attributes from PhoneAssignmentBase.

    Attributes:
        id_assignment: Unique identifier of the phone assignment.
    """
    id_assignment: int

    model_config = ConfigDict(from_attributes=True)

