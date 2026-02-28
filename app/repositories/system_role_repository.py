from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.system_roles import SystemRole
from app.schemas.system_role_schema import SystemRoleCreate, SystemRoleUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin
from app.repositories.mixins.name_search_repository import NameSearchRepositoryMixin


class SystemRoleRepository(
    BaseRepository[
        SystemRole, 
        SystemRoleCreate, 
        SystemRoleUpdate
        ], 
    FilterableRepositoryMixin[SystemRole], 
    NameSearchRepositoryMixin[SystemRole]
    ):
    """
    Repository handling CRUD operations for the SystemRole model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the SystemRole model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the system role repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(SystemRole, db)