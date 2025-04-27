from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Index
from sqlalchemy.sql import func
from app.db.base import Base

class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True, index=True)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_faculty_university_name", "university_id", "name", unique=True),)