from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Enum, Index
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import LearningStyleEnumDB

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)
    program_id = Column(Integer, ForeignKey("programs.id"), nullable=False)
    university_student_id = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    enrollment_year = Column(Integer)
    current_status = Column(String)
    learning_style = Column(Enum(LearningStyleEnumDB), default=LearningStyleEnumDB.UNDEFINED)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP)

    __table_args__ = (
        Index("ix_student_university_student_id", "university_id", "university_student_id", unique=True),
    )