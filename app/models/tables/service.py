from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base


class Service(Base):
    """
    Represents a service stored in the database. 

    Attributes:
        id_service (int): Unique identifier of the Service.
        name (str): Official name of the Service.
        department_id: Foreign key referencing the parent Department
    
    Relationships:
        department (Department): Many-to-one relationship pointing to the
        Department this service belongs to.
    
    Notes:
        - The name must be 100 characters max.
        - The name is required
    """
    __tablename__ = "services"

    id_service: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("departments.id_department"), nullable=False)

    department = relationship("Department", back_populates="services")
    