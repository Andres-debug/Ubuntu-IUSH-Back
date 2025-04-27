from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Float, Enum, JSON, Index
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import PredictionTypeEnum

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    prediction_type = Column(Enum(PredictionTypeEnum), nullable=False)
    predicted_value_numeric = Column(Float)
    predicted_value_category = Column(String)
    confidence_score = Column(Float)
    prediction_timestamp = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    model_version = Column(String)
    related_course_id = Column(Integer, ForeignKey("courses.id"))
    input_data_snapshot = Column(JSON)

    __table_args__ = (Index("ix_prediction_unique", "student_id", "prediction_type", "prediction_timestamp"),)