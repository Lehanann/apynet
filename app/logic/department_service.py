from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.department_repository import DepartmentRepository
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentRead
from app.logic.base_service import BaseService, RepositoryType

class DepartmentService(BaseService[DepartmentRepository, DepartmentCreate, DepartmentUpdate, DepartmentRead]):
    """
    Service for handling department-related operations.

    Inherits from BaseService to provide CRUD operations using the Department repository.
    """

    def __init__(self, repository: DepartmentRepository, db: AsyncSession):
        """
        Initialize the DepartmentService with the Department repository and an asynchronous database session.

        Args:
            repository (DepartmentRepository): The repository for performing CRUD operations on Department entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)
