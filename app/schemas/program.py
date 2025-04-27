from pydantic import BaseModel
from typing import Optional
from app.schemas.enums import DegreeLevelEnum

class ProgramBase(BaseModel):
    faculty_id: int
    name: str
    degree_level: DegreeLevelEnum
    program_code: Optional[str]

class ProgramCreate(ProgramBase):
    pass

class ProgramUpdate(ProgramBase):
    pass

class ProgramInDB(ProgramBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True