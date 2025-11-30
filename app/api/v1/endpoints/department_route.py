from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.department_service import DepartmentService
from app.schemas.department_schema import DepartmentCreate, DepartmentRead, DepartmentUpdate
from app.repositories.department_repository import DepartmentRepository

router = APIRouter(prefix="/departments", tags=["departments"])

def get_department_service(db: AsyncSession = Depends(get_session)) -> DepartmentService:
    return DepartmentService(DepartmentRepository(db), db)

@router.get("/",response_model=list[DepartmentRead])
async def list_departments(service: DepartmentService = Depends(get_department_service)):
    """
    Retrieve a list of all departments from the database.

    This endpoint fetches all departments stored in the database and returns 
    them in the format specified by the `DepartmentRead` schema.

    Args:
        service (DepartmentService, optional): The service layer for handling
            department-related operations. This is injected automatically using
            `Depends(get_department_service)`.

    Returns:
        List[DepartmentRead]: A list of departments represented by the `DepartmentRead`
            schema, which includes relevant department details such as name and ID.
    """
    return await service.get_all()

@router.get("/{department_id}", response_model=DepartmentRead)
async def get_department(department_id: int, service: DepartmentService = Depends(get_department_service)) -> DepartmentRead:
    """
    Retrieve department by its ID from the database.

    This endpoint fetches a department by its ID stored in the database and returns 
    them in the format specified by the `DepartmentRead` schema.

    Args:
        department_id (int): Unique identifier of th edepartment
        Args:
        service (DepartmentService, optional): The service layer for handling
            department-related operations. This is injected automatically using
            `Depends(get_department_service)`.

    Returns:
        department (DepartmentRead): A department represented by the `DepartmentRead`
            schema, which includes relevant department details such as name and ID.
    """
    
    return await service.get_by_id(department_id)
    
"""@router.get("/department/{department_name}", response_model=DepartmentRead)
async def get_department_by_name(department_name: str, service: DepartmentService = Depends(get_department_service)):
    service = DepartmentService(db)
    return await service.get_department_by_name(department_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_department(data: DepartmentCreate, service: DepartmentService = Depends(get_department_service)) -> dict[str,str]:
    """
    Create a new department.

    Args:
        data (DepartmentCreate): The datas used to create the department.
        service (DepartmentService, optional): The service layer for handling
            department-related operations. This is injected automatically using
            `Depends(get_department_service)`.

    Raises:
        HTTPException: If the department creation fails or if the department name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the department was created successfully.
    """
    await service.create(data)
    return {"message": "Department created successfully!"}
   
@router.put("/{department_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{department_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_department(department_id: int, data: DepartmentUpdate, service: DepartmentService = Depends(get_department_service)) -> dict[str,str]:
    """
    Update a department by its ID.

    Args:
        department_id (int): Unique identifier of the department.
        data (DepartmentUpdate): The data used to update the department.
        service (DepartmentService, optional): The service layer for handling
            department-related operations. This is injected automatically using
            `Depends(get_department_service)`.

    Raises:
        HTTPException: if the name already exist or if the department is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the department was updated successfully.
    """
    
    await service.update(department_id, data)
    return {"message": "the department updated successfully."}
    
@router.delete("/{department_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_department(department_id: int, service: DepartmentService = Depends(get_department_service)) -> dict[str,str]:
    """
    Delete a department by its ID.

    Args:
        department_id (int): Unique identifier of the department.
        service (DepartmentService, optional): The service layer for handling
            department-related operations. This is injected automatically using
            `Depends(get_department_service)`.

    Raises:
        HTTPException: if the department with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the department was deleted successfully.
    """

    await service.delete(department_id)
    return {"message": "the department deleted successfully."}
