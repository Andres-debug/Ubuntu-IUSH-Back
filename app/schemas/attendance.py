from pydantic import BaseModel
from app.schemas.enums import AttendanceStatusEnum

class AttendanceBase(BaseModel):
    student_id: int
    course_id: int
    session_date: str
    status: AttendanceStatusEnum

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceUpdate(AttendanceBase):
    pass

class AttendanceInDB(AttendanceBase):
    id: int
    recorded_at: str

    class Config:
        orm_mode = True