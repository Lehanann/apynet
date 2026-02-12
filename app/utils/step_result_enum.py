from enum import Enum

class StepResultEnum(str, Enum):
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'