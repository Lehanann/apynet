from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.candidate_step_service import CandidateStepService
from app.schemas.candidate_step_schema import CandidateStepCreate, CandidateStepRead, CandidateStepUpdate
from app.repositories.candidate_step_repository import CandidateStepRepository

router = APIRouter(prefix="/candidate-steps", tags=["candidate-steps"])

def get_candidate_step_service(db: AsyncSession = Depends(get_session)) -> CandidateStepService:
    return CandidateStepService(CandidateStepRepository(db), db)

@router.get("/",response_model=list[CandidateStepRead])
async def list_candidate_steps(service: CandidateStepService = Depends(get_candidate_step_service)):
    """
    Retrieve a list of all candidate steps from the database.

    This endpoint fetches all candidate steps stored in the database and returns 
    them in the format specified by the `CandidateStepRead` schema.

    Args:
        service (CandidateStepService, optional): The service layer for handling
            candidate_step-related operations. This is injected automatically using
            `Depends(get_candidate_step_service)`.

    Returns:
        List[CandidateStepRead]: A list of candidate steps represented by the `CandidateStepRead`
            schema, which includes relevant candidate_step details such as name and ID.
    """
    return await service.get_all()

@router.get("/{candidate_step_id}", response_model=CandidateStepRead)
async def get_candidate_step(candidate_step_id: int, service: CandidateStepService = Depends(get_candidate_step_service)) -> CandidateStepRead:
    """
    Retrieve candidate_step by its ID from the database.

    This endpoint fetches a candidate_step by its ID stored in the database and returns 
    them in the format specified by the `CandidateStepRead` schema.

    Args:
        candidate_step_id (int): Unique identifier of th ecandidate_step
        Args:
        service (CandidateStepService, optional): The service layer for handling
            candidate_step-related operations. This is injected automatically using
            `Depends(get_candidate_step_service)`.

    Returns:
        candidate_step (CandidateStepRead): A candidate_step represented by the `CandidateStepRead`
            schema, which includes relevant candidate_step details such as name and ID.
    """
    
    return await service.get_by_id(candidate_step_id)
    
"""@router.get("/candidate_step/{candidate_step_name}", response_model=CandidateStepRead)
async def get_candidate_step_by_name(candidate_step_name: str, service: CandidateStepService = Depends(get_candidate_step_service)):
    service = CandidateStepService(db)
    return await service.get_candidate_step_by_name(candidate_step_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_candidate_step(data: CandidateStepCreate, service: CandidateStepService = Depends(get_candidate_step_service)) -> dict[str,str]:
    """
    Create a new candidate_step.

    Args:
        data (CandidateStepCreate): The datas used to create the candidate_step.
        service (CandidateStepService, optional): The service layer for handling
            candidate_step-related operations. This is injected automatically using
            `Depends(get_candidate_step_service)`.

    Raises:
        HTTPException: If the candidate_step creation fails or if the candidate_step name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the candidate_step was created successfully.
    """
    await service.create(data)
    return {"message": "CandidateStep created successfully!"}
   
@router.put("/{candidate_step_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{candidate_step_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_candidate_step(candidate_step_id: int, data: CandidateStepUpdate, service: CandidateStepService = Depends(get_candidate_step_service)) -> dict[str,str]:
    """
    Update a candidate_step by its ID.

    Args:
        candidate_step_id (int): Unique identifier of the candidate_step.
        data (CandidateStepUpdate): The data used to update the candidate_step.
        service (CandidateStepService, optional): The service layer for handling
            candidate_step-related operations. This is injected automatically using
            `Depends(get_candidate_step_service)`.

    Raises:
        HTTPException: if the name already exist or if the candidate_step is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the candidate_step was updated successfully.
    """
    
    await service.update(candidate_step_id, data)
    return {"message": "the candidate_step updated successfully."}
    
@router.delete("/{candidate_step_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_candidate_step(candidate_step_id: int, service: CandidateStepService = Depends(get_candidate_step_service)) -> dict[str,str]:
    """
    Delete a candidate_step by its ID.

    Args:
        candidate_step_id (int): Unique identifier of the candidate_step.
        service (CandidateStepService, optional): The service layer for handling
            candidate_step-related operations. This is injected automatically using
            `Depends(get_candidate_step_service)`.

    Raises:
        HTTPException: if the candidate_step with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the candidate_step was deleted successfully.
    """

    await service.delete(candidate_step_id)
    return {"message": "the candidate_step deleted successfully."}
