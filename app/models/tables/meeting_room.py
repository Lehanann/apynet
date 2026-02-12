from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base


class MeetingRoom(Base):
    """
    Represents a meeting_room stored in the database. 

    Attributes:
        id_meeting_room (int): Unique identifier of the MeetingRoom.
        name (str): Official name of the MeetingRoom.
        company_id: Foreign key referencing the parent Company
    
    Relationships:
        company (Company): Many-to-one relationship pointing to the
        Company this meeting_room belongs to.
    
    Notes:
        - The name must be 100 characters max.
        - The name is required
    """
    __tablename__ = "meeting_rooms"

    id_meeting_room: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    site_id: Mapped[int] = mapped_column(Integer, ForeignKey("sites.id_site"), nullable=False)

    site = relationship("Site", back_populates="meeting_rooms")
    