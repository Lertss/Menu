from models.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class DishState(Base):
    __tablename__ = "dish_state"

    id = Column(Integer, primary_key=True)
    dish_state_name = Column(String)
    dish = relationship("Dish")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    category_eng_name = Column(String, nullable=False)
    pomiar = Column(String, nullable=False)
    turn_number = Column(Integer, unique=True, autoincrement=True, nullable=False)
    dish = relationship("Dish")

    def __repr__(self):
        return (
            f"<Category(id={self.id}, category_name={self.category_name}, "
            f"category_eng_name={self.category_eng_name}, pomiar={self.pomiar}, turn_number={self.turn_number})>"
        )


class Dodatki(Base):
    __tablename__ = "additions"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    text_eng = Column(String, nullable=False)
