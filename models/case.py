import logging

from models.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from models.database import Session


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    name_eng = Column(String, nullable=False)
    description = Column(String, nullable=False)
    description_english = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    masa = Column(Integer, nullable=False)
    case_state = Column(Integer, ForeignKey('case_state.id'))
    category = Column(Integer, ForeignKey('category.id'), nullable=False)

    def __init__(self, name: str = "", name_eng: str = "", description: str = "",
                 description_english: str = "", price: str = "", masa: str = "", category: str = ""):
        self.name = name
        self.name_eng = name_eng
        self.description = description
        self.description_english = description_english
        self.price = price
        self.masa = masa
        self.category = category
        self.case_state = 2

    def update_state(self):
        session = Session()
        session.query(Case).filter(Case.id == self.id).update({Case.case_state: self.case_state})
        session.commit()
        session.close()
        logging.info("Sukces zmiany statusa dania. *update_state")

    @staticmethod
    def delete_case(case_id):
        session = Session()
        case_to_delete = session.query(Case).filter_by(id=case_id).first()
        if case_to_delete:
            session.delete(case_to_delete)
            session.commit()
            session.close()
            logging.info(f'Danie z ID {case_id} zostało usunięte. *Case.delete_danie')

        else:
            logging.error(f'Danie z ID {case_id} nie znaleziono. *delete_danie')
            session.close()

    @staticmethod
    def create_case(category, name, name_eng, description, description_eng, masa, cena):
        session = Session()
        new_case = Case(name, name_eng, description, description_eng, masa, cena, category)
        if new_case:
            session.add(new_case)
            session.commit()
            session.close()
            logging.info("Danie stworzono. *Case.create_case")
        else:
            logging.error("Bląd stworzenia dania. *Case.create_case")
            session.close()

    @staticmethod
    def update_case(case_id, category, name, name_eng, description, description_eng, masa, cena):
        session = Session()
        danie_to_update = session.query(Case).filter_by(id=case_id).first()

        if danie_to_update:
            danie_to_update.category = category
            danie_to_update.name = name
            danie_to_update.name_eng = name_eng
            danie_to_update.description = description
            danie_to_update.description_english = description_eng
            danie_to_update.masa = masa
            danie_to_update.price = cena

            session.commit()

            session.refresh(danie_to_update)
            session.close()
            logging.info("Danie zostało zaktualizowane. *Case.update_case")
        else:
            logging.error(f'Danie z ID {case_id} nie znaleziono *Case.update_case')
            session.close()

    def __repr__(self):
        return f' [{self.name} ID: {self.id}, state: {self.case_state}]'
