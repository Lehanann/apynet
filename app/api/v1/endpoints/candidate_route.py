from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.candidate_service import CandidateService
from app.schemas.candidate_schema import CandidateCreate, CandidateRead, CandidateUpdate
from app.repositories.candidate_repository import CandidateRepository

router = APIRouter(prefix="/candidates", tags=["candidates"])

def get_candidate_service(db: AsyncSession = Depends(get_session)) -> CandidateService:
    return CandidateService(CandidateRepository(db), db)

@router.get("/",response_model=list[CandidateRead])
async def list_candidates(service: CandidateService = Depends(get_candidate_service)):
    """
    Retrieve a list of all candidates from the database.

    This endpoint fetches all candidates stored in the database and returns 
    them in the format specified by the `CandidateRead` schema.

    Args:
        service (CandidateService, optional): The service layer for handling
            candidate-related operations. This is injected automatically using
            `Depends(get_candidate_service)`.

    Returns:
        List[CandidateRead]: A list of candidates represented by the `CandidateRead`
            schema, which includes relevant candidate details such as name and ID.
    """
    return await service.get_all()

@router.get("/{candidate_id}", response_model=CandidateRead)
async def get_candidate(candidate_id: int, service: CandidateService = Depends(get_candidate_service)) -> CandidateRead:
    """
    Retrieve candidate by its ID from the database.

    This endpoint fetches a candidate by its ID stored in the database and returns 
    them in the format specified by the `CandidateRead` schema.

    Args:
        candidate_id (int): Unique identifier of th ecandidate
        Args:
        service (CandidateService, optional): The service layer for handling
            candidate-related operations. This is injected automatically using
            `Depends(get_candidate_service)`.

    Returns:
        candidate (CandidateRead): A candidate represented by the `CandidateRead`
            schema, which includes relevant candidate details such as name and ID.
    """
    
    return await service.get_by_id(candidate_id)
    
"""@router.get("/candidate/{candidate_name}", response_model=CandidateRead)
async def get_candidate_by_name(candidate_name: str, service: CandidateService = Depends(get_candidate_service)):
    service = CandidateService(db)
    return await service.get_candidate_by_name(candidate_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_candidate(data: CandidateCreate, service: CandidateService = Depends(get_candidate_service)) -> dict[str,str]:
    """
    Create a new candidate.

    Args:
        data (CandidateCreate): The datas used to create the candidate.
        service (CandidateService, optional): The service layer for handling
            candidate-related operations. This is injected automatically using
            `Depends(get_candidate_service)`.

    Raises:
        HTTPException: If the candidate creation fails or if the candidate name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the candidate was created successfully.
    """
    await service.create(data)
    return {"message": "Candidate created successfully!"}
   
@router.put("/{candidate_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{candidate_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_candidate(candidate_id: int, data: CandidateUpdate, service: CandidateService = Depends(get_candidate_service)) -> dict[str,str]:
    """
    Update a candidate by its ID.

    Args:
        candidate_id (int): Unique identifier of the candidate.
        data (CandidateUpdate): The data used to update the candidate.
        service (CandidateService, optional): The service layer for handling
            candidate-related operations. This is injected automatically using
            `Depends(get_candidate_service)`.

    Raises:
        HTTPException: if the name already exist or if the candidate is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the candidate was updated successfully.
    """
    
    await service.update(candidate_id, data)
    return {"message": "the candidate updated successfully."}
    
@router.delete("/{candidate_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_candidate(candidate_id: int, service: CandidateService = Depends(get_candidate_service)) -> dict[str,str]:
    """
    Delete a candidate by its ID.

    Args:
        candidate_id (int): Unique identifier of the candidate.
        service (CandidateService, optional): The service layer for handling
            candidate-related operations. This is injected automatically using
            `Depends(get_candidate_service)`.

    Raises:
        HTTPException: if the candidate with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the candidate was deleted successfully.
    """

    await service.delete(candidate_id)
    return {"message": "the candidate deleted successfully."}
