from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.meeting_room_repository import MeetingRoomRepository
from app.schemas.meeting_room_schema import MeetingRoomCreate, MeetingRoomUpdate, MeetingRoomRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.meeting_room import MeetingRoom

class MeetingRoomService(
    BaseService[
        MeetingRoomRepository, 
        MeetingRoomCreate, 
        MeetingRoomUpdate, 
        MeetingRoomRead, 
        MeetingRoom
        ]
    ):
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
    
    async def create(self, data: MeetingRoomCreate) -> MeetingRoom:
        """
        Create a new instance of the meeting room repository.

        Args:
            data (MeetingRoomCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            MeetingRoom: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Meeting room name already exists")
        return await super().create(data)