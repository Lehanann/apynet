from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class MeetingRoomBase(BaseModel):
    """
    Base schema for the meeting room, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the meeting room.
        address (str): Address of the meeting room
        corporate_id (int): ID of the parent corporate.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
        - The corporate_id is required and refers to the parent corporate.
    """
    name: str = Field(..., max_length=100, description="Official name of the meeting room.")
    site_id: int = Field(...,  description="ID of the parent site.")

class MeetingRoomCreate(MeetingRoomBase):
    """
    Schema used when creating a new meeting room.

    Inherits all fields from MeetingRoomBase schema.
    """
    pass

class MeetingRoomUpdate(MeetingRoomBase):
    """
    Schema used when updating an existing meeting room.

    All fields inherited from MeetingRoomBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    site_id: Optional[int] = None

class MeetingRoomRead(MeetingRoomBase):
    """
    Schema used when reading a meeting room from the database.

    Inherits all fields from MeetingRoomBase schema.

    Attributes:
        id_meeting room (int): Unique identifier of the meeting room.
    """
    id_meeting_room: int

    model_config = ConfigDict(from_attributes=True)