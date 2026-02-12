from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base

class PhoneNumber(Base):
    """
    Represents a phone number stored in the database.

    Attributes:
        id_phone (int): Unique identifier of the phone number.
        internal_number (str): Unique phone number on 4 characters(ex.: 1010).
        external_number (str): External number phone on 15 characters max(ex.: +330504030201).
        active (bool): Whether the phone number is or not active.

    Relationships:
        phone_assignment (PhoneAssignment): One-to-One 
    """

    __tablename__ = "phone_numbers"

    id_phone: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    internal_number: Mapped[str] = mapped_column(String(4),unique=True, nullable=False)
    external_number: Mapped[str] = mapped_column(String(15))
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="true")

    phone_assignment = relationship("PhoneAssignment", back_populates="phone_number")