from sqlalchemy import Column, Integer, String, Float
from backend.core.database import Base

class Campaign(Base):

    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    job_title = Column(String)
    location = Column(String)
    budget = Column(Float)