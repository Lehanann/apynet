from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.department_repository import DepartmentRepository
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.department import Department

class DepartmentService(
    BaseService[
        DepartmentRepository, 
        DepartmentCreate, 
        DepartmentUpdate, 
        DepartmentRead,
        Department
        ]
    ):
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

    async def create(self, data: DepartmentCreate) -> Department:
        """
        Create a new instance of the department repository.

        Args:
            data (DepartmentCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Department: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Department name already exists")
        return await super().create(data)