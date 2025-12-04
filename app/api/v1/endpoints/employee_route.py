from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.employee_service import EmployeeService
from app.schemas.employee_schema import EmployeeCreate, EmployeeRead, EmployeeUpdate
from app.repositories.employee_repository import EmployeeRepository

router = APIRouter(prefix="/employees", tags=["employees"])

def get_employee_service(db: AsyncSession = Depends(get_session)) -> EmployeeService:
    return EmployeeService(EmployeeRepository(db), db)

@router.get("/",response_model=list[EmployeeRead])
async def list_employees(service: EmployeeService = Depends(get_employee_service)):
    """
    Retrieve a list of all employees from the database.

    This endpoint fetches all employees stored in the database and returns 
    them in the format specified by the `EmployeeRead` schema.

    Args:
        service (EmployeeService, optional): The service layer for handling
            employee-related operations. This is injected automatically using
            `Depends(get_employee_service)`.

    Returns:
        List[EmployeeRead]: A list of employees represented by the `EmployeeRead`
            schema, which includes relevant employee details such as name and ID.
    """
    return await service.get_all()

@router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee(employee_id: int, service: EmployeeService = Depends(get_employee_service)) -> EmployeeRead:
    """
    Retrieve employee by its ID from the database.

    This endpoint fetches a employee by its ID stored in the database and returns 
    them in the format specified by the `EmployeeRead` schema.

    Args:
        employee_id (int): Unique identifier of th eemployee
        Args:
        service (EmployeeService, optional): The service layer for handling
            employee-related operations. This is injected automatically using
            `Depends(get_employee_service)`.

    Returns:
        employee (EmployeeRead): A employee represented by the `EmployeeRead`
            schema, which includes relevant employee details such as name and ID.
    """
    
    return await service.get_by_id(employee_id)
    
"""@router.get("/employee/{employee_name}", response_model=EmployeeRead)
async def get_employee_by_name(employee_name: str, service: EmployeeService = Depends(get_employee_service)):
    service = EmployeeService(db)
    return await service.get_employee_by_name(employee_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_employee(data: EmployeeCreate, service: EmployeeService = Depends(get_employee_service)) -> dict[str,str]:
    """
    Create a new employee.

    Args:
        data (EmployeeCreate): The datas used to create the employee.
        service (EmployeeService, optional): The service layer for handling
            employee-related operations. This is injected automatically using
            `Depends(get_employee_service)`.

    Raises:
        HTTPException: If the employee creation fails or if the employee name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the employee was created successfully.
    """
    await service.create(data)
    return {"message": "Employee created successfully!"}
   
@router.put("/{employee_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{employee_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_employee(employee_id: int, data: EmployeeUpdate, service: EmployeeService = Depends(get_employee_service)) -> dict[str,str]:
    """
    Update a employee by its ID.

    Args:
        employee_id (int): Unique identifier of the employee.
        data (EmployeeUpdate): The data used to update the employee.
        service (EmployeeService, optional): The service layer for handling
            employee-related operations. This is injected automatically using
            `Depends(get_employee_service)`.

    Raises:
        HTTPException: if the name already exist or if the employee is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the employee was updated successfully.
    """
    
    await service.update(employee_id, data)
    return {"message": "the employee updated successfully."}
    
@router.delete("/{employee_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_employee(employee_id: int, service: EmployeeService = Depends(get_employee_service)) -> dict[str,str]:
    """
    Delete a employee by its ID.

    Args:
        employee_id (int): Unique identifier of the employee.
        service (EmployeeService, optional): The service layer for handling
            employee-related operations. This is injected automatically using
            `Depends(get_employee_service)`.

    Raises:
        HTTPException: if the employee with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the employee was deleted successfully.
    """

    await service.delete(employee_id)
    return {"message": "the employee deleted successfully."}
