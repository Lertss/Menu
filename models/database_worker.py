from PySide6.QtWidgets import QMessageBox

from models.database import Session, create_db
from models.dish import Dish
from models.dish_state import Category, DishState, Dodatki, ColorString


def create_database():
    try:
        create_db()
        with Session() as session:
            session.add(DishState(dish_state_name="Menu dziś"))
            session.add(DishState(dish_state_name="Menu cale"))
            session.commit()
        createDefaultColor()
    except Exception as e:
        show_error_message(f"DB nie stworzono.{str(e)}")


def createDish(state: DishState) -> Dish:
    try:
        with Session() as session:
            dish = Dish(state.id)
            session.add(dish)
            session.commit()
            return dish

    except Exception as e:
        show_error_message(str(e))
        return None


def getStates() -> list[DishState]:
    try:
        with Session() as session:
            return [it for it in session.query(DishState)]
    except Exception as e:
        show_error_message(str(e))
        return []


def getDishs(state: DishState) -> list[Dish]:
    try:
        with Session() as session:
            dishs = session.query(Dish).filter(Dish.dish_state == state.id)
            dishs = dishs.join(Category, Dish.category == Category.id)
            dishs = dishs.order_by(Category.turn_number, Dish.name)
            return [dish for dish in dishs]
    except Exception as e:
        show_error_message(str(e))
        return []


def searchDishs(search_term: str) -> list[Dish]:
    try:
        with Session() as session:
            dishs = session.query(Dish).filter(Dish.name.contains(search_term))
            return [dish for dish in dishs]
    except Exception as e:
        show_error_message(str(e))
        return []


def getCategories() -> list[Category]:
    try:
        with Session() as session:
            return session.query(Category).order_by(Category.turn_number).all()
    except Exception as e:
        show_error_message(str(e))
        return []


def getCategoryIdByName(category_name):
    try:
        with Session() as session:
            category = (
                session.query(Category).filter_by(category_name=category_name).first()
            )
            if category:
                return category.id
            else:
                return None
    except Exception as e:
        show_error_message(str(e))
        return None

def getDodatki():
        with Session() as session:
            return [dodatki for dodatki in session.query(Dodatki)]

def createDefaultColor():
    with Session() as session:
        session.add(ColorString(headline="rgb(130, 174, 90)",
                                category="rgb(255, 126, 40)",
                                main="rgb(130, 174, 90);",
                                masa="yellow",
                                cena="yellow",
                                english_dish="rgb(130, 174, 90)",
                                description="rgb(130, 174, 90)",
                                dodatki="red",
                                ))
        session.commit()

def update_color(color, string_update):
    def update_first_element(sessions, colors, string_updates):
        """Function to update the attribute of the first element"""
        first_element = session.query(ColorString).first()
        if first_element and hasattr(first_element, string_updates):
            setattr(first_element, string_updates, colors)
        else:
            raise AttributeError(show_error_message(f"'ColorString' об'єкт не має атрибута '{string_update}'"))
    try:
        with Session() as session:
            count = session.query(ColorString).count()

            if count == 0:
                createDefaultColor()
            elif count > 1:
                session.query(ColorString).delete()
                session.commit()
                createDefaultColor()

            update_first_element(session, color, string_update)
            session.commit()
    except Exception as e:
        show_error_message(str(e))

def getColor():
    with Session() as session:
        return session.query(ColorString).first()

def show_error_message(error_message):
    msg = QMessageBox()
    msg.setText("Bląd:")
    msg.setInformativeText(error_message)
    msg.setWindowTitle("Bląd:")
    msg.exec_()
