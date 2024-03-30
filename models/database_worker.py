from models.case import Case
from models.case_state import CaseState, Category
from models.database import create_db, Session


def create_database():
    create_db()
    session = Session()
    session.add(CaseState(case_state_name="Menu dziś"))
    session.add(CaseState(case_state_name="Menu cale"))
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

    def getCategoryIdByName(self, category_name):
        session = Session()
        category = session.query(Category).filter_by(category_name=category_name).first()
        session.close()
        if category:
            return category.id
        else:
            return None

    def __del__(self):
        self.session.commit()
        self.session.close()