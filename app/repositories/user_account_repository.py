from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.user_account import UserAccount
from app.schemas.user_account_schema import UserAccountCreate, UserAccountUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin

class UserAccountRepository(
    BaseRepository[
        UserAccount, 
        UserAccountCreate, 
        UserAccountUpdate
        ], 
    FilterableRepositoryMixin[UserAccount]
    ):
    """
    Repository handling CRUD operations for the UserAccount model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the UserAccount model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """

    def __init__(self, db: AsyncSession):
        """
        Initialize the user account repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(UserAccount, db)

    async def get_by_username(self, username: str) -> UserAccount | None:
        """Retrieve an user account by its username.

        Args:
            username (str): The username of the user account.

        Returns:
            UserAccount: The matching user account if found, otherwise None.
        """
        return await self.get_one_by("username", username)

    async def get_by_work_email(self, work_email: str) -> UserAccount | None:
        """Retreive an user account by its email.

        Args:
            work_email (str): The work email of the user account.

        Returns:
            UserAccount: The matching user account if found, otherwise None.
        """
        return await self.get_one_by("work_email", work_email)