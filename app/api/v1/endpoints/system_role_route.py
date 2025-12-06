from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.system_role_service import SystemRoleService
from app.schemas.system_role_schema import SystemRoleCreate, SystemRoleRead, SystemRoleUpdate
from app.repositories.system_role_repository import SystemRoleRepository

router = APIRouter(prefix="/system-roles", tags=["system-roles"])

def get_system_role_service(db: AsyncSession = Depends(get_session)) -> SystemRoleService:
    return SystemRoleService(SystemRoleRepository(db), db)

@router.get("/",response_model=list[SystemRoleRead])
async def list_system_roles(service: SystemRoleService = Depends(get_system_role_service)):
    """
    Retrieve a list of all system_roles from the database.

    This endpoint fetches all system_roles stored in the database and returns 
    them in the format specified by the `SystemRoleRead` schema.

    Args:
        service (SystemRoleService, optional): The service layer for handling
            system_role-related operations. This is injected automatically using
            `Depends(get_system_role_service)`.

    Returns:
        List[SystemRoleRead]: A list of system_roles represented by the `SystemRoleRead`
            schema, which includes relevant system_role details such as name and ID.
    """
    return await service.get_all()

@router.get("/{system_role_id}", response_model=SystemRoleRead)
async def get_system_role(system_role_id: int, service: SystemRoleService = Depends(get_system_role_service)) -> SystemRoleRead:
    """
    Retrieve system_role by its ID from the database.

    This endpoint fetches a system_role by its ID stored in the database and returns 
    them in the format specified by the `SystemRoleRead` schema.

    Args:
        system_role_id (int): Unique identifier of th esystem_role
        Args:
        service (SystemRoleService, optional): The service layer for handling
            system_role-related operations. This is injected automatically using
            `Depends(get_system_role_service)`.

    Returns:
        system_role (SystemRoleRead): A system_role represented by the `SystemRoleRead`
            schema, which includes relevant system_role details such as name and ID.
    """
    
    return await service.get_by_id(system_role_id)
    
"""@router.get("/system_role/{system_role_name}", response_model=SystemRoleRead)
async def get_system_role_by_name(system_role_name: str, service: SystemRoleService = Depends(get_system_role_service)):
    service = SystemRoleService(db)
    return await service.get_system_role_by_name(system_role_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_system_role(data: SystemRoleCreate, service: SystemRoleService = Depends(get_system_role_service)) -> dict[str,str]:
    """
    Create a new system_role.

    Args:
        data (SystemRoleCreate): The datas used to create the system_role.
        service (SystemRoleService, optional): The service layer for handling
            system_role-related operations. This is injected automatically using
            `Depends(get_system_role_service)`.

    Raises:
        HTTPException: If the system_role creation fails or if the system_role name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the system_role was created successfully.
    """
    await service.create(data)
    return {"message": "SystemRole created successfully!"}
   
@router.put("/{system_role_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{system_role_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_system_role(system_role_id: int, data: SystemRoleUpdate, service: SystemRoleService = Depends(get_system_role_service)) -> dict[str,str]:
    """
    Update a system_role by its ID.

    Args:
        system_role_id (int): Unique identifier of the system_role.
        data (SystemRoleUpdate): The data used to update the system_role.
        service (SystemRoleService, optional): The service layer for handling
            system_role-related operations. This is injected automatically using
            `Depends(get_system_role_service)`.

    Raises:
        HTTPException: if the name already exist or if the system_role is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the system_role was updated successfully.
    """
    
    await service.update(system_role_id, data)
    return {"message": "the system_role updated successfully."}
    
@router.delete("/{system_role_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_system_role(system_role_id: int, service: SystemRoleService = Depends(get_system_role_service)) -> dict[str,str]:
    """
    Delete a system_role by its ID.

    Args:
        system_role_id (int): Unique identifier of the system_role.
        service (SystemRoleService, optional): The service layer for handling
            system_role-related operations. This is injected automatically using
            `Depends(get_system_role_service)`.

    Raises:
        HTTPException: if the system_role with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the system_role was deleted successfully.
    """

    await service.delete(system_role_id)
    return {"message": "the system_role deleted successfully."}
