from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_account_repository import UserAccountRepository
from app.schemas.user_account_schema import UserAccountCreate, UserAccountUpdate, UserAccountRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.user_account import UserAccount

class UserAccountService(
    BaseService[
        UserAccountRepository, 
        UserAccountCreate, 
        UserAccountUpdate, 
        UserAccountRead,
        UserAccount
        ]
    ):
    """
    UserAccount for handling user_account-related operations.

    Inherits from BaseService to provide CRUD operations using the UserAccount repository.
    """
    def __init__(self, repository: UserAccountRepository, db: AsyncSession):
        """
        Initialize the UserAccountService with the UserAccount repository and an asynchronous database session.

        Args:
            repository (ServiceRepository): The repository for performing CRUD operations on Service entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)

    async def create(self, data: UserAccountCreate) -> UserAccount:
        """
        Create a new instance of the user account repository.

        Args:
            data (UserAccountCreate): Schema containing fields to create a new instance

        Raises:
            HTTPException: if username already exists, in the repository. 

        Returns:
            UserAccount: The newly created instance.
        """

        if data.username:
            existing = await self.repository.get_by_username(data.username)

            if existing:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The username already exists.")
        
        return await super().create(data)