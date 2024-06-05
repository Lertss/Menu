from PySide6.QtWidgets import QMessageBox

from models.database import Session, create_db
from models.dish import Dish
from models.dish_state import Category, DishState, Dodatki


def create_database():
    try:
        create_db()
        session = Session()
        session.add(DishState(dish_state_name="Menu dziś"))
        session.add(DishState(dish_state_name="Menu cale"))
        session.commit()
        session.close()
    except Exception as e:
        show_error_message(str(e))
        msgbox = QMessageBox()
        msgbox.setText("Bląd:")
        msgbox.setInformativeText(f"DB nie stworzono.{show_error_message(str(e))}.")
        msgbox.exec()


class Worker:
    def __init__(self, session: Session):
        self.session = session

    def createDish(self, state: DishState) -> Dish:
        try:
            dish = Dish(state.id)
            self.session.add(dish)
            self.session.commit()
            self.session.close()
            return dish

        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(
                f"DB nie stworzono. {show_error_message(str(e))}."
            )
            msgbox.exec()
            return None
        finally:
            self.session.close()

    def getStates(self) -> list[DishState]:
        try:
            return [it for it in self.session.query(DishState)]
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()

            return []
        finally:
            self.session.close()

    def getDishs(self, state: DishState) -> list[Dish]:
        try:
            dishs = self.session.query(Dish).filter(Dish.dish_state == state.id)
            dishs = dishs.join(Category, Dish.category == Category.id)
            dishs = dishs.order_by(Category.turn_number, Dish.name)
            return [dish for dish in dishs]
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()
            return []
        finally:
            self.session.close()

    def searchDishs(self, search_term: str) -> list[Dish]:
        try:
            # Modify the query according to your search criteria
            dishs = self.session.query(Dish).filter(Dish.name.contains(search_term))
            return [dish for dish in dishs]
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(
                f"Bląd wyszukiwania. {show_error_message(str(e))}."
            )
            msgbox.exec()
            return []
        finally:
            self.session.close()

    def getCategories(self) -> list[Category]:
        try:
            return self.session.query(Category).order_by(Category.turn_number).all()
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()
            return []
        finally:
            self.session.close()

    def getCategoryIdByName(self, category_name):
        try:
            session = Session()
            category = (
                session.query(Category).filter_by(category_name=category_name).first()
            )
            session.close()
            if category:
                return category.id
            else:
                return None
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()
            return None
        finally:
            self.session.close()

    def getDodatki(self):
        return [dodatki for dodatki in self.session.query(Dodatki)]

    def __del__(self):
        try:
            self.session.commit()
            self.session.close()
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()


def show_error_message(error_message):
    msg = QMessageBox()
    msg.setText("Error")
    msg.setInformativeText(error_message)
    msg.setWindowTitle("Error")
    msg.exec_()
