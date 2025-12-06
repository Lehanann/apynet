from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.material_service import MaterialService
from app.schemas.material_schema import MaterialCreate, MaterialRead, MaterialUpdate
from app.repositories.material_repository import MaterialRepository

router = APIRouter(prefix="/materials", tags=["materials"])

def get_material_service(db: AsyncSession = Depends(get_session)) -> MaterialService:
    return MaterialService(MaterialRepository(db), db)

@router.get("/",response_model=list[MaterialRead])
async def list_materials(service: MaterialService = Depends(get_material_service)):
    """
    Retrieve a list of all materials from the database.

    This endpoint fetches all materials stored in the database and returns 
    them in the format specified by the `MaterialRead` schema.

    Args:
        service (MaterialService, optional): The service layer for handling
            material-related operations. This is injected automatically using
            `Depends(get_material_service)`.

    Returns:
        List[MaterialRead]: A list of materials represented by the `MaterialRead`
            schema, which includes relevant material details such as name and ID.
    """
    return await service.get_all()

@router.get("/{material_id}", response_model=MaterialRead)
async def get_material(material_id: int, service: MaterialService = Depends(get_material_service)) -> MaterialRead:
    """
    Retrieve material by its ID from the database.

    This endpoint fetches a material by its ID stored in the database and returns 
    them in the format specified by the `MaterialRead` schema.

    Args:
        material_id (int): Unique identifier of th ematerial
        Args:
        service (MaterialService, optional): The service layer for handling
            material-related operations. This is injected automatically using
            `Depends(get_material_service)`.

    Returns:
        material (MaterialRead): A material represented by the `MaterialRead`
            schema, which includes relevant material details such as name and ID.
    """
    
    return await service.get_by_id(material_id)
    
"""@router.get("/material/{material_name}", response_model=MaterialRead)
async def get_material_by_name(material_name: str, service: MaterialService = Depends(get_material_service)):
    service = MaterialService(db)
    return await service.get_material_by_name(material_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_material(data: MaterialCreate, service: MaterialService = Depends(get_material_service)) -> dict[str,str]:
    """
    Create a new material.

    Args:
        data (MaterialCreate): The datas used to create the material.
        service (MaterialService, optional): The service layer for handling
            material-related operations. This is injected automatically using
            `Depends(get_material_service)`.

    Raises:
        HTTPException: If the material creation fails or if the material name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the material was created successfully.
    """
    await service.create(data)
    return {"message": "Material created successfully!"}
   
@router.put("/{material_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{material_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_material(material_id: int, data: MaterialUpdate, service: MaterialService = Depends(get_material_service)) -> dict[str,str]:
    """
    Update a material by its ID.

    Args:
        material_id (int): Unique identifier of the material.
        data (MaterialUpdate): The data used to update the material.
        service (MaterialService, optional): The service layer for handling
            material-related operations. This is injected automatically using
            `Depends(get_material_service)`.

    Raises:
        HTTPException: if the name already exist or if the material is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the material was updated successfully.
    """
    
    await service.update(material_id, data)
    return {"message": "the material updated successfully."}
    
@router.delete("/{material_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_material(material_id: int, service: MaterialService = Depends(get_material_service)) -> dict[str,str]:
    """
    Delete a material by its ID.

    Args:
        material_id (int): Unique identifier of the material.
        service (MaterialService, optional): The service layer for handling
            material-related operations. This is injected automatically using
            `Depends(get_material_service)`.

    Raises:
        HTTPException: if the material with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the material was deleted successfully.
    """

    await service.delete(material_id)
    return {"message": "the material deleted successfully."}
