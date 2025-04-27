from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class University(Base):
    __tablename__ = "universities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    short_name = Column(String, unique=True)
    city = Column(String)
    country = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)