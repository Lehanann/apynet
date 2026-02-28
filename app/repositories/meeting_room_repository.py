from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.meeting_room import MeetingRoom
from app.schemas.meeting_room_schema import MeetingRoomCreate, MeetingRoomUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin
from app.repositories.mixins.name_search_repository import NameSearchRepositoryMixin

class MeetingRoomRepository(
    BaseRepository[
        MeetingRoom, 
        MeetingRoomCreate, 
        MeetingRoomUpdate
        ], 
    FilterableRepositoryMixin[MeetingRoom], 
    NameSearchRepositoryMixin[MeetingRoom]
    ):
    """
    Repository handling CRUD operations for the MeetingRoom model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the MeetingRoom model,
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
        super().__init__(MeetingRoom, db)