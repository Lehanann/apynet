from sqlalchemy.ext.asyncio import AsyncSession
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate
from app.repositories.base_repository import BaseRepository

class EmployeeRepository(BaseRepository[Employee, EmployeeCreate, EmployeeUpdate]):
    """
    Repository handling CRUD operations for the Employee model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Employee model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Employee repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Employee, db)