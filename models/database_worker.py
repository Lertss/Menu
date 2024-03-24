from models.case import Case
from models.case_state import CaseState, Category
from models.database import create_db, Session


def create_database():
    create_db()
    session = Session()
    session.add(CaseState(case_state_name="Menu dziś"))
    session.add(CaseState(case_state_name="Menu cale"))
    session.add(Category(category_name="Zupy"))
    session.add(Category(category_name="II Danie"))
    session.commit()
    session.close()


class Worker:
    def __init__(self, session: Session):
        self.session = session

    def createCase(self, state: CaseState) -> Case:
        case = Case(state.id)
        self.session.add(case)
        self.session.commit()
        self.session.close()
        return case

    def getStates(self) -> list[CaseState]:
        return [it for it in self.session.query(CaseState)]

    def getCases(self, state: CaseState) -> list[Case]:
        return [it for it in self.session.query(Case).filter(Case.case_state == state.id).order_by(Case.name.asc())]

    def getCategories(self) -> list[Category]:
        return [category for category in self.session.query(Category)]

    def __del__(self):
        self.session.commit()
        self.session.close()