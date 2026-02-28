from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.phone_assignment_repository import PhoneAssignmentRepository
from app.schemas.phone_assignment_schema import PhoneAssignmentCreate, PhoneAssignmentUpdate, PhoneAssignmentRead
from app.logic.base_service import BaseService
from app.models.tables.phone_assignment import PhoneAssignment

class PhoneAssignmentService(
    BaseService[
        PhoneAssignmentRepository, 
        PhoneAssignmentCreate, 
        PhoneAssignmentUpdate, 
        PhoneAssignmentRead, 
        PhoneAssignment
        ]
    ):
    """
    Service for handling company-related operations.

    Inherits from BaseService to provide CRUD operations using the PhoneAssignment repository.
    """

    def __init__(self, repository: PhoneAssignmentRepository, db: AsyncSession):
        """
        Initialize the PhoneAssignmentService with the PhoneAssignment repository and an asynchronous database session.

        Args:
            repository (PhoneAssignmentRepository): The repository for performing CRUD operations on PhoneAssignment entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)