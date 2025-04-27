from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Float, Index
from sqlalchemy.sql import func
from app.db.base import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    term = Column(String, nullable=False)
    grade_value = Column(Float, nullable=False)
    grade_type = Column(String)
    recorded_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_grade_unique", "student_id", "course_id", "term", "grade_type", unique=True),)