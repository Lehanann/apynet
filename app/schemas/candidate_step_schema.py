from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from app.utils.step_name_enum import StepNameEnum
from app.utils.step_result_enum import StepResultEnum
from datetime import date

class CandidateStepBase(BaseModel):
    """
    Base schema for the CandidateStep, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        candidate_id (int): Identifier of the parent candidate.
        step_name (StepNameEnum): The name of the candidacy's step.
        result (StepResultEnum): Result of the candidacy's step.
        step_date (date): The date of the candidacy's step.

    Notes:
        - The candidate id, step name, result and step date are required.
    """
    
    candidate_id: int = Field(..., description="Identifier of the parent candidate.")
    step_name: StepNameEnum = Field(..., description="Name of the candidacy's step.")
    result: StepResultEnum = Field(..., description="Result of the candidacy's step.")
    step_date: date = Field(..., description="The date of the candidacy's step.")

class CandidateStepCreate(CandidateStepBase):
    """
    Schema used for creating a new candidate step.

    Inherits all fields from CandidateStepBase schema.
    """
    pass

class CandidateStepUpdate(CandidateStepBase):
    """    
    Schema used when updating an existing candidate step.

    All fields inherited from CandidateStepBase become optional.
    Only fields provided in the request will be updated.

    """
    
    candidate_id: Optional[int] = None
    step_name: Optional[StepNameEnum] = None 
    result: Optional[StepResultEnum] = None 
    step_date: Optional[date] = None 

class CandidateStepRead(CandidateStepBase):
    """
    Schema used when reading a candidate step in the database.

    Inherits all attributes from CandidateStepBase.

    Attributes:
        id_step: Unique identifier of the candidate step.
    """
    id_step: int

    model_config = ConfigDict(from_attributes=True)