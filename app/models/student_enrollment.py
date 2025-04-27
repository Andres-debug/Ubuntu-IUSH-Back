from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Index
from sqlalchemy.sql import func
from app.db.base import Base

class StudentEnrollment(Base):
    __tablename__ = "student_enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    enrollment_term = Column(String, nullable=False)
    enrollment_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    status = Column(String, default="Enrolled")

    __table_args__ = (Index("ix_student_enrollment_unique", "student_id", "course_id", "enrollment_term", unique=True),)