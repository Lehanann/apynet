from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base

class Material(Base):
    """
    Represents a material stored in the database.

    Attributes:
        id_material (int): Unique identifier of the material.
        name (str): The name of the materials.
        type (str): The type of the material.
        description (text): Description of the material.
    Notes:
        - The name and type are required.
        - The name must be 100 characters max.
        - The type must be 50 characters max.
    """
    __tablename__ = "materials"

    id_material: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text)
