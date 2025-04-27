from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.enums import LearningStyleEnumDB

class StudentBase(BaseModel):
    university_id: int
    program_id: int
    university_student_id: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    enrollment_year: Optional[int]
    current_status: Optional[str]
    learning_style: Optional[LearningStyleEnumDB] = LearningStyleEnumDB.UNDEFINED

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentInDB(StudentBase):
    id: int
    created_at: str
    updated_at: Optional[str]

    class Config:
        orm_mode = True