from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class SiteBase(BaseModel):
    """
    Base schema for the site, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        name (str): Official name of the site.
        address (str): Address of the site
        company_id (int): ID of the parent corporate.

    Notes:
        - The name must be 100 characters max.
        - The name is required.
        - The corporate_id is required and refers to the parent corporate.
    """
    name: str = Field(..., max_length=100, description="Official name of the site.")
    address: Optional[str] = Field(None, description="Address of the site.")
    company_id: int = Field(...,  description="ID of the parent corporate.")

class SiteCreate(SiteBase):
    """
    Schema used when creating a new site.

    Inherits all fields from SiteBase schema.
    """
    pass

class SiteUpdate(SiteBase):
    """
    Schema used when updating an existing site.

    All fields inherited from SiteBase become optional.
    Only fields provided in the request will be updated.
    """
    name: Optional[str] = None
    address: Optional[str] = None
    company_id: Optional[int] = None

class SiteRead(SiteBase):
    """
    Schema used when reading a site from the database.

    Inherits all fields from SiteBase schema.

    Attributes:
        id_site (int): Unique identifier of the site.
    """
    id_site: int

    model_config = ConfigDict(from_attributes=True)