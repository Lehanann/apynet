from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.meeting_room_service import MeetingRoomService
from app.schemas.meeting_room_schema import MeetingRoomCreate, MeetingRoomRead, MeetingRoomUpdate
from app.repositories.meeting_room_repository import MeetingRoomRepository

router = APIRouter(prefix="/meeting-rooms", tags=["meeting-rooms"])

def get_meeting_room_service(db: AsyncSession = Depends(get_session)) -> MeetingRoomService:
    return MeetingRoomService(MeetingRoomRepository(db), db)

@router.get("/",response_model=list[MeetingRoomRead])
async def list_meeting_rooms(service: MeetingRoomService = Depends(get_meeting_room_service)):
    """
    Retrieve a list of all meeting_rooms from the database.

    This endpoint fetches all meeting_rooms stored in the database and returns 
    them in the format specified by the `MeetingRoomRead` schema.

    Args:
        service (MeetingRoomService, optional): The service layer for handling
            meeting_room-related operations. This is injected automatically using
            `Depends(get_meeting_room_service)`.

    Returns:
        List[MeetingRoomRead]: A list of meeting_rooms represented by the `MeetingRoomRead`
            schema, which includes relevant meeting_room details such as name and ID.
    """
    return await service.get_all()

@router.get("/{meeting_room_id}", response_model=MeetingRoomRead)
async def get_meeting_room(meeting_room_id: int, service: MeetingRoomService = Depends(get_meeting_room_service)) -> MeetingRoomRead:
    """
    Retrieve meeting_room by its ID from the database.

    This endpoint fetches a meeting_room by its ID stored in the database and returns 
    them in the format specified by the `MeetingRoomRead` schema.

    Args:
        meeting_room_id (int): Unique identifier of th emeeting_room
        Args:
        service (MeetingRoomService, optional): The service layer for handling
            meeting_room-related operations. This is injected automatically using
            `Depends(get_meeting_room_service)`.

    Returns:
        meeting_room (MeetingRoomRead): A meeting_room represented by the `MeetingRoomRead`
            schema, which includes relevant meeting_room details such as name and ID.
    """
    
    return await service.get_by_id(meeting_room_id)
    
"""@router.get("/meeting_room/{meeting_room_name}", response_model=MeetingRoomRead)
async def get_meeting_room_by_name(meeting_room_name: str, service: MeetingRoomService = Depends(get_meeting_room_service)):
    service = MeetingRoomService(db)
    return await service.get_meeting_room_by_name(meeting_room_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_meeting_room(data: MeetingRoomCreate, service: MeetingRoomService = Depends(get_meeting_room_service)) -> dict[str,str]:
    """
    Create a new meeting_room.

    Args:
        data (MeetingRoomCreate): The datas used to create the meeting_room.
        service (MeetingRoomService, optional): The service layer for handling
            meeting_room-related operations. This is injected automatically using
            `Depends(get_meeting_room_service)`.

    Raises:
        HTTPException: If the meeting_room creation fails or if the meeting_room name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the meeting_room was created successfully.
    """
    await service.create(data)
    return {"message": "MeetingRoom created successfully!"}
   
@router.put("/{meeting_room_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{meeting_room_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_meeting_room(meeting_room_id: int, data: MeetingRoomUpdate, service: MeetingRoomService = Depends(get_meeting_room_service)) -> dict[str,str]:
    """
    Update a meeting_room by its ID.

    Args:
        meeting_room_id (int): Unique identifier of the meeting_room.
        data (MeetingRoomUpdate): The data used to update the meeting_room.
        service (MeetingRoomService, optional): The service layer for handling
            meeting_room-related operations. This is injected automatically using
            `Depends(get_meeting_room_service)`.

    Raises:
        HTTPException: if the name already exist or if the meeting_room is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the meeting_room was updated successfully.
    """
    
    await service.update(meeting_room_id, data)
    return {"message": "the meeting_room updated successfully."}
    
@router.delete("/{meeting_room_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_meeting_room(meeting_room_id: int, service: MeetingRoomService = Depends(get_meeting_room_service)) -> dict[str,str]:
    """
    Delete a meeting_room by its ID.

    Args:
        meeting_room_id (int): Unique identifier of the meeting_room.
        service (MeetingRoomService, optional): The service layer for handling
            meeting_room-related operations. This is injected automatically using
            `Depends(get_meeting_room_service)`.

    Raises:
        HTTPException: if the meeting_room with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the meeting_room was deleted successfully.
    """

    await service.delete(meeting_room_id)
    return {"message": "the meeting_room deleted successfully."}
