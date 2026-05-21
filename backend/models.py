from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Calculation(Base):
    __tablename__ = 'calculations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    operation = Column(String)
    num1 = Column(Float)
    num2 = Column(Float)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
