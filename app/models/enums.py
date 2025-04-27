from sqlalchemy import Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AttendanceStatusEnum(str, Enum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    LATE = "LATE"
    EXCUSED = "EXCUSED"

class PredictionTypeEnum(str, Enum):
    STRESS_LEVEL = "STRESS_LEVEL"
    DROPOUT_RISK = "DROPOUT_RISK"
    EMOTIONAL_STATE = "EMOTIONAL_STATE"

class RecommendationTypeEnum(str, Enum):
    STUDY_HABIT = "STUDY_HABIT"
    WELLBEING = "WELLBEING"
    ORGANIZATION = "ORGANIZATION"
    ACADEMIC_RESOURCE = "ACADEMIC_RESOURCE"
    SUPPORT_SERVICE = "SUPPORT_SERVICE"

class LearningStyleEnumDB(str, Enum):
    VISUAL = "VISUAL"
    AUDITORY = "AUDITORY"
    KINESTHETIC = "KINESTHETIC"
    READING_WRITING = "READING_WRITING"
    UNDEFINED = "UNDEFINED"

class DegreeLevelEnum(str, Enum):
    BACHELOR = "BACHELOR"
    MASTER = "MASTER"
    DOCTORATE = "DOCTORATE"
    TECHNICAL = "TECHNICAL"
    ASSOCIATE = "ASSOCIATE"
    OTHER = "OTHER"