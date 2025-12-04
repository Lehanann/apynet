from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_account_repository import UserAccountRepository
from app.schemas.user_account_schema import UserAccountCreate, UserAccountUpdate, UserAccountRead
from app.logic.base_service import BaseService

class UserAccountService(BaseService[UserAccountRepository, UserAccountCreate, UserAccountUpdate, UserAccountRead]):
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