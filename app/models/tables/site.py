from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base


class Site(Base):
    """
    Represents a site stored in the database. 

    Attributes:
        id_site (int): Unique identifier of the Site.
        name (str): Official name of the Site.
        address (str): Address of the site.
        company_id: Foreign key referencing the parent Company
    
    Relationships:
        company (Company): Many-to-one relationship pointing to the
        Company this site belongs to.
    
    Notes:
        - The name must be 100 characters max.
        - The name is required
    """
    __tablename__ = "sites"

    id_site: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(Text)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id_company"), nullable=False)

    company = relationship("Company", back_populates="sites")
    meeting_rooms = relationship("MeetingRoom",back_populates="site")