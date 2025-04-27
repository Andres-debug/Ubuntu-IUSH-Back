from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    program_id: int
    course_code: str
    name: str
    credits: Optional[int]
    term_offered: Optional[str]

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class CourseInDB(CourseBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True