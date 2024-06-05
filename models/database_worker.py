

from models.case import Case
from models.case_state import CaseState, Category, Dodatki
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
    except Exception as e:
        show_error_message(str(e))
        msgbox = QMessageBox()
        msgbox.setText("Bląd:")
        msgbox.setInformativeText(f"DB nie stworzono.{show_error_message(str(e))}.")
        msgbox.exec()


class Worker:
    def __init__(self, session: Session):
        self.session = session

    def createCase(self, state: CaseState) -> Case:
        try:
            case = Case(state.id)
            self.session.add(case)
            self.session.commit()
            self.session.close()
            return case

        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"DB nie stworzono. {show_error_message(str(e))}.")
            msgbox.exec()
            return None
        finally:
            self.session.close()

    def getStates(self) -> list[CaseState]:
        try:
            return [it for it in self.session.query(CaseState)]
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()

            return []
        finally:
            self.session.close()

    def getCases(self, state: CaseState) -> list[Case]:
        try:
            cases = self.session.query(Case).filter(Case.case_state == state.id)
            cases = cases.join(Category, Case.category == Category.id)
            cases = cases.order_by(Category.turn_number, Case.name)
            return [case for case in cases]
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd. {show_error_message(str(e))}.")
            msgbox.exec()
            return []
        finally:
            self.session.close()

    def searchCases(self, search_term: str) -> list[Case]:
        try:
            # Змінюйте запит відповідно до ваших критеріїв пошуку
            cases = self.session.query(Case).filter(Case.name.contains(search_term))
            return [case for case in cases]
        except Exception as e:
            show_error_message(str(e))
            msgbox = QMessageBox()
            msgbox.setText("Bląd:")
            msgbox.setInformativeText(f"Bląd wyszukiwania. {show_error_message(str(e))}.")
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
            category = session.query(Category).filter_by(category_name=category_name).first()
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
