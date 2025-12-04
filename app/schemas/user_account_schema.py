from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class UserAccountBase(BaseModel):
    """
    Base schema for the user account shared by create, update and read operations and inherited by other schemas.

     Attributes:
        username (str): Username associated with the employee.
        password (str): Password of the user account.
        work_email (str): Professional email of the user account.
        employee_id (int): ID of the associated employee.

    Notes:
        - username, password, work_email and employee_id are required.
        - username must be 50 characters max.
        - password must be 255 characters max.
        - work_email must be 100 characters max.
        - Uniqueness for username, work_email and employee_id
          is enforced at the database level, not by this schema.
    """

    username: str = Field(..., max_length=50, description="Username associated with the employee.")
    password: str = Field(..., max_length=255, description="Password of the user account.")
    work_email: str = Field(..., max_length=100, description="Professional email of the user account.")
    employee_id: int = Field(..., description="ID of the associated employee.")

class UserAccountCreate(UserAccountBase):
    """
    Schema used for creating a new user account.

    Inherits all fields from UserAccountBase schema.
    """
    pass

class UserAccountUpdate(UserAccountBase):
    """
    Schema used when updating an existing user account.

    All fields inherited from UserAccountBase become optional.
    Only fields provided in the request will be updated.
    """
    username: Optional[str] = None
    password: Optional[str] = None
    work_email: Optional[str] = None
    employee_id: Optional[int] = None

class UserAccountRead(UserAccountBase):
    """
    Schema used when reading an user account in the database.

    Inherits all fields from UserAccountBase schema.

    Attributes:
        id_user (int): Unique identifier of the user_account.
        last_login (Optional[datetime]): Date of the last login.
    """
    id_user: int
    last_login: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)