from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.schemas.corporate_schema import CorporateUpdate, CorporateRead, CorporateCreate
from app.logic.corporate_service import CorporateService

router = APIRouter(prefix="/corporates", tags=["corporates"])

@router.get("/", response_model=list[CorporateRead])
async def list_corporates(db: AsyncSession = Depends(get_session)):
    """
    Docstring for list_corporates
    Route to get a list of corporates -> method GET 
    :param db: Description
    :type db: AsyncSession
    """
    service = CorporateService(db)
    return await service.list_corporates()

@router.get("/{corporate_id}", response_model=CorporateRead)
async def get_corporate(corporate_id: int, db:AsyncSession = Depends(get_session)):
    """
    Docstring for get_corporate
    Route to get a corporate by id -> method GET
    
    :param corporate_id: Identifiant of corporate
    :type corporate_id: int
    :param db: Description
    :type db: AsyncSession
    """
    service = CorporateService(db)
    try:
        return await service.get_corporate(corporate_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/",response_model=CorporateRead, status_code=status.HTTP_201_CREATED)
async def create_corporate(data: CorporateCreate, db: AsyncSession = Depends(get_session)):
    """
    Docstring for create_corporate
    Route to create a new corporate -> method POST
    
    :param data: Schema of validation 
    :type data: CorporateCreate
    :param db: 
    :type db: AsyncSession
    """
    service = CorporateService(db)
    try:
        return await service.create_corporate(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{corporate_id}", response_model=CorporateRead)
@router.patch("/{corporate_id}", response_model=CorporateRead)
async def update_corporate(corporate_id: int, data: CorporateUpdate, db: AsyncSession = Depends(get_session)):
    """
    Docstring for update_corporate
    Route to update a corporate -> method PUT or PATCH

    :param corporate_id: Identifiant corporate
    :type corporate_id: int
    :param data: Description
    :type data: CorporateUpdate
    :param db: Description
    :type db: AsyncSession
    """
    service = CorporateService(db)
    try:
        return await service.update_corporate(corporate_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{corporate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_corporate(corporate_id: int, db: AsyncSession = Depends(get_session)):
    """
    Docstring for delete_corporate
    Route to delete a corporate -> method DELETE
    
    :param corporate_id: Identifiant coporate
    :type corporate_id: int
    :param db: Description
    :type db: AsyncSession
    """
    service = CorporateService(db)
    try:
        return await service.delete_corporate(corporate_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
