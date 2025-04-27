from pydantic import BaseModel
from typing import Optional

class StudentEnrollmentBase(BaseModel):
    student_id: int
    course_id: int
    enrollment_term: str
    status: Optional[str] = "Enrolled"

class StudentEnrollmentCreate(StudentEnrollmentBase):
    pass

class StudentEnrollmentUpdate(StudentEnrollmentBase):
    pass

class StudentEnrollmentInDB(StudentEnrollmentBase):
    id: int
    enrollment_date: str

    class Config:
        orm_mode = True