from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_account import UserAccount
from app.schemas.user_account_schema import UserAccountCreate, UserAccountUpdate
from app.repositories.base_repository import BaseRepository


class UserAccountRepository(BaseRepository[UserAccount, UserAccountCreate, UserAccountUpdate]):
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