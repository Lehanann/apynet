from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base

class Corporate(Base):
    """
    Represents a corporate (companies group) stored in the database.

    Attributes:
        id_corporate (int): Unique identifier of the Corporate
        name (str): Official name of the Corporate

    Relationships:
        companies: One-to-many relationship with the Company model 

    Notes:
        - The name must be 100 characters max
        - The name is required
    """
    __tablename__ = "corporates"

    id_corporate: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    companies = relationship("Company", back_populates="corporate")