from pydantic import BaseModel
from typing import Optional

class FacultyBase(BaseModel):
    university_id: int
    name: str

class FacultyCreate(FacultyBase):
    pass

class FacultyUpdate(FacultyBase):
    pass

class FacultyInDB(FacultyBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True