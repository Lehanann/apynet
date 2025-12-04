from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeRead
from app.logic.base_service import BaseService, RepositoryType

class EmployeeService(BaseService[EmployeeRepository, EmployeeCreate, EmployeeUpdate, EmployeeRead]):
    """
    Service for handling employee-related operations.

    Inherits from BaseService to provide CRUD operations using the Employee repository.
    """
    
    def __init__(self, repository: EmployeeRepository, db: AsyncSession):
        """
        Initialize the EmployeenService with the Employee repository and an asynchronous database session.

        Args:
            repository (EmployeeRepository): The repository for performing CRUD operations on Employee entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)