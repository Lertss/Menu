from models.database import Base, Session
from PySide6.QtWidgets import QMessageBox
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    description_english = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    masa = Column(Integer)
    dish_state = Column(Integer, ForeignKey("dish_state.id"))
    category = Column(Integer, ForeignKey("category.id"), nullable=False)

    def __init__(
        self,
        name: str = "",
        description: str = "",
        description_english: str = "",
        price: str = "",
        masa: str = "",
        category: str = "",
    ):
        self.name = name
        self.description = description
        self.description_english = description_english
        self.price = price
        self.masa = masa
        self.category = category
        self.dish_state = 2

    def update_state(self):
        session = Session()
        session.query(Dish).filter(Dish.id == self.id).update({Dish.dish_state: self.dish_state})
        session.commit()
        session.close()

    @staticmethod
    def delete_dish(dish_id):
        session = Session()
        dish_to_delete = session.query(Dish).filter_by(id=dish_id).first()
        if dish_to_delete:
            session.delete(dish_to_delete)
            session.commit()
            session.close()

        else:
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Danie z ID {dish_id} nie znaleziono.")
            msgbox.exec()

            session.close()

    @staticmethod
    def create_dish(category, name, description, description_eng, masa, cena):
        session = Session()
        new_dish = Dish(name, description, description_eng, masa, cena, category)
        if new_dish:
            session.add(new_dish)
            session.commit()
            session.close()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText("Bląd stworzenia dania. *Dish.create_dish")
            msgbox.exec()

            session.close()

    @staticmethod
    def update_dish(dish_id, category, name, description, description_eng, masa, cena):
        session = Session()
        danie_to_update = session.query(Dish).filter_by(id=dish_id).first()

        if danie_to_update:
            danie_to_update.category = category
            danie_to_update.name = name

            danie_to_update.description = description
            danie_to_update.description_english = description_eng
            danie_to_update.masa = masa
            danie_to_update.price = cena

            session.commit()

            session.refresh(danie_to_update)
            session.close()
        else:
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Danie z ID {dish_id} nie znaleziono *Dish.update_dish")
            msgbox.exec()
            session.close()

    def __repr__(self):
        return f" [{self.name} ID: {self.id}, state: {self.dish_state}]"
