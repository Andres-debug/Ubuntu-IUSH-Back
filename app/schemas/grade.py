from pydantic import BaseModel
from typing import Optional

class GradeBase(BaseModel):
    student_id: int
    course_id: int
    term: str
    grade_value: float
    grade_type: Optional[str]

class GradeCreate(GradeBase):
    pass

class GradeUpdate(GradeBase):
    pass

class GradeInDB(GradeBase):
    id: int
    recorded_at: str

    class Config:
        orm_mode = True