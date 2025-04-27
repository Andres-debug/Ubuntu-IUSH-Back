from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Index
from sqlalchemy.sql import func
from app.db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    program_id = Column(Integer, ForeignKey("programs.id"), nullable=False)
    course_code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    credits = Column(Integer)
    term_offered = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_course_program_code", "program_id", "course_code", unique=True),)