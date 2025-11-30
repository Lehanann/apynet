from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base


class Company(Base):
    """
    Represents a company stored in the database.

    Attributes:
        id_company (int): Unique identifier of the Company.
        name (str): Official name of the Company.
        corporate_id (int): Foreign key referencing the parent Corporate.

    Relationships:
        corporate (Corporate): Many-to-one relationship pointing to the
        Corporate this company belongs to.
        departments: One-to-many relationship with the Department model

    Notes:
        - The name must be 100 characters max.
        - The name is required.
    """
    __tablename__ = "companies"

    id_company: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    corporate_id: Mapped[int] = mapped_column(ForeignKey("corporates.id_corporate"), nullable=False)

    corporate = relationship("Corporate", back_populates="companies")
    departments = relationship("Department", back_populates="company")