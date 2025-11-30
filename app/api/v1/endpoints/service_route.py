from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.service_manager import ServiceManager
from app.schemas.service_schema import ServiceCreate, ServiceRead, ServiceUpdate
from app.repositories.service_repository import ServiceRepository

router = APIRouter(prefix="/services", tags=["services"])

def get_service_service(db: AsyncSession = Depends(get_session)) -> ServiceManager:
    return ServiceManager(ServiceRepository(db), db)

@router.get("/",response_model=list[ServiceRead])
async def list_services(service: ServiceManager = Depends(get_service_service)):
    """
    Retrieve a list of all services from the database.

    This endpoint fetches all services stored in the database and returns 
    them in the format specified by the `ServiceRead` schema.

    Args:
        service (ServiceManager, optional): The service layer for handling
            service-related operations. This is injected automatically using
            `Depends(get_service_service)`.

    Returns:
        List[ServiceRead]: A list of services represented by the `ServiceRead`
            schema, which includes relevant service details such as name and ID.
    """
    return await service.get_all()

@router.get("/{service_id}", response_model=ServiceRead)
async def get_service(service_id: int, service: ServiceManager = Depends(get_service_service)) -> ServiceRead:
    """
    Retrieve service by its ID from the database.

    This endpoint fetches a service by its ID stored in the database and returns 
    them in the format specified by the `ServiceRead` schema.

    Args:
        service_id (int): Unique identifier of th eservice
        Args:
        service (ServiceManager, optional): The service layer for handling
            service-related operations. This is injected automatically using
            `Depends(get_service_service)`.

    Returns:
        service (ServiceRead): A service represented by the `ServiceRead`
            schema, which includes relevant service details such as name and ID.
    """
    
    return await service.get_by_id(service_id)
    
"""@router.get("/service/{service_name}", response_model=ServiceRead)
async def get_service_by_name(service_name: str, service: ServiceManager = Depends(get_service_service)):
    service = ServiceManager(db)
    return await service.get_service_by_name(service_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_service(data: ServiceCreate, service: ServiceManager = Depends(get_service_service)) -> dict[str,str]:
    """
    Create a new service.

    Args:
        data (ServiceCreate): The datas used to create the service.
        service (ServiceManager, optional): The service layer for handling
            service-related operations. This is injected automatically using
            `Depends(get_service_service)`.

    Raises:
        HTTPException: If the service creation fails or if the service name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the service was created successfully.
    """
    await service.create(data)
    return {"message": "Service created successfully!"}
   
@router.put("/{service_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{service_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_service(service_id: int, data: ServiceUpdate, service: ServiceManager = Depends(get_service_service)) -> dict[str,str]:
    """
    Update a service by its ID.

    Args:
        service_id (int): Unique identifier of the service.
        data (ServiceUpdate): The data used to update the service.
        service (ServiceManager, optional): The service layer for handling
            service-related operations. This is injected automatically using
            `Depends(get_service_service)`.

    Raises:
        HTTPException: if the name already exist or if the service is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the service was updated successfully.
    """
    
    await service.update(service_id, data)
    return {"message": "the service updated successfully."}
    
@router.delete("/{service_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_service(service_id: int, service: ServiceManager = Depends(get_service_service)) -> dict[str,str]:
    """
    Delete a service by its ID.

    Args:
        service_id (int): Unique identifier of the service.
        service (ServiceManager, optional): The service layer for handling
            service-related operations. This is injected automatically using
            `Depends(get_service_service)`.

    Raises:
        HTTPException: if the service with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the service was deleted successfully.
    """

    await service.delete(service_id)
    return {"message": "the service deleted successfully."}
