from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Enum, Index
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import DegreeLevelEnum

class Program(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True, index=True)
    faculty_id = Column(Integer, ForeignKey("faculties.id"), nullable=False)
    name = Column(String, nullable=False)
    degree_level = Column(Enum(DegreeLevelEnum), nullable=False)
    program_code = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    __table_args__ = (Index("ix_program_faculty_name_level", "faculty_id", "name", "degree_level", unique=True),)