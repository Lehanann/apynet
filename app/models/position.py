from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base

class Position(Base):
    """
    Represents a position stored in the database.

    Attributes:
        id_position (int): Unique identifier of the position.
        name (str): Official name of the position.
        description (text): Description of the position.
    
    relationship:

    Notes:
        - The name is required.
        - The name must be 100 characters max.
        - The description is required.
        - The default value of description is empty string ''.        
    """

    __tablename__ = "positions"

    id_position: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default='', server_default='')
