from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.site_service import SiteService
from app.schemas.site_schema import SiteCreate, SiteRead, SiteUpdate
from app.repositories.site_repository import SiteRepository

router = APIRouter(prefix="/sites", tags=["sites"])

def get_site_service(db: AsyncSession = Depends(get_session)) -> SiteService:
    return SiteService(SiteRepository(db), db)

@router.get("/",response_model=list[SiteRead])
async def list_sites(service: SiteService = Depends(get_site_service)):
    """
    Retrieve a list of all sites from the database.

    This endpoint fetches all sites stored in the database and returns 
    them in the format specified by the `SiteRead` schema.

    Args:
        service (SiteService, optional): The service layer for handling
            site-related operations. This is injected automatically using
            `Depends(get_site_service)`.

    Returns:
        List[SiteRead]: A list of sites represented by the `SiteRead`
            schema, which includes relevant site details such as name and ID.
    """
    return await service.get_all()

@router.get("/{site_id}", response_model=SiteRead)
async def get_site(site_id: int, service: SiteService = Depends(get_site_service)) -> SiteRead:
    """
    Retrieve site by its ID from the database.

    This endpoint fetches a site by its ID stored in the database and returns 
    them in the format specified by the `SiteRead` schema.

    Args:
        site_id (int): Unique identifier of th esite
        Args:
        service (SiteService, optional): The service layer for handling
            site-related operations. This is injected automatically using
            `Depends(get_site_service)`.

    Returns:
        site (SiteRead): A site represented by the `SiteRead`
            schema, which includes relevant site details such as name and ID.
    """
    
    return await service.get_by_id(site_id)
    
"""@router.get("/site/{site_name}", response_model=SiteRead)
async def get_site_by_name(site_name: str, service: SiteService = Depends(get_site_service)):
    service = SiteService(db)
    return await service.get_site_by_name(site_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_site(data: SiteCreate, service: SiteService = Depends(get_site_service)) -> dict[str,str]:
    """
    Create a new site.

    Args:
        data (SiteCreate): The datas used to create the site.
        service (SiteService, optional): The service layer for handling
            site-related operations. This is injected automatically using
            `Depends(get_site_service)`.

    Raises:
        HTTPException: If the site creation fails or if the site name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the site was created successfully.
    """
    await service.create(data)
    return {"message": "Site created successfully!"}
   
@router.put("/{site_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{site_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_site(site_id: int, data: SiteUpdate, service: SiteService = Depends(get_site_service)) -> dict[str,str]:
    """
    Update a site by its ID.

    Args:
        site_id (int): Unique identifier of the site.
        data (SiteUpdate): The data used to update the site.
        service (SiteService, optional): The service layer for handling
            site-related operations. This is injected automatically using
            `Depends(get_site_service)`.

    Raises:
        HTTPException: if the name already exist or if the site is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the site was updated successfully.
    """
    
    await service.update(site_id, data)
    return {"message": "the site updated successfully."}
    
@router.delete("/{site_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_site(site_id: int, service: SiteService = Depends(get_site_service)) -> dict[str,str]:
    """
    Delete a site by its ID.

    Args:
        site_id (int): Unique identifier of the site.
        service (SiteService, optional): The service layer for handling
            site-related operations. This is injected automatically using
            `Depends(get_site_service)`.

    Raises:
        HTTPException: if the site with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the site was deleted successfully.
    """

    await service.delete(site_id)
    return {"message": "the site deleted successfully."}
