from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Enum, Date, Index
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import AttendanceStatusEnum

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    session_date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatusEnum), nullable=False)
    recorded_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_attendance_unique", "student_id", "course_id", "session_date", unique=True),)