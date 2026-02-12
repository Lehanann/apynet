from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class CandidateBase(BaseModel):
    """
    Base schema for the Candidate, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        first_name (str): First name of the candidate.
        last_name (str): Last name of the candidate.
        email (str): Email of the candidate.
        phone (str): Phone of the candidate.
        archived (bool): Status of the candidacy.

    Notes:
        - The first name and last name must be 50 characters max.
        - The email must be 100 characters max.
        - The phone must be 20 characters max.
        - The first name, last name is required.
    """

    first_name: str = Field(..., max_length=50, description="The first name of the candidate.")
    last_name: str = Field(..., max_length=50, description="The last name of the candidate.")
    email: str = Field(..., max_length=100, description="The email of the candidate.")
    phone: str = Field(..., max_length=20, description="The phone of the candidate.")
    archived: bool = Field(..., description="The status of the candidacy.")

class CandidateCreate(CandidateBase):
    """
    Schema used for creating a new candidate.

    Inherits all fields from CandidateBase schema.
    """
    pass

class CandidateUpdate(CandidateBase):
    """    
    Schema used when updating an existing candidate.

    All fields inherited from CandidateBase become optional.
    Only fields provided in the request will be updated.

    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    archived: Optional[bool] = None

class CandidateRead(CandidateBase):
    """
    Schema used when reading a candidate in the database.

    Inherits all attributes from CandidateBase.

    Attributes:
        id_candidate: Unique identifier of the candidate.
    """
    id_candidate: int

    model_config = ConfigDict(from_attributes=True)