from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.system_role_repository import SystemRoleRepository
from app.schemas.system_role_schema import SystemRoleCreate, SystemRoleUpdate, SystemRoleRead
from app.logic.base_service import BaseService


class SystemRoleService(BaseService[SystemRoleRepository, SystemRoleCreate, SystemRoleUpdate, SystemRoleRead]):
    """
    UserAccount for handling system_role-related operations.

    Inherits from BaseService to provide CRUD operations using the SystemRole repository.
    """
    def __init__(self, repository: SystemRoleRepository, db: AsyncSession):
        """
        Initialize the SystemRoleService with the SystemRole repository and an asynchronous database session.

        Args:
            repository (ServiceRepository): The repository for performing CRUD operations on SystemRole entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)