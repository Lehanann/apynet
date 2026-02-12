from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base



class Candidate(Base):
    """
    Represents an candidate stored in the database.

    Attributes:
        id_candidate (int): Unique identifier of the candidate.
        first_name (str): First name of the candidate.
        last_name (str): Last name of the candidate.
        email (str): Personal email address of the candidate.
        phone (str): Personal phone of the candidate
        archived (bool): Status of the candidate.

    Relationship:
        candidate_steps: One-to-many relationship with the CandidateStep model
    """

    __tablename__ = "candidates"

    id_candidate: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    archived: Mapped[bool] = mapped_column(Boolean, server_default='false')

    candidate_steps = relationship("CandidateStep", back_populates='candidate')