from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base

class Department(Base):
    """
    Represents a department stored in the database.

    Attributes:
        id_department (int): Unique identifier of the Department.
        name (str): Official name of the Department.
        company_id (int): Foreign key referencing the parent Company.

    Relationships:
        company (Company): Many-to-one relationship pointing to the
        Company this department belongs to.
        services: One-to-many relationship with the Service model

    Notes:
        - The name must be 100 characters max.
        - The name is required.
    """
    __tablename__ = "departments"

    id_department: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id_company") ,nullable=False)

    company = relationship("Company", back_populates="departments")
    services = relationship("Service", back_populates="department")