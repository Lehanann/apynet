from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.system_role_repository import SystemRoleRepository
from app.schemas.system_role_schema import SystemRoleCreate, SystemRoleUpdate, SystemRoleRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.system_roles import SystemRole

class SystemRoleService(
    BaseService[
        SystemRoleRepository, 
        SystemRoleCreate, 
        SystemRoleUpdate, 
        SystemRoleRead,
        SystemRole
        ]
    ):
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

    async def create(self, data: SystemRoleCreate) -> SystemRole:
        """
        Create a new instance of the system role repository.        

        Args:
            data (SystemRoleCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            SystemRole: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="System role name already exists")
        return await super().create(data)