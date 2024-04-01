import logging

from models.case import Case
from models.case_state import CaseState, Category
from models.database import create_db, Session

from PySide6.QtWidgets import QMessageBox

def create_database():
    try:
        create_db()
        session = Session()
        session.add(CaseState(case_state_name="Menu dziś"))
        session.add(CaseState(case_state_name="Menu cale"))
        session.commit()
        session.close()
        logging.info("DB stworzono. *create_database")
    except Exception as e:
        show_error_message(str(e))
        logging.error(f"DB nie stworzono.{show_error_message(str(e))}. *create_database")

class Worker:
    def __init__(self, session: Session):
        self.session = session

    def createCase(self, state: CaseState) -> Case:
        try:
            case = Case(state.id)
            self.session.add(case)
            self.session.commit()
            self.session.close()
            logging.info("DB stworzono. *Worker.createCase")
            return case

        except Exception as e:
            show_error_message(str(e))
            logging.error(f"DB nie stworzono. {show_error_message(str(e))}. *Worker.createCase")
            return None

    def getStates(self) -> list[CaseState]:
        try:
            logging.info("Sukces. *Worker.getStates")
            return [it for it in self.session.query(CaseState)]
        except Exception as e:
            show_error_message(str(e))
            logging.error(f"Bląd. {show_error_message(str(e))}. *Worker.getStates")
            return []

    def getCases(self, state: CaseState) -> list[Case]:
        try:
            cases = self.session.query(Case).filter(Case.case_state == state.id)
            cases = cases.join(Category, Case.category == Category.id)
            cases = cases.order_by(Category.turn_number, Case.name)
            logging.info("Sukces. *Worker.getCases")
            return [case for case in cases]
        except Exception as e:
            show_error_message(str(e))
            logging.error(f"Bląd. {show_error_message(str(e))}. *Worker.getCases")
            return []

    def getCategories(self) -> list[Category]:
        try:
            logging.info("Sukces. *Worker.getCategories")
            return [category for category in self.session.query(Category)]
        except Exception as e:
            show_error_message(str(e))
            logging.error(f"Bląd. {show_error_message(str(e))}. *Worker.getCategories")
            return []

    def getCategoryIdByName(self, category_name):
        try:
            session = Session()
            category = session.query(Category).filter_by(category_name=category_name).first()
            session.close()
            logging.info("Sukces. *Worker.getCategoryIdByName")
            if category:
                return category.id
            else:
                return None
        except Exception as e:
            show_error_message(str(e))
            logging.error(f"Bląd. {show_error_message(str(e))}. *Worker.getCategoryIdByName")
            return None

    def __del__(self):
        try:
            self.session.commit()
            self.session.close()
            logging.info("Sukces. *Worker.__del__")
        except Exception as e:
            show_error_message(str(e))
            logging.error(f"Bląd. {show_error_message(str(e))}. *Worker.__del__")

def show_error_message(error_message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(error_message)
    msg.setWindowTitle("Error")
    msg.exec_()
    logging.info("Sukces. *show_error_message")
