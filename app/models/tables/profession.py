from typing import Any, Optional

from sqlalchemy import String, Integer, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

from databases.postgresql import Base


class Profession(Base):
    """
    Represents a profession stored in the database.

    Attributes:
        id_profession (int): Unique identifier of the profession.
        name (str): Official name of the profession.
        default_account_allowed (bool): Whether the profession needs an account.
        default_material_allowed (bool): Whether the profession needs materials.
        default_material (dict): Materials needed by the profession.

    Notes:
        - The name is required.
        - The name must be 100 characters max.
    """

    __tablename__ = "professions"

    id_profession: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    default_account_allowed: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text("FALSE"))
    default_material_allowed: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text("FALSE"))
    default_material: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
