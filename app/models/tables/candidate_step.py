from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ENUM
from databases.postgresql import Base
from app.utils.step_name_enum import StepNameEnum
from app.utils.step_result_enum import StepResultEnum
from datetime import date

class CandidateStep(Base):
    """
    Represents a step of candidacy stored in the database.

    Attributes:
        id_step (int): Unique identifier of the step candidacy.
        candidate_id (int): Foreign key referencing the parent candidate.
        step_name (SteNameEnum): The name of the candidacy's step.
        result (StepResultEnum): Status of the candidacy.
        step_date(date): Date of the candidate step.

    Relationship:
        candidate (Candidate): Many-to-one relationship pointing to the
        Candidate these candidate steps belongs to.
    """

    __tablename__ = "candidate_steps"

    id_step: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    candidate_id: Mapped[int] = mapped_column(Integer, ForeignKey("candidates.id_candidate"), nullable=False)
    step_name: Mapped[StepNameEnum] = mapped_column(ENUM(StepNameEnum, name="step_name_enum", create_type=False), nullable=False)
    result: Mapped[StepResultEnum] = mapped_column(ENUM(StepResultEnum, name="step_result_enum", create_type=False), nullable=False, server_default='pending')
    step_date: Mapped[date] = mapped_column(Date)

    candidate = relationship("Candidate", back_populates='candidate_steps')