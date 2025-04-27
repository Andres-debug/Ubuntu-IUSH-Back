from pydantic import BaseModel
from typing import Optional
from app.schemas.enums import RecommendationTypeEnum

class RecommendationBase(BaseModel):
    student_id: int
    recommendation_type: RecommendationTypeEnum
    content: str
    source: Optional[str]
    related_course_id: Optional[int]
    is_viewed: Optional[bool] = False
    viewed_at: Optional[str]
    is_helpful: Optional[bool]
    feedback_comment: Optional[str]

class RecommendationCreate(RecommendationBase):
    pass

class RecommendationUpdate(RecommendationBase):
    pass

class RecommendationInDB(RecommendationBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True