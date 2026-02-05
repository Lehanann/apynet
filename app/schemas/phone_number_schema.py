from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class PhoneNumberBase(BaseModel):
    """
    Base schema for the phone number, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        internal_phone_number (str): Internal phone number.
        external_phone_number (str): Externe phone number.
        active (bool): Indicates whether the phone number is active.

    Notes:
        - The internal_number is required.
        - The internal_phone_number must be 4 characters max.
        - The external_phone_number must be 15 characters max.
    """

    internal_number: str = Field(...,max_length=4, description="The internal phone number.")
    external_number: Optional[str] = Field(None, max_length=15, description="The external phone number.")
    active: bool = Field(...,description="Indicates whether yhe phone number is active.")

class PhoneNumberCreate(PhoneNumberBase):
    """
    Schema used for creating a new phone number.

    Inherits all fields from PhoneNumberBase schema.
    """
    pass

class PhoneNumberUpdate(PhoneNumberBase):
    """
    Schema used when updating an existing phone number.

    All fields inherited from PhoneNumberBase become optional.
    Only fields provided in the request will be updated.
    """

    internal_number: Optional[str] = None
    external_number: Optional[str] = None
    active: Optional[bool] = None

class PhoneNumberRead(PhoneNumberBase):
    """
    Schema used when reading a phone number in the database.

    Inherits all fields from PhoneNumberBase schema.

    Attributes:
        id_phone (int): Unique identifier of the phone number.
    """

    id_phone: int

    model_config = ConfigDict(from_attributes=True)