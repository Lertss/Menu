from models.database import Base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship


class CaseState(Base):
    __tablename__ = 'case_state'

    id = Column(Integer, primary_key=True)
    case_state_name = Column(String)
    case = relationship('Case')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    pomiar = Column(String, nullable=False)
    turn_number = Column(Integer, unique=True, autoincrement=True, nullable=False)
    case = relationship('Case')

    def __repr__(self):
        return f"<Category(id={self.id}, category_name={self.category_name}, pomiar={self.pomiar}, turn_number={self.turn_number})>"
