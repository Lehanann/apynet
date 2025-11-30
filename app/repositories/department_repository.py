from sqlalchemy.ext.asyncio import AsyncSession
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate
from app.repositories.base_repository import BaseRepository

class DepartmentRepository(BaseRepository[Department, DepartmentCreate, DepartmentUpdate]):
    """
    Repository handling CRUD operations for the Department model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Department model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Department repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Department, db)
