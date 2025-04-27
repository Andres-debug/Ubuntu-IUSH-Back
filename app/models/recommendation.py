from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Text, Boolean, Enum, Index
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import RecommendationTypeEnum

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    recommendation_type = Column(Enum(RecommendationTypeEnum), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    related_course_id = Column(Integer, ForeignKey("courses.id"))
    is_viewed = Column(Boolean, default=False)
    viewed_at = Column(TIMESTAMP)
    is_helpful = Column(Boolean)
    feedback_comment = Column(Text)

    __table_args__ = (Index("ix_recommendation_unique", "student_id", "recommendation_type", "created_at"),)