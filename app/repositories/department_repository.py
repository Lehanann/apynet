from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.department import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin
from app.repositories.mixins.name_search_repository import NameSearchRepositoryMixin

class DepartmentRepository(
    BaseRepository[
        Department, 
        DepartmentCreate, 
        DepartmentUpdate
        ], 
    FilterableRepositoryMixin[Department], 
    NameSearchRepositoryMixin[Department]
    ):
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