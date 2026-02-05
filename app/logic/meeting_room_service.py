from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.meeting_room_repository import MeetingRoomRepository
from app.schemas.meeting_room_schema import MeetingRoomCreate, MeetingRoomUpdate, MeetingRoomRead
from app.logic.base_service import BaseService

class MeetingRoomService(BaseService[MeetingRoomRepository, MeetingRoomCreate, MeetingRoomUpdate, MeetingRoomRead]):
    """
    Service for handling Phone number -related operations.

    Inherits from BaseService to provide CRUD operations using the MeetingRoom repository.
    """

    def __init__(self, repository: MeetingRoomRepository, db: AsyncSession):
        """
        Initialize the MeetingRoomService with the MeetingRoom repository and an asynchronous database session.

        Args:
            repository (MeetingRoomRepository): The repository for performing CRUD operations on MeetingRoom entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)