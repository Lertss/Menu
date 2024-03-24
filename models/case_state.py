from models.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class CaseState(Base):
    __tablename__ = 'case_state'

    id = Column(Integer, primary_key=True)
    case_state_name = Column(String)
    case = relationship('Case')

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    pomiar = Column(String)
    case = relationship('Case')