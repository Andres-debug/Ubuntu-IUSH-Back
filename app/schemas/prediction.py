from pydantic import BaseModel
from typing import Optional
from app.schemas.enums import PredictionTypeEnum

class PredictionBase(BaseModel):
    student_id: int
    prediction_type: PredictionTypeEnum
    predicted_value_numeric: Optional[float]
    predicted_value_category: Optional[str]
    confidence_score: Optional[float]
    related_course_id: Optional[int]
    input_data_snapshot: Optional[dict]

class PredictionCreate(PredictionBase):
    pass

class PredictionUpdate(PredictionBase):
    pass

class PredictionInDB(PredictionBase):
    id: int
    prediction_timestamp: str
    model_version: Optional[str]

    class Config:
        orm_mode = True

class StressPredictionInput(BaseModel):
    grades: list[float]
    attendance: float
    total_hours: float

class StressPredictionOutput(BaseModel):
    stress_level: str
    confidence_score: float