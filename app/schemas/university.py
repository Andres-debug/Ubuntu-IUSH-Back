from pydantic import BaseModel
from typing import Optional

class UniversityBase(BaseModel):
    name: str
    short_name: Optional[str]
    city: Optional[str]
    country: Optional[str]

class UniversityCreate(UniversityBase):
    pass

class UniversityUpdate(UniversityBase):
    pass

class UniversityInDB(UniversityBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True