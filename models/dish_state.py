from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


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
    dish = relationship("Dish", cascade="all, delete-orphan")

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


class ColorString(Base):
    __tablename__ = "color_string"

    id = Column(Integer, primary_key=True)
    headline = Column(String, nullable=False, default="rgb(130, 174, 90)")
    category = Column(String, nullable=False, default="rgb(255, 126, 40)")
    main = Column(String, nullable=False, default="rgb(130, 174, 90);")
    masa = Column(String, nullable=False, default="yellow")
    cena = Column(String, nullable=False, default="yellow")
    english_dish = Column(String, nullable=False, default="rgb(130, 174, 90)")
    description = Column(String, nullable=False, default="rgb(130, 174, 90)")
    dodatki = Column(String, nullable=False, default="red")
