from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base


class PhoneAssignment(Base):
    """
    Represents a phone_assignment stored in the database. 

    Attributes:
        id_phone_assignment (int): Unique identifier of the MeetingRoom.
        phone_id (int): Foreign key referencing the parent phone number.
        assignment_type (str): Referencing the type of assignment check if employee or meeting_room or service.
        assigned_id
        
    Relationships:
        phone_number (PhoneNumber): One-to-one relationship pointing to the
        PhoneNumber this phone_assignment belongs to.
    """
    __tablename__ = "phone_assignments"

    id_assignment: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    phone_id: Mapped[int] = mapped_column(Integer, ForeignKey("phone_numbers.id_phone"), nullable=False)
    assigned_id: Mapped[int] = mapped_column(Integer, nullable=False)
    assigned_type: Mapped[str] = mapped_column(String(30), nullable=False)

    phone_number = relationship("PhoneNumber", back_populates="phone_assignment")